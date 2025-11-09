import os
import pandas as pd

with open("ips.txt", "r") as file:
    ip_list = [x.strip() for x in file.readlines()]

results = []

# for ip in ip_list:
#     response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
#     if response == 0:
#         print(f"{ip} is reachable.")
#     else:
#         print(f"{ip} is unreachable.")

for ip in ip_list:
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    status = "Reachable" if response == 0 else "Unreachable"
    results.append({"IP Address": ip, "Status": status})

data_result = pd.DataFrame(results)
# print(data_result)

data_result.to_excel("Report.xlsx", index=False)