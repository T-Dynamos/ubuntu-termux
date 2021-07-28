#!/data/data/com.termux/files/usr/bin/python3
#!/usr/bin/python3
import os 
try:
	from colorama import Fore,Back
except ModuleNotFoundError:
	print("colorama is  Not installed")
	os.system("pip3 install colorama")
try:
	import requests, tqdm
except ModuleNotFoundError:
	print("Modules is  Not installed")
	os.system("pip3 install requests tqdm")
os.system('cd $HOME && clear')
from tqdm import tqdm
def download_file_pg(url):
	response = requests.get(url, stream=True)
	filename = (response.url[url.rfind('/')+1:])
	total_size_in_bytes= int(response.headers.get('content-length', 0))
	block_size = 1024 
	progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
	with open('Ubuntu.tar.gz', 'wb') as file:
		for data in response.iter_content(block_size):
			progress_bar.update(len(data))
			file.write(data)
	progress_bar.close()
	if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
			print("ERROR, File size is less tan 10mb")
from colorama import Fore,Back,Style
import platform
usage = """
░█▀▀░█░█░█▀▀░█▀▀░█▀▀░█▀▀░█▀▀
░▀▀█░█░█░█░░░█░░░█▀▀░▀▀█░▀▀█
░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀

🇨​​​​​🇴​​​​​🇲​​​​​🇲​​​​​🇦​​​​​🇳​​​​​🇩​​​​​🇸​​​​​

[1] rsf             (to start Routersploit)
[2] msf             (to start Metasploit-Framework)
[3] mbot            (to start Maths Bot)
[4] hack            (to start  AdvPhishing)
[5] exploit         (to start HiddenEye)
[6] target -t <ip>  (to trace ip location)
[7] target -m       (to trace your ip)
[8] vncserver-start (to start vnc server)
[9] vncserver-stop  (to stop vnc srever)

🇳​​​​​🇴​​​​​🇼​​​​​ 🇼​​​​​🇭​​​​​🇦​​​​​🇹​​​​​ 🇹​​​​​🇴​​​​​ 🇩​​​​​🇴
"""


logo  = """
╔╗─╔╦══╗╔╗─╔╦═╗─╔╦════╦╗─╔╗
║║─║║╔╗║║║─║║║╚╗║║╔╗╔╗║║─║║
║║─║║╚╝╚╣║─║║╔╗╚╝╠╝║║╚╣║─║║ TERMUX
║║─║║╔═╗║║─║║║╚╗║║─║║─║║─║║  
║╚═╝║╚═╝║╚═╝║║─║║║─║║─║╚═╝║ By Ansh Dadwal | T-Dynamos
╚═══╩═══╩═══╩╝─╚═╝─╚╝─╚═══╝
"""
def arch():
	abc = os.path.isdir('/data/data/com.termux/files/usr/bin')
	if abc == True:
		print(Fore.GREEN + "Termux Dedected " + platform.machine())
		os.system('termux-setup-storage')
		print()
	if abc == False:
		print(Fore.RED + "Os is not  supported")
		exit()
	
	if platform.machine() == 'aarch64' :
		print(Fore.GREEN+"Architecture is supported")
		print()
	else:
		print(Fore.RED + "Sorry , Device is not supported ")
		exit()
def heading(h11):
	print(Fore.BLUE+ "["+ Fore.RED + "*" + Fore.BLUE + "]" , Fore.YELLOW + Style.BRIGHT + h11 )
	print(Fore.GREEN)
head = (Fore.BLUE + "["+ Fore.RED + "*" + Fore.BLUE + "]" , Fore.YELLOW + Style.BRIGHT + 'File is To Large [1.3gb] ')
class main():
	def install():
		print(logo)
		arch()
		heading('Checking  the  Downloaded file')
		ab = os.path.isfile('/sdcard/Download/Ubuntu.tar.gz')
		if ab == True:
			print(Fore.GREEN + "File Exists")
			print()
			ins.hel.install2()
		if ab == False:
			print(Fore.RED + "File Does not exist")
			print()
			heading("Downloading File Manually")
			print(Fore.BLUE)
			inu=input('File is too large [1.3gb] Press Enter\n\n =>')
			os.chdir('/sdcard/Download/')
			download_file_pg('https://archive.org/download/Ubuntu.tar/Ubuntu.tar.gz')
			install2()

class ins():
	class hel():
		def install2():
			os.chdir('/data/data/com.termux/files/home')
			
			heading('Installing')
			os.system('apt install proot -y')
			os.system('apt install wget -y ')
			os.system('mkdir -p $HOME/ubuntu20-binds && mkdir -p ubuntu20-fs && cd ubuntu20-fs')
			heading('Extracting Files Please Wait ')
			os.system('proot --link2symlink tar -xf /sdcard/Download/Ubuntu.tar.gz 2> /dev/null')
			print()
			heading('Extarction Successful')
			print()
			heading('Creating Shortcuts ')
			os.system('wget https://raw.githubusercontent.com/T-Dynamos/ubuntu-termux/main/start-ubuntu20.sh  ')
			os.system('cd $PREFIX/bin && rm login && wget https://raw.githubusercontent.com/T-Dynamos/ubuntu-termux/main/login && chmod +x *')
			print("Installation Successful")
			print(Fore.GREEN + usage)
			exit()			
try:
	main.install()
except KeyboardInterrupt:
	print("Exiting Now")
	exit()
except EOFError:
	print("Exiting Now")
	exit()		
