import os

with open("ips.txt", "r") as file:
    ip_list = [x.strip() for x in file.readlines()]

for ip in ip_list:
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    if response == 0:
        print(f"{ip} is reachable.")
    else:
        print(f"{ip} is unreachable.")