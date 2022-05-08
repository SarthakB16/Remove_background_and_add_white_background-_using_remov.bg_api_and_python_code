from urllib import response
import requests
response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('D:\intern\intern.png', 'rb')},
    data={'size': 'auto', 'bg':'white','bg_type':'color'},
    headers={'X-Api-Key': 'Using_your_key_here'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)
