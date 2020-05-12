from requests import get
import os

AS = ["AS57858", "AS25369", "AS3223", "AS62240", "AS205119", "AS49367", "AS174",
      "AS197706", "AS51167", "AS49453", "AS60068", "AS36351", "AS5432", "AS49367"]

dir_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
save_path = "../../lists/"+dir_name+"/"


def main():

    ips = set()

    for asn in AS:
        url = 'https://stat.ripe.net/data/maxmind-geo-lite-announced-by-as/data.json'
        PARAMS = {"resource": asn}

        r = get(url=url, params=PARAMS)
        assert r.status_code == 200, "Network Error"
        file = r.json()

        for obj in file['data']['located_resources']:
            ips.add(obj["resource"])

    with open(save_path+"ipv4CIDR.txt", "w", encoding="UTF-8") as ipv4F, open(save_path+"ipv6CIDR.txt", "w", encoding="UTF-8") as ipv6F, open(save_path+"all.txt", "w", encoding="UTF-8") as allF:
        for ip in ips:
            allF.write(ip+"\n")
            if '.' in ip:
                ipv4F.write(ip+"\n")
            else:
                ipv6F.write(ip+"\n")


if __name__ == "__main__":
    print("Bad AS ips")
    main()
