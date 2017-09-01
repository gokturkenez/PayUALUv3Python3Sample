'''   
Project: PayU Turkey ALU Python Sample
Author: Göktürk Enez
'''
# Importing required libraries for sample.
from datetime import datetime
import hmac
import hashlib
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# Endpoint
url = "https://secure.payu.com.tr/order/alu/v3"
# PayU Merchant's Secret Key
secret = 'SECRET_KEY'
# Array Begin
array = {
    # PayU Merchant's Merchant ID
    'MERCHANT': "OPU_TEST",
    'ORDER_REF':  "Test1234",
    'ORDER_DATE': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
    'BACK_REF': "http://2ac99a34.ngrok.io/",
    'ORDER_PNAME[0]': "Ürün İsmi",
    'ORDER_PCODE[0]': "Ürünkodu",
    'ORDER_PINFO[0]': "Ürün Açıklaması",
    'ORDER_PRICE[0]': "100",
    'ORDER_VAT[0]': "18",
    'ORDER_QTY[0]': "1",
    'ORDER_SHIPPING': "5",
    'PRICES_CURRENCY': "TRY",
    'PAY_METHOD': "CCVISAMC",
    'SELECTED_INSTALLMENTS_NUMBER': "2",
    'CC_NUMBER': "4355084355084358",
    'EXP_MONTH': "12",
    'EXP_YEAR': "2018",
    'CC_CVV': "000",
    'BILL_FNAME': "Adı",
    'BILL_LNAME': "Soyadı",
    'BILL_PHONE': "05316806562",
    'BILL_EMAIL': "payutest@mail.com",
    'BILL_COUNTRYCODE': "TR",

}
# Initialize the hashstring @param
hashstring = ''
# Sorting Array params
for k, v in sorted(array.items()):
# Adding the length of each field value at the beginning of field value
    hashstring += str(len(v)) + str(v)
print(hashstring)
# Calculating ORDER_HASH
signature = hmac.new(secret.encode('utf-8'), hashstring.encode('utf-8'), hashlib.md5).hexdigest()
# Adding ORDER_HASH param to dictionary
array['ORDER_HASH'] = signature
print(signature)
print()
# Sending Request to Endpoint
request = Request(url, urlencode(array).encode())
json = urlopen(request).read().decode()
# Printing result
print(json)


