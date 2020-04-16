import os
from requests import get

dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"


def main():

    ipv4CIDR = set()
    ipv6CIDR = set()

    url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

    r = get(url=url)
    file = r.json()

    for obj in file['prefixes']:
        ipv4CIDR.add(obj["ip_prefix"])

    for obj in file['ipv6_prefixes']:
        ipv6CIDR.add(obj["ipv6_prefix"])

    with open(save_path+"ipv4CIDR.txt","w", encoding="UTF-8") as f:
        for ip in ipv4CIDR:
            f.write(ip+"\n")
    
    with open(save_path+"ipv6CIDR.txt","w", encoding="UTF-8") as f:
        for ip in ipv6CIDR:
            f.write(ip+"\n")
    
    with open(save_path+"all.txt","w", encoding="UTF-8") as f:
        for ip in ipv4CIDR:
            f.write(ip+"\n")
        for ip in ipv6CIDR:
            f.write(ip+"\n")


if __name__ == "__main__":
    main()