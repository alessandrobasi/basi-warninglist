'''

127.0.0.0/8
192.168.0.0/16

'''


def cidr_to_ip(ip):
    from ipaddress import IPv4Network
    return [str(ip) for ip in IPv4Network(ip)]

def main(nomefile="ipv4.txt"):
    ipv4 = list()

    with open(nomefile, "r" , encoding="UTF-8") as f:
        for _, ip in enumerate(f):
            ipv4.extend( cidr_to_ip(ip[:-1:]) )
    
    with open(nomefile, "w", encoding="UTF-8") as f:
        for ip in ipv4:
            f.write(ip+"\n")

if __name__ == "__main__":
    main()