from urllib.parse import quote
import ctypes
import httpx
from colorama import Fore,init
from solver import public
import threading
import string
import random
init(convert=True,strip=True)
lock = threading.Lock()
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
            'cookie': cookie,
            'host': '1337x.to',
            'referer': 'https://1337x.to/register',
            'sec-fetch-dest': 'image',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        r = client.get("https://1337x.to/captcha.php", headers=headers)
        php_id = r.cookies.get("PHPSESSID")
        file_name = Utils.generate_random_string(10)
        with open(f"temp/{file_name}.png", "wb") as f:
            f.write(r.content)
        return file_name, php_id

class Logger(object):
    @staticmethod
    def saveLogs(phpid, uid, pid, username, password):
        with open("data/accounts.txt", "a") as f:
            f.write(f"{phpid}:{uid}:{pid}:{username}:{password}\n")
    
    @staticmethod
    def Success(username, password, email):
        with lock:
            print(f"{Fore.RED}INFO : {Fore.RESET}{Fore.CYAN}[COMMENTED] |{Fore.RESET}{Fore.LIGHTBLACK_EX}{email}:{password}{Fore.RESET} | [{username}]")

class Botter(object):
    def __init__(self):
        self.torrent = input("Torrent ID: ")
        self.count = int(input("Count: "))
        self.threads = int(input("Threads: "))
        self.message = input("Message: ")
        self.success = 0
        self.solved = 0
        self.failed = 0
        self.tokens = open("data/accounts.txt", "r").read().splitlines()
        self.Handle()

    def UpdateConsole(self):
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW(f"1337x.to [EMPRESSCLOWN] | Success: {self.success} | Solved: {self.solved} | Failed: {self.failed} | Dev : Terminal | Telegram : @rateIimits")
    def Handle(self):
        threading.Thread(target=self.UpdateConsole).start()
        for token in self.tokens:
            token = token.split(":")
            threading.Thread(target=self.comment, args=(token[1], token[2], self.count)).start()
            if threading.active_count() >= self.threads:
                while True:
                    if threading.active_count() < self.threads:
                        break

    def comment(self, uid, pass_, count: int = 1):
        with httpx.Client(proxies='http://169.197.82.58:51165') as client:
            try:

                cookie = f"uid={uid}; pass={pass_};"
                for i in range(count):
                    captcha_file, phpid = Utils.get_captcha(client, cookie)
                    cookie = f"uid={uid}; pass={pass_}; PHPSESSID={phpid}"
                    captcha = public.return_string(f"temp/{captcha_file}.png")
                    self.solved += 1
                    headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.6',
                'cache-control': 'max-age=0',
                'connection': 'keep-alive',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookie,
                'origin': 'https://1337x.to',
                'referer': 'https://1337x.to/torrent/5722094/Transformers-Rise-of-the-Beasts-2023-720p-WEBRip-800MB-x264-GalaxyRG/',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
            # print(captcha)
                    data = f'comment={quote(self.message)}&torrent={self.torrent}&phrase={captcha}&postcomment=Post+Comment'
                    resp = client.post('https://1337x.to/postcomment', headers=headers, data=data)
                    if resp.status_code == 200:
                        self.success += 1
                        Logger.Success(uid, pass_, captcha)
                    else:
                        self.failed += 1
                    return
            except Exception as e:
                self.failed += 1
                return

            





if __name__ == "__main__":
    Botter()