 
import re
import requests
import json
import time
import os
from random import randrange

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getIds(test_str):
    ids = list()
    regex = r"data-value=\"(\d+)\""
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for _, match in enumerate(matches, start=1):
        for groupNum in range(1, len(match.groups())+1):
            ids.append(match.group(groupNum))
    ids.sort(key=int)
    return ids

def updateIds():

    driver = webdriver.Firefox(executable_path='C:\\Program Files\\Mozilla Firefox\\geckodriver.exe')
    driver.minimize_window()
    wait = WebDriverWait(driver,4)

    driver.get('https://nordvpn.com/it/servers/tools/')

    lista_stati = wait.until( EC.presence_of_element_located( (By.XPATH, '//*[@id="recommended"]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div' ) ) ) 
    lista_str = lista_stati.get_attribute('innerHTML')
    driver.quit()

    return getIds(lista_str)


dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"

def main():

    ips = set()
    with open(save_path+"all.txt","r",encoding="UTF-8") as f:
        for line in f:
            ips.add(line[:-1])

    ids = updateIds()

    url_ = 'https://nordvpn.com/wp-admin/admin-ajax.php'
    headers = {'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}

    for num in ids:
        attesa = randrange(10,15,1)
        time.sleep(attesa)
        PARAMS = {'action': "servers_recommendations", "filters": '{"country_id": '+ num +'}'}
        r = requests.get(url =url_, params = PARAMS, headers=headers)
        try:
            data = r.json()
        except:
            continue

        for i in range(len(data)):
            ips.add(data[i]["station"])

    with open(save_path+"ipv4CIDR.txt","w", encoding="UTF-8") as ipv4F, open(save_path+"ipv6CIDR.txt","w", encoding="UTF-8") as ipv6F, open(save_path+"all.txt","w", encoding="UTF-8") as allF:
        for ip in ips:
            allF.write(ip+"\n")
            if '.' in ip:
                ipv4F.write(ip+"\n")
            else:
                ipv6F.write(ip+"\n")
    
    return str(len(ips))
        

if __name__ == "__main__":
    print("NordVPN ips")
    main()