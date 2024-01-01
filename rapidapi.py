import requests

api_url = 'https://face-verification2.p.rapidapi.com/faceverification'
api_key = '653b5c6c39msh05142c1a49c9fa6p13fc75jsn586404778a62' 

image1_path = r'img1.png'

image2_path = r'img2.png'


files = {'Photo1': ( open(image1_path, 'rb')),
         'Photo2': ( open(image2_path, 'rb'))}
headers = {
    'X-RapidAPI-Key': '653b5c6c39msh05142c1a49c9fa6p13fc75jsn586404778a62',
    'X-RapidAPI-Host': 'face-verification2.p.rapidapi.com'
}
response = requests.post(api_url, files=files, headers=headers)

result_message = response.json().get('data', {}).get('resultMessage', 'Result not available')

print(result_message)