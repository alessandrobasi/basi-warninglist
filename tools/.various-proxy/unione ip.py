
from os import getcwd, listdir

def main():
    
    ipv4 = set()

    file_presenti = ["proxyIP\\"+file for file in listdir(getcwd()+"\\proxyIP") if ( file.startswith("Proxy") & file.endswith(".txt") ) ]

    for file in file_presenti:

        print("file: "+file+" in elaborazione\n")

        with open(file, "r", encoding="UTF-8") as f:

            for _, ip in enumerate(f):
                ipv4.add( ip[:-1:] )
    
    with open("lista.txt", "w", encoding="UTF-8") as f:
        for ip in  ipv4:
            f.write(ip+"\n")
    print("finito")

if __name__ == "__main__":

    main()