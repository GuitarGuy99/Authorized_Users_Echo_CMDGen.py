#!/usr/bin/python3

import os

print("As long as your public key is saved in your local .ssh as 'id_rsa.pub' this will work!")


filepath = os.getenv('HOME') + "/.ssh/id_rsa.pub"
rsa = open(filepath,"r")
user = input("What is the user we have to ssh into?")

if user == 'root':
    print(f"\n \necho '{rsa.read()}' > /{user}/.ssh/authorized_keys")

else:
    print(f"\n \necho '{rsa.read()}' > /home/{user}/.ssh/authorized_keys")
