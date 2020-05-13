from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.cache import cache
import xero

from xero import Xero
from xero.auth import OAuth2Credentials
from xero.constants import XeroScopes
from .models import Form

client_id = '49A1007E580642A489BC7CAA3B4A661C'
client_secret = 'jgmVIa00CB-KPGztOlAz7ATpsSjiiB0ZqFup0jDlV6SS4pWb'
callback_uri = 'https://infinite-stream-24407.herokuapp.com/form'

# Create your views here.

def login(request):
       return render(request,'login.html')


def form(request):
        if(request.method == 'POST'):
              productType = request.POST['productType']
              contactID = request.POST['contactID']
              date = request.POST['date']
              dueDate = request.POST['dueDate']
              lineAmountTypes = request.POST['lineAmountTypes']
              description = request.POST['description']
              quantity = request.POST['quantity']
              unitAmount = request.POST['unitAmount']
              accountCode = request.POST['accountCode']
              discountRate = request.POST['discountRate']
              if(productType and contactID and date and dueDate and lineAmountTypes and description and quantity and unitAmount and accountCode and discountRate ):

                    form = Form(productType=productType, contactID = contactID, date=date,dueDate=dueDate,lineAmountTypes=lineAmountTypes,
                          description=description,quantity=quantity,unitAmount=unitAmount,accountCode=accountCode,
                          discountRate=discountRate)
                    form.save()
                    jsonData = {
                            "Type": productType,
                            "Contact": {
                            "ContactID": contactID
                            },
                            "Date": date,
                            "DueDate": dueDate,
                            "DateString": "2009-05-27T00:00:00",
                            "DueDateString": "2009-06-06T00:00:00",
                            "LineAmountTypes": lineAmountTypes,
                            "LineItems": [
                            {
                            "Description": description,
                            "Quantity": quantity,
                            "UnitAmount": unitAmount,
                            "AccountCode": accountCode,
                            "DiscountRate": discountRate
                            }
                            ]}
                    jsonFetch = JsonResponse(jsonData)
                    print(jsonFetch)
                    #xero.contacts.put(jsonFetch)

                    return redirect(success)
              else:
                  return render(request,'form.html')
        else:
              return render(request,'form.html')


def start_xero_auth_view(request):
       # Get client_id, client_secret from config file or settings then
       credentials = OAuth2Credentials(
           client_id, client_secret, callback_uri=callback_uri,
           scope=[XeroScopes.OFFLINE_ACCESS, XeroScopes.ACCOUNTING_CONTACTS,
                  XeroScopes.ACCOUNTING_TRANSACTIONS]
       )
       authorization_url = credentials.generate_url()
       cache.set('xero_creds', credentials.state)
       return HttpResponseRedirect(authorization_url)

def process_callback_view(request):
       cred_state = cache.get('xero_creds')
       credentials = OAuth2Credentials(**cred_state)
       auth_secret = request.get_raw_uri()
       credentials.verify(auth_secret)
       credentials.set_default_tenant()
       cache.set('xero_creds', credentials.state)

def some_view_which_calls_xero(request):
       cred_state = cache.get('xero_creds')
       credentials = OAuth2Credentials(**cred_state)
       if credentials.expired():
           credentials.refresh()
           cache.set('xero_creds', credentials.state)
       xero = Xero(credentials)

       contacts = xero.contacts.all()

def success(request):
    return render(request,'message.html')

