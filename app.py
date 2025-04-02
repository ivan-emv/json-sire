import requests

form_id = "WD4lUnn8"
token = "tfp_9sDQa5Ns2LeGtgxwiPp2hnYWsUcqnHG6Nv5VXbjmCXuR_e5CajswVJsC9"

url = f"https://api.typeform.com/forms/{form_id}"
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    form_data = response.json()
    print(form_data)
else:
    print("Error:", response.status_code, response.text)
