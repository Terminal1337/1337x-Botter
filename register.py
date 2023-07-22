import ctypes
import httpx
import string
import random
import urllib.parse
from colorama import Fore,init
from solver import public
import threading

lock = threading.Lock()
init(convert=True,strip=True)
class Utils:
    @staticmethod
    def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string



    @staticmethod
    def get_captcha(client: httpx.Client, cookie):
        headers = {
            'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.6',
            'connection': 'keep-alive',
            'cookie': f'PHPSESSID={cookie};',
            'host': '1337x.to',
            'referer': 'https://1337x.to/register',
            'sec-fetch-dest': 'image',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        r = client.get("https://1337x.to/captcha.php", headers=headers)
        file_name = Utils.generate_random_string(10)
        with open(f"temp/{file_name}.png", "wb") as f:
            f.write(r.content)
        return file_name

class Logger(object):
    @staticmethod
    def saveLogs(phpid, uid, pid, username, password):
        with open("data/accounts.txt", "a") as f:
            f.write(f"{phpid}:{uid}:{pid}:{username}:{password}\n")
    
    @staticmethod
    def Success(username, password, email):
        with lock:
            print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[GENERATED] |{Fore.RESET}{Fore.LIGHTBLACK_EX}{email}:{password}{Fore.RESET} | [{username}]")
class EmpressClown:
    def __init__(self):
        self.password = "Terminaliscute123$"
        self.threads = int(input("Threads: "))
        self.success = 0
        self.solved = 0
        self.failed = 0

    def UpdateConsole(self):
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW(f"1337x.to [EMPRESSCLOWN] | Success: {self.success} | Solved: {self.solved} | Failed: {self.failed} | Dev : Terminal | Telegram : @rateIimits")
    def Handler(self):
        threading.Thread(target=self.UpdateConsole).start()
        for i in range(self.threads):
            threading.Thread(target=self.generate).start()
    def generate(self):
        with httpx.Client(proxies='http://169.197.82.58:51165') as client:
            try:
                cookie = client.get("https://1337x.to/register").cookies["PHPSESSID"]
                captcha_file = Utils.get_captcha(client, cookie)
                headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.7',
                'cache-control': 'max-age=0',
                'connection': 'keep-alive',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'PHPSESSID={cookie};',
                'host': '1337x.to',
                'origin': 'https://1337x.to',
                'referer': 'https://1337x.to/register',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
                captcha_string = public.return_string(f"temp/{captcha_file}.png")
                self.solved += 1
                email = captcha_file + random.choice(["@gmail.com", "@yahoo.com", "@hotmail.com"])
                data = f"username={urllib.parse.quote(captcha_file)}&password={urllib.parse.quote(self.password)}&repassword={urllib.parse.quote(self.password)}&email={urllib.parse.quote(email)}&country=2&phrase={captcha_string}&register=Register"
                resp = client.post("https://1337x.to/register", headers=headers, data=data)
                if resp.status_code == 200:
                    Logger.Success(captcha_file, self.password, email)
                    self.CookieParser(client, captcha_file)
                    self.success += 1
                    client.close()
                    self.generate()
            except Exception as e:
                 client.close()
                 self.failed += 1
                 with open('data/errors.txt', 'a') as f:
                        f.write(f"{e}\n")
                 self.generate()
    def CookieParser(self,client : httpx.Client,username):
        uid =  pid = ""
        headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'connection': 'keep-alive',
    # 'content-length': '72',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'PHPSESSID=8rmhrlk54eqacsumhpidgdujp5; __cf_bm=tqrxfDcrnghL1vw7iGXvr4UDtIG2INriS0A.RjVtAIg-1689311562-0-AaMXJtu5t4cL/fzOH5cUb2TPwIUJ/Hwz50mjHyDA2Lravmmo27MSz2hqPEnDMKs20g==',
    'host': '1337x.to',
    'origin': 'https://1337x.to',
    'referer': 'https://1337x.to/login',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
        data = f'username={urllib.parse.quote(username)}&password={urllib.parse.quote(self.password)}&submit=Login'
        resp = client.post("https://1337x.to/login", headers=headers, data=data)
        uid = resp.cookies["uid"]
        pid = resp.cookies["pass"]
        Logger.saveLogs("NULL",uid,pid,username,self.password)
       



if __name__ == "__main__":
    EmpressClown().Handler()
