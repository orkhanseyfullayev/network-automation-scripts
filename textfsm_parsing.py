import textfsm
import pandas as pd

raw_output = """
Interface    IP-Address     OK? Method Status Protocol
Gig0/0       192.168.1.1    YES manual up     up
Gig0/1       unassigned     YES unset  down   down
"""

with open("textfsm_template.textfsm") as template:
    fsm = textfsm.TextFSM(template)

parsed = fsm.ParseText(raw_output)


# print(fsm.header)
# print(parsed)

df = pd.DataFrame(parsed, columns=fsm.header)
print(df)
