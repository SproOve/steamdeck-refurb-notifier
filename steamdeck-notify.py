from bs4 import BeautifulSoup
import requests

url64g = 'https://api.steampowered.com/IPhysicalGoodsService/CheckInventoryAvailableByPackage/v1?origin=https:%2F%2Fstore.steampowered.com&input_protobuf_encoded=COGVNxICREU%3D'
url256g = 'https://api.steampowered.com/IPhysicalGoodsService/CheckInventoryAvailableByPackage/v1?origin=https:%2F%2Fstore.steampowered.com&input_protobuf_encoded=COKVNxICREU%3D'
url512g = 'https://api.steampowered.com/IPhysicalGoodsService/CheckInventoryAvailableByPackage/v1?origin=https:%2F%2Fstore.steampowered.com&input_protobuf_encoded=COOVNxICREU%3D'
resp64 = requests.get(url64g)
resp256 = requests.get(url256g)
resp512 = requests.get(url512g)

if resp64.text == "\x08\x01\x10\x00":
    ava64 = True
elif resp64.text == "\x08\x00\x10\x00":
    ava64 = False
    
if resp256.text == "\x08\x01\x10\x00":
    ava256 = True
elif resp256.text == "\x08\x00\x10\x00":
    ava256 = False
    
if resp512.text == "\x08\x01\x10\x00":
    ava512 = True
elif resp512.text == "\x08\x00\x10\x00":
    ava512 = False

# soup = BeautifulSoup(page.text, features="html.parser")



# container1 = soup.find_all("div", {"class" : "responsive_page_template_content" })



print(container1)

