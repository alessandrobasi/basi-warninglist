
import os
from requests.api import get
from shutil import copyfileobj
from zipfile import ZipFile
from os import listdir, remove

dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"

def main():
    ips = set()
    ipv4 = list()
    ipv6 = list()

    url_sfs_30d = "https://www.stopforumspam.com/downloads/listed_ip_30_ipv46.zip"
    
    dowload_name = "sfs-bad-ip.zip"

    # Download
    with get(url_sfs_30d, stream=True) as r:
        with open(dowload_name, 'wb') as f:
            copyfileobj(r.raw, f)

    # unzip
    with ZipFile(dowload_name, 'r') as zipObj:
        lista_nomi_file = zipObj.namelist()[0]
        zipObj.extractall()
    
    # del zip
    remove(dowload_name)

    # load IP file
    with open(save_path+"all.txt","r",encoding="UTF-8") as f:
        for line in f:
            ips.add(line[:-1])
    
    # Add New IP
    with open(lista_nomi_file,"r",encoding="UTF-8") as f:
        for line in f:
            ips.add(line[:-1])

    # Remove new IP list
    remove(lista_nomi_file)

    for ip in ips:
        if '.' in ip:
            ipv4.append(ip)
        else:
            ipv6.append(ip)

    with open(save_path+"ipv4.txt","w", encoding="UTF-8") as f:
        for ip in ipv4:
            f.write(ip+"\n")
    
    with open(save_path+"ipv6.txt","w", encoding="UTF-8") as f:
        for ip in ipv6:
            f.write(ip+"\n")
    
    with open(save_path+"all.txt","w", encoding="UTF-8") as f:
        for ip in ips:
            f.write(ip+"\n")


if __name__ == "__main__":
    main()