from netmiko import ConnectHandler

CSR = {
    "device_type": "linux",
    "ip": "sandbox-nso-1.cisco.com",
    "username": "developer",
    "password": "Services4Ever"
}

net_connect = ConnectHandler(**CSR)
output = net_connect.send_command('show running-config devices device internet-rtr01 config interface | display json')
print(f'{type(output)} : \n{output}')
net_connect.disconnect()
