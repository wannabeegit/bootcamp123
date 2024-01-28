#INTRO TO PYTHON STRINGS

my_str1 = 'I learn python'
my_str2 = "I learn python"

print(my_str1)
#hi there! i'm Andre


print("hi there! I'm Andre")

message ='he said; "Go for it"'

print(type(message))

languages="""I like python
goland
and
solidarity
"""

print(languages)

my_languages='i like python\nwomen\nand\nsolidarity'

print(my_languages)

print('a\tb\tc\td\ne')

# \is a special character in python
# CHALLENGE

my_str3 = "wlo1 Link encap:Ethernet macc b4:6d:83:77:85:f3"

mac = my_str3[len(my_str3)-17:]

print(mac)

mac = my_str3[32:50]

print(mac)

# re stands for regular expression

import re
my_str3 = "wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3"

mac_pattern = r'Hwaddr ([0-9a-fA-F:]+)'

mac_match = re.search(mac_pattern, my_str3)

if mac_match:
    mac = mac_match.group(1)
    print(mac)

else:
    print("MAC address not found")

# solution 2

mac = my_str3[-1:-18:-1]
print(mac)

# Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm
#
# The user will be prompted to enter the value in ft.
#
# Display the value in cm with 2 decimals, formatted using an f-string.






