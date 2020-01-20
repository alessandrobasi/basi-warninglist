
import re
import requests
import json
import time
from random import randrange

def getNewIds():
    with open("html.txt", "r", encoding="UTF-8") as f:
        test_str = f.read()
    ids = list()
    regex = r"data-value=\"(\d+)\""
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for _, match in enumerate(matches, start=1):
        for groupNum in range(1, len(match.groups())+1):
            ids.append(match.group(groupNum))
    return ids


def main():

    ip = set()
    with open("ipnord.txt","r",encoding="UTF-8") as f:
        for line in f:
            ip.add(line[:-1])

    ids = ['2', '10', '13', '14', '21', '27', '30', '33', '38', '43', '52', '54', '56', '57', '58', '68', '73', '74', '80', '81', '84', '97', '98', '99', '100', '101', '104', '105', '106', '108', '119', '126', '131', '140', '142', '153', '156', '128', '163', '174', '175', '179', '192', '195', '196', '197', '200', '114', '202', '208', '209', '211', '214', '220', '225', '226', '227', '228', '234']
    
    #ids = getNewIds()

    url_ = 'https://nordvpn.com/wp-admin/admin-ajax.php'
    headers = {'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}

    for num in ids:
        attesa = randrange(10,60,1)
        print("attesa di",attesa)
        time.sleep(attesa)
        print("scaricando",num)
        PARAMS = {'action': "servers_recommendations", "filters": '{"country_id": '+ num +'}'}
        r = requests.get(url =url_, params = PARAMS, headers=headers)
        data = r.json()

        for i in range(len(data)):
            ip.add(data[i]["station"])


    with open("ipnord.txt","w",encoding="UTF-8") as f:
        for i in ip:
            f.write(i+"\n")
    print("ip trovati unici:",len(ip))
        

if __name__ == "__main__":
    main()