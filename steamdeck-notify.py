import requests, threading, os, json
import yagmail

json_path = os.path.join(os.getcwd()
, 'config.json')

with open(json_path, 'r') as f:
    config_dict = json.load(f)

pollInterval = config_dict.__getitem__('pollInterval')
notify64 = config_dict.__getitem__('notify64')
notify256 = config_dict.__getitem__('notify256')
notify512 = config_dict.__getitem__('notify512')
mailAcc = config_dict.__getitem__('mailAcc')
mailPW = config_dict.__getitem__('mailPW')

url64g = 'https://api.steampowered.com/IPhysicalGoodsService/CheckInventoryAvailableByPackage/v1?origin=https:%2F%2Fstore.steampowered.com&input_protobuf_encoded=COGVNxICREU%3D&format=json'
url256g = 'https://api.steampowered.com/IPhysicalGoodsService/CheckInventoryAvailableByPackage/v1?origin=https:%2F%2Fstore.steampowered.com&input_protobuf_encoded=COKVNxICREU%3D&format=json'
url512g = 'https://api.steampowered.com/IPhysicalGoodsService/CheckInventoryAvailableByPackage/v1?origin=https:%2F%2Fstore.steampowered.com&input_protobuf_encoded=COOVNxICREU%3D&format=json'

def sendMail(memory):
    body = "Steamdeck refurbished is available with " + memory + "GB of memory right now, check it out here \n https://store.steampowered.com/sale/steamdeckrefurbished"

    yag = yagmail.SMTP(mailAcc, mailPW, host='smtp.office365.com', port=587, smtp_starttls=True, smtp_ssl=False)
    yag.send(
        to=mailAcc,
        subject="Steamdeck refurbished is available with " + memory + "GB of space",
        contents=body
    )

def refreshStates():
    threading.Timer(pollInterval, refreshStates).start()
    resp64 = requests.get(url64g).json()
    resp256 = requests.get(url256g).json()
    resp512 = requests.get(url512g).json()

    ava64 = resp64.get('response').get('inventory_available')
    ava256 = resp256.get('response').get('inventory_available')
    ava512 = resp512.get('response').get('inventory_available')

    if notify64 == True and ava64 == True:
        sendMail("64")
    if notify256 == True and ava256 == True:
        sendMail("256")
    if notify512 == True and ava512 == True:
        sendMail("512")

refreshStates()

