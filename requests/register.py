import httpx
import string
import random
import urllib.parse
from solver import public
class Utils:
    @staticmethod
    def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    @staticmethod
    def saveLogs(phpid, uid, pid, username, password):
        with open("data/accounts.txt", "a") as f:
            f.write(f"{phpid}:{uid}:{pid}:{username}:{password}\n")

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


class EmpressClown:
    def __init__(self):
        self.password = "Terminaliscute123$"
        self.threads = 10


    def generate(self):
        with httpx.Client(proxies='http://169.197.82.58:51165') as client:
            cookie = client.get("https://1337x.to/register").cookies["PHPSESSID"]
            captcha_file = Utils.get_captcha(client, cookie)
            headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.7',
    'cache-control': 'max-age=0',
    'connection': 'keep-alive',
    'content-length': '146',
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
            data = f"username={urllib.parse.quote(captcha_file)}&password={urllib.parse.quote('Empressdaskid123$')}&repassword={urllib.parse.quote('Empressdaskid123$')}&email={urllib.parse(f'{captcha_file}@gmail.com')}&country=2&phrase={captcha_string}&register=Register"
            resp = client.post("https://1337x.to/register", headers=headers, data=data)
            print(resp.status_code)
            print(resp.text)
            print(resp.url)

if __name__ == "__main__":
    EmpressClown().generate()
