
import json
from ipaddress import IPv4Network
from requests import get
import os
import csv

ips_csv = ["https://download.microsoft.com/download/B/2/A/B2AB28E1-DAE1-44E8-A867-4987FE089EBE/msft-public-ips.csv"]

ips_json = ["https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20200112.json",
"https://download.microsoft.com/download/6/4/D/64DB03BF-895B-4173-A8B1-BA4AD5D4DF22/ServiceTags_AzureGovernment_20200112.json",
"https://download.microsoft.com/download/0/7/6/076274AB-4B0B-4246-A422-4BAF1E03F974/ServiceTags_AzureGermany_20200112.json",
"https://download.microsoft.com/download/9/D/0/9D03B7E2-4B80-4BF3-9B91-DA8C7D3EE9F9/ServiceTags_China_20200112.json"]

dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"

def main():

    ips = list()
    ipv4CIDR = list()
    ipv6CIDR = list()
    
    for url in ips_json:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
        r = get(url=url, headers=headers)
        file = r.json()

        for i in range(len(file['values'])):
            ips.extend( file['values'][i]['properties']['addressPrefixes'])
    
    for url in ips_csv:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
        r = get(url=url, headers=headers)
        testo = r.text.split('\n')
        csv_reader = csv.reader(testo)
        csv_reader = list(csv_reader)
        for i in range(0,len(csv_reader)-1):
            ips.append(csv_reader[i][0])

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





if __name__ == "__main__":
    main()