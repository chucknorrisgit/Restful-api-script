import requests
URL = "https://ilorestfulapiexplorer.ext.hpe.com//redfish/v1/"
r = requests.get(url=URL, verify=False)
jdata = r.json()
name = jdata["Name"]
URL = "https://ilorestfulapiexplorer.ext.hpe.com//redfish/v1/systems/1"
r = requests.get(url=URL, verify=False)
jdata = r.json()
bootOrder = jdata["Boot"]["BootOrder"]
URL = "https://ilorestfulapiexplorer.ext.hpe.com//redfish/v1/systems/1/SmartStorage/"
r = requests.get(url=URL, verify=False)
jdata = r.json()
smartStorage = jdata["@odata.type"]
URL = "https://ilorestfulapiexplorer.ext.hpe.com//redfish/v1/systems/1/EthernetInterfaces/"
r = requests.get(url=URL, verify=False)
jdata = r.json()
count = int(jdata["Members@odata.count"])
ethernetInterfaces = list()
for i in range(1, count+1):
    URL = 'https://ilorestfulapiexplorer.ext.hpe.com//redfish/v1/systems/1/EthernetInterfaces/' + str(i) + '/'
    r = requests.get(url=URL, verify=False)
    jdata = r.json()
    ethernetInterfaces.append(jdata["MACAddress"])
print("name: " + name)
print("boot order: ", end="")
print(bootOrder)
print("smart storage battery module: " + smartStorage)
print("ethernet interfaces mac addresses: ", end="")
print(ethernetInterfaces)

