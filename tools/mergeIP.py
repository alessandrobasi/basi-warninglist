import os
from os import getcwd, listdir

dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

path = "../lists/"
dir_presenti = [path+file for file in listdir(path) if "list.txt" not in file]
file_presenti = [cartella+"/"+file for cartella in dir_presenti for file in listdir(cartella) ]

def main():

    ips = set()

    for file in file_presenti:
        with open(file, "r", encoding="UTF-8") as f:
            for line in f:
                ips.add(line[:-1])
    
    with open(path+"list.txt", "w",encoding="UTF-8") as f:
        for ip in ips:
            f.write(ip+"\n")
    

if __name__ == "__main__":
    main()
