 
import requests, os

dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"

def main():

    ips = set()

    with open(save_path+"all.txt","r",encoding="UTF-8") as f:
        for line in f:
            ips.add(line[:-1])

    url_ = 'https://api.protonmail.ch/vpn/logicals'
    headers = {'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}
    r = requests.get(url=url_, headers=headers)
    json_request = r.json()

    for obj in json_request["LogicalServers"]:
        for server in obj["Servers"]:
            ips.add(server["EntryIP"])
            ips.add(server["ExitIP"])

    with open(save_path+"ipv4CIDR.txt","w", encoding="UTF-8") as ipv4F, open(save_path+"ipv6CIDR.txt","w", encoding="UTF-8") as ipv6F, open(save_path+"all.txt","w", encoding="UTF-8") as allF:
        for ip in ips:
            allF.write(ip+"\n")
            if '.' in ip:
                ipv4F.write(ip+"\n")
            else:
                ipv6F.write(ip+"\n")
    
    return str(len(ips))
        

if __name__ == "__main__":
    print("ProtonVPN ips")
    main()