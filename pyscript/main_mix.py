'''
Autor: alessandrobasi.it

'''

def cidr_to_ip(ip):
    from ipaddress import IPv4Network
    return [str(ip) for ip in IPv4Network(ip)]

def remove_port(ip):
    return ip.split(sep=":")[0]


def auto_port(nomefile=""):
    ipv4 = list()
    
    with open(nomefile, "r", encoding="UTF-8") as f:
        for _, ip in enumerate(f):
            ip = remove_port(ip[:-1:])
            ipv4.extend( cidr_to_ip(ip) )
    
    with open(nomefile, "w", encoding="UTF-8") as f:
        for ip in ipv4:
            f.write(ip+"\n")


if __name__ == "__main__":

    #auto_port("proxy.txt")

    pass