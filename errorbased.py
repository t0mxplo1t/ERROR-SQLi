import requests,os

print("\033[33mInstallation of requests\033[0m")
os.system("pip install requests")
print("\033[33mInstallation complete\033[0m")
os.system("clear")

def banner():
	print("""\033[33m
███████╗██████╗ ██████╗  ██████╗ ██████╗       ███████╗ ██████╗ ██╗     ██╗
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗      ██╔════╝██╔═══██╗██║     ██║
█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝█████╗███████╗██║   ██║██║     ██║
██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗╚════╝╚════██║██║▄▄ ██║██║     ██║
███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║      ███████║╚██████╔╝███████╗██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝      ╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝\033[0m
\033[30;43mSimple Error-Based SQLi Vulnerability Scanner\033[0m\n""")
banner()

try:
	url = input("\033[33mEnter Web with Parameters : \033[0m")
	payload = input("\033[33mEnter payload : \033[0m")
	j = requests.get(url+payload)

	if "MySQL" in j.text:
		print("\n\033[30;43mThe website is Vulnerable to SQL injection!\033[0m")
	else:
		print("\n\033[30;43mWebsite is not Vulnerable!\033[0m")

except KeyboardInterrupt:
	print("\033[33mOops\033[0m")

except EOFError:
	print("\033[33mOkay\033[0m")

