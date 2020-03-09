 
import requests, os

dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"

def main():

    ip = set()

    with open(save_path+"all.txt","r",encoding="UTF-8") as f:
        for line in f:
            ip.add(line[:-1])

    url_ = 'https://api.protonmail.ch/vpn/logicals'
    headers = {'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}
    r = requests.get(url=url_, headers=headers)
    json_request = r.json()

    for obj in json_request["LogicalServers"]:
        for server in obj["Servers"]:
            ip.add(server["EntryIP"])
            ip.add(server["ExitIP"])

    with open(save_path+"all.txt","w",encoding="UTF-8") as f:
        for i in ip:
            f.write(i+"\n")
    
    return "ip trovati unici: "+str(len(ip))
        

if __name__ == "__main__":
    print(main())