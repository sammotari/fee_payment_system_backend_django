import requests

def make_mpesa_request(url, headers, data):
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def get_access_token(consumer_key, consumer_secret):
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    headers = {
        "Authorization": f"Basic {DbAwmiHyggSaLNTCPqzXpv84AszQ}:{SaF0ttC3pcAeOxann512cAAAtGdyqGB8pcXmcrmiqxGtExj4F7FQ5pPFCnmtIWUc}",
        "Content-Type": "application/json"
    }
    response = make_mpesa_request(url, headers, {})
    return response.get("access_token")

def mpesa_stk_push(access_token, phone_number, amount, callback_url):
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "BusinessShortCode": "YourShortCode",
        "Password": "YourGeneratedPassword",
        "Timestamp": "YourGeneratedTimestamp",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": "YourShortCode",
        "PhoneNumber": phone_number,
        "CallBackURL": callback_url,
        "AccountReference": "YourAccountReference",
        "TransactionDesc": "Testing"
    }
    response = make_mpesa_request(url, headers, data)
    return response