import json
from ipaddress import IPv4Network

def cidr(ip):
    return [str(ip) for ip in IPv4Network(ip)]

def main():
    
    ips = list()
    ipv4CIDR = list()
    ipv6 = list()

    ipv4ok = list()
    
    with open("m247-2.json", "r", encoding="UTF-8") as f:
        
        file = json.load(f)
        for i in range(len(file['data']['located_resources'])):
            #print(file['data']['located_resources'][0]['locations'][0]['resources'] ) 
            for j in range(len(file['data']['located_resources'][i]['locations'])):
                ips.extend( file['data']['located_resources'][i]['locations'][j]['resources'])
            
    
    #print(ips)
    for ip in ips:
        if '.' in ip:
            ipv4CIDR.append(ip)
        else:
            ipv6.append(ip)
    
    #print(ipv4CIDR)
    #print(ipv6)
    
    
    for ipv in ipv4CIDR:
        ipv4ok.extend( cidr(ipv) )

    with open("ipv4.txt","w", encoding="UTF-8") as f:
        for ip in ipv4ok:
            f.write(ip+"\n")
    
    with open("ipv6.txt","w", encoding="UTF-8") as f:
        for ip in ipv6:
            f.write(ip+"\n")
    
    
    #print(ipv4CIDR)
    
    pass

if __name__ == "__main__":
    main()