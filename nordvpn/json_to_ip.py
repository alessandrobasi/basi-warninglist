import json
from os import listdir, getcwd

def main():
    
    file_json = ["json\\"+file for file in listdir(getcwd()+"\\json") if ( file.endswith(".json") ) ]

    ip = set()
    with open("ipnord.txt","r",encoding="UTF-8") as f:
        for line in f:
            ip.add(line[:-1])

    for file_ in file_json:
        with open(file_, "r", encoding="UTF-8") as f:
            data = json.load(f)

        for i in range(len(data)):
            ip.add(data[i]["station"])
    
    with open("ipnord.txt","w",encoding="UTF-8") as f:
        for i in ip:
            f.write(i+"\n")




if __name__ == "__main__":
    main()