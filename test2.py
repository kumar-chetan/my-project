# import requests

# url = "https://face-verification2.p.rapidapi.com/faceverification"

# payload = {
# 	"image1Base64": r"C:\Users\kumar\OneDrive\Desktop\my_project\img1.png",
# 	"image2Base64": r"C:\Users\kumar\OneDrive\Desktop\my_project\img1.png"
# }
# headers = {
# 	"content-type": "application/x-www-form-urlencoded",
# 	"X-RapidAPI-Key": "653b5c6c39msh05142c1a49c9fa6p13fc75jsn586404778a62",
# 	"X-RapidAPI-Host": "face-verification2.p.rapidapi.com"
# }

# response = requests.post(url, data=payload, headers=headers)

# print(response.json())

import requests

api_url = 'https://face-verification2.p.rapidapi.com/faceverification'
api_key = '653b5c6c39msh05142c1a49c9fa6p13fc75jsn586404778a62'

image1_path = r'C:\Users\kumar\OneDrive\Desktop\my_project'
image1_name = r'\img1.png'
image2_path = r'C:\Users\kumar\OneDrive\Desktop\my_project'
image2_name = r'\img1.png'

files = {'Photo1': (image1_name, open(image1_path + image1_name, 'rb'), 'multipart/form-data'), 
          'Photo2': (image2_name, open(image2_path + image2_name, 'rb'), 'multipart/form-data')}
header = {
     'content-type': 'application/x-www-form-urlencoded',
    'X-RapidAPI-Key': '653b5c6c39msh05142c1a49c9fa6p13fc75jsn586404778a62',
    'X-RapidAPI-Host': 'face-verification2.p.rapidapi.com'
}
response = requests.post(api_url, files=files, headers=header)

print(response.json())