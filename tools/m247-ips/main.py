import json
from ipaddress import IPv4Network
from requests import get
import os

AS = ["AS9009","AS16247"]
dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"

def cidr(ip):
    return [str(ip) for ip in IPv4Network(ip)]

def main():
    
    ips = list()
    ipv4CIDR = list()
    ipv6CIDR = list()

    ipv4 = list()

    for asn in AS:
        url = 'https://stat.ripe.net/data/maxmind-geo-lite-announced-by-as/data.json'
        PARAMS = {"resource": asn}
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

        r = get(url=url, params=PARAMS, headers=headers)
        file = r.json()

        for i in range(len(file['data']['located_resources'])):
            for j in range(len(file['data']['located_resources'][i]['locations'])):
                ips.extend( file['data']['located_resources'][i]['locations'][j]['resources'])
    
    for ip in ips:
        if '.' in ip:
            ipv4CIDR.append(ip)
        else:
            ipv6CIDR.append(ip)
    
    for ipv in ipv4CIDR:
        ipv4.extend( cidr(ipv) )

    with open(save_path+"ipv4CIDR.txt","w", encoding="UTF-8") as f:
        for ip in ipv4CIDR:
            f.write(ip+"\n")

    with open(save_path+"ipv4.txt","w", encoding="UTF-8") as f:
        for ip in ipv4:
            f.write(ip+"\n")
    
    with open(save_path+"ipv6CIDR.txt","w", encoding="UTF-8") as f:
        for ip in ipv6CIDR:
            f.write(ip+"\n")


if __name__ == "__main__":
    main()