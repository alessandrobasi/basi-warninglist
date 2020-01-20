
def main():
    
    lista_ip_from_cidr = set()
    lista_proxy = set()

    with open("ipv4list.txt","r",encoding="UTF-8") as f:
        for _,ip in enumerate(f):
            lista_ip_from_cidr.add(ip[:-1:])

    with open("lista.txt","r",encoding="UTF-8") as f:
        for _,ip in enumerate(f):
            lista_proxy.add(ip[:-1:])

    print("IP dal cidr:",len(lista_ip_from_cidr) )
    print("IP proxy   :",len(lista_proxy) )

    in_comune = lista_ip_from_cidr.intersection(lista_proxy)

    print("IP in comune :", len(in_comune) )

    with open("in_comune.txt","w",encoding="UTF-8") as f:
        for ip in in_comune:
            f.write(ip+"\n")


if __name__ == "__main__":
    main()