'''

127.0.0.1\t\t\tqualcosa
127.0.0.2\t\t\tqualcosa


'''

def main(nomefile="full_blacklist_database.txt"):
    
    ipv4 = list()

    with open(nomefile, "r", encoding="UTF-8") as f:

        for _, ip in enumerate(f):
            ip = ip.split(sep="\t\t\t")[0]

            ipv4.append( ip )

    with open(nomefile, "w", encoding="UTF-8") as f:
        for ip in ipv4:
            f.write(ip+"\n")



if __name__ == "__main__":

    main()