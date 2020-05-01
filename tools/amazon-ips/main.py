import os
from requests import get

dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"


def main():

    ips = set()

    url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

    r = get(url=url)
    file = r.json()

    for obj in file['prefixes']:
        ips.add(obj["ip_prefix"])

    for obj in file['ipv6_prefixes']:
        ips.add(obj["ipv6_prefix"])

    with open(save_path+"ipv4CIDR.txt", "w", encoding="UTF-8") as ipv4F, open(save_path+"ipv6CIDR.txt", "w", encoding="UTF-8") as ipv6F, open(save_path+"all.txt", "w", encoding="UTF-8") as allF:
        for ip in ips:
            allF.write(ip+"\n")
            if '.' in ip:
                ipv4F.write(ip+"\n")
            else:
                ipv6F.write(ip+"\n")


if __name__ == "__main__":
    print("Amazon ips")
    main()
