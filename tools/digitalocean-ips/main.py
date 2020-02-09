import os

dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"

def main():
    
    ips = list()
    ipv4CIDR = list()
    ipv6CIDR = list()

    with open("digital.txt","r",encoding="UTF-8") as f:
        for line in f:
            ips.append(line.split("\t")[0])
    
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