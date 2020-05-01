import os
from os import getcwd, listdir

dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

path = "../lists/"
dir_presenti = [path+file for file in listdir(path) if "list.txt" not in file]
file_presenti = [
    cartella+"/"+file_name for cartella in dir_presenti for file_name in listdir(cartella) if "ipv4" in file_name]


def getscript():
    path = "./"

    dir_presenti = [path+dir_name
        for dir_name in listdir(path) if os.path.isdir(dir_name) and not dir_name.startswith(".")]
    file_presenti = [
        [cartella, file_name] for cartella in dir_presenti for file_name in listdir(cartella) if "main.py" in file_name]

    return file_presenti


def runscript():

    scripts = getscript()
    for script in scripts:
        #exec(compile(open(script).read(), __file__, "exec"))
        if(os.system("cd "+script[0]+" && python "+script[1]+" && cd ..")):
            print("Error Stopping...")
            break
        
        

    pass

def main():

    runscript()

    ips = set()

    for file in file_presenti:
        with open(file, "r", encoding="UTF-8") as f:
            for line in f:
                ips.add(line[:-1])

    with open(path+"list.txt", "w", encoding="UTF-8") as f:
        for ip in ips:
            f.write(ip+"\n")


if __name__ == "__main__":
    main()
