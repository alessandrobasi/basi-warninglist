import os

# https://bgp.he.net/search?search%5Bsearch%5D=digitalocean&commit=Search
dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"

def main():
    
    ips = list()

    with open("digital.txt","r",encoding="UTF-8") as f:
        for line in f:
            ips.append(line.split("\t")[0])
    
    with open(save_path+"ipv4CIDR.txt","w", encoding="UTF-8") as ipv4F, open(save_path+"ipv6CIDR.txt","w", encoding="UTF-8") as ipv6F, open(save_path+"all.txt","w", encoding="UTF-8") as allF:
        for ip in ips:
            allF.write(ip+"\n")
            if '.' in ip:
                ipv4F.write(ip+"\n")
            else:
                ipv6F.write(ip+"\n")


if __name__ == "__main__":
    main()