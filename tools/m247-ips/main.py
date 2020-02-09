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
    
    ips = set()
    ipv4CIDR = list()
    ipv6CIDR = list()

    for asn in AS:
        url = 'https://stat.ripe.net/data/maxmind-geo-lite-announced-by-as/data.json'
        PARAMS = {"resource": asn}

        r = get(url=url, params=PARAMS)
        file = r.json()

        for obj in file['data']['located_resources']:
            ips.add(obj["resource"])
    
    for ip in ips:
        if '.' in ip:
            ipv4CIDR.append(ip)
        else:
            ipv6CIDR.append(ip)

    with open(save_path+"ipv4CIDR.txt","w", encoding="UTF-8") as f:
        for ip in ipv4CIDR:
            f.write(ip+"\n")
    
    with open(save_path+"ipv6CIDR.txt","w", encoding="UTF-8") as f:
        for ip in ipv6CIDR:
            f.write(ip+"\n")
    
    with open(save_path+"all.txt","w", encoding="UTF-8") as f:
        for ip in ips:
            f.write(ip+"\n")


if __name__ == "__main__":
    main()