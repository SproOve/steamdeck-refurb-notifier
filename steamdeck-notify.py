from bs4 import BeautifulSoup
import requests

url64g = 'https://api.steampowered.com/IPhysicalGoodsService/CheckInventoryAvailableByPackage/v1?origin=https:%2F%2Fstore.steampowered.com&input_protobuf_encoded=COGVNxICREU%3D&format=json'
url256g = 'https://api.steampowered.com/IPhysicalGoodsService/CheckInventoryAvailableByPackage/v1?origin=https:%2F%2Fstore.steampowered.com&input_protobuf_encoded=COKVNxICREU%3D&format=json'
url512g = 'https://api.steampowered.com/IPhysicalGoodsService/CheckInventoryAvailableByPackage/v1?origin=https:%2F%2Fstore.steampowered.com&input_protobuf_encoded=COOVNxICREU%3D&format=json'

resp64 = requests.get(url64g).json()
resp256 = requests.get(url256g).json()
resp512 = requests.get(url512g).json()

ava64 = resp64.get('response').get('inventory_available')
ava256 = resp256.get('response').get('inventory_available')
ava512 = resp512.get('response').get('inventory_available')

print(ava64)