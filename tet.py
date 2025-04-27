import requests
import json
def get_homecolection():
    url = "https://gw.be.com.vn/api/v1/be-merchant-gateway/web/customer/get_home_collections"

    payload = json.dumps({
    "locale": "vi",
    "client_info": {
        "locale": "vi",
        "device_type": 3
    },
    "latitude": 10.77253621500006,
    "longitude": 106.69798153800008
    })
    headers = {
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjowLCJhdWQiOiJndWVzdCIsImV4cCI6MTc0NTgwMjgwMywiaWF0IjoxNzQ1NzE2NDAzLCJpc3MiOiJiZS1kZWxpdmVyeS1nYXRld2F5In0.72d0fyO8_OZwpSkrAr8wgMDcCTeblunPrnMHD3bt4jI',
    'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    #print(response.text)
    data = json.loads(response.text)
    return data