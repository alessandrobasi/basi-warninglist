'''

127.0.0.1:8080
127.0.0.1:9090

'''

def remove_port(ip):
    return ip.split(sep=":")[0]

def main(nomefile="Proxyliste1.txt"):
        
    ipv4 = list()

    with open(nomefile, "r", encoding="UTF-8") as f:

        for _, ip in enumerate(f):
            ip = ip[:-1:].split(sep=":")[0]

            ipv4.append( ip )

    with open(nomefile, "w", encoding="UTF-8") as f:
        for ip in ipv4:
            f.write(ip+"\n")



if __name__ == "__main__":

    main()