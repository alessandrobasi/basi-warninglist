
def main():

    ip = set()

    with open("ipv4list.txt", "r", encoding="UTF-8") as f:
        for line in f:
            ip.add(line[:-1])
    with open("lista.txt", "r", encoding="UTF-8") as f:
        for line in f:
            ip.add(line[:-1])
    with open("proxy.csv","r",encoding="UTF-8") as f:
        for line in f:
            ip.add(line[:-1])
    with open("digitalocean.txt","r",encoding="UTF-8") as f:
        for line in f:
            ip.add(line[:-1])
    
    with open("proxy.csv", "w",encoding="UTF-8") as f:
        for line in ip:
            f.write(line+"\n")

if __name__ == "__main__":
    main()