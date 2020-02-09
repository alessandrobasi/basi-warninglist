
import os

dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"

def main():
    
    ips = set()

    with open("bad1.txt", "r", encoding="UTF-8") as f:
        for line in f:
            ips.add(line[:-1])
    with open("bad2.txt", "r", encoding="UTF-8") as f:
        for line in f:
            ips.add(line[:-1])
    with open(save_path+"ipv4.txt", "w", encoding="UTF-8") as f:
        for ip in ips:
            f.write(ip+"\n")



if __name__ == "__main__":
    main()