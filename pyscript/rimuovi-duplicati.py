
def main():
    ipv4 = set()
    with open("proxy.csv", "r", encoding="UTF-8") as f:
        for ip in f:
            ipv4.add(ip)
    
    with open("proxy1.txt", "w", encoding="UTF-8") as f:
        for ip in ipv4:
            f.write(ip)



if __name__ == "__main__":
    main()