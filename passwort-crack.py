#!/usr/bin/python3

# give the following command in the terminal to show you the hash from the users: sudo cat /etc/shadow

# For example in this case: username:$6$bVtoNJr/GHPs7R$i7Ip5frU9wEfPfGhFGE2w6CkdTpL21zQ2zRbZyR51KkFilzOf8prHxhxpiDzuxRhS8/TZyQ04t25hDXOajIl7.

# The algorithmus in this case are: $6$ = SHA512
# The password-salt in this case are: $6$bVtoNJr/GHPs7R$

password_hash = "$6$bVtoNJr/GHPs7R$i7Ip5frU9wEfPfGhFGE2w6CkdTpL21zQ2zRbZyR51KkFilzOf8prHxhxpiDzuxRhS8/TZyQ04t25hDXOajIl7."

import crypt

with open("./password-crack-dictionary.txt") as file:
	for line in file:
		word = line.strip()
		if crypt.crypt(word, "$6$bVtoNJr/GHPs7R$") == password_hash:
			print(word)
