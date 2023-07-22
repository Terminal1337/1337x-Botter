from colorama import Fore, Back, Style
import threading
import ctypes
import asyncio
import httpx
from playwright.sync_api import sync_playwright
import time
import string
import random
from solver import public
class Utils():
    def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string
    def saveLogs(phpid,uid,pid,username,password):
        with open("data/accounts.txt","a") as f:
            f.write(f"{phpid}:{uid}:{pid}:{username}:{password}\n")
class EmpressClown():
    def __init__(self) -> None:
        self.password = "Terminaliscute123$"
        self.threads = 10
        self.Handler()
    def Handler(self):
        while True:
            threading.Thread(target=self.register).start()
            if threading.active_count() >= self.threads:
                while True:
                    if threading.active_count() < self.threads:
                        break

    def UpdateConsole(self):
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW(f"1337x.to [EMPRESSCLOWN] | Success: {self.success} | Solved: {self.solved} | Failed: {self.failed}")
    def register(self):
        with sync_playwright() as p:
            php_id = uid = pass_ = ""
            temp_name = Utils.generate_random_string(10)
            username = temp_name
            browser_engine = p.chromium.launch(headless=True,devtools=True,proxy={"server": "169.197.82.58:51165"})
            browser = browser_engine.new_context()
            page = browser.new_page()
            page.goto("https://1337x.to/register",wait_until='networkidle',timeout=20000)
            element = page.query_selector('#contact-form > div:nth-child(6) > img')
            element.screenshot(path=f"temp/{temp_name}.png")
            page.query_selector('#contact-form > div:nth-child(4) > input').type(f"{temp_name}@{random.choice(['gmail','yahoo','hotmail'])}.com")
            page.query_selector('#contact-form > div:nth-child(3) > input').type(self.password)
            page.query_selector('#contact-form > div:nth-child(2) > input').type(self.password)
            page.query_selector('#contact-form > div:nth-child(1) > input').type(username)
            page.query_selector('#contact-form > div:nth-child(6) > input').type(public.return_string(f"temp/{temp_name}.png"))
            page.query_selector('#contact-form > div:nth-child(7) > input').click()
            # page.wait_for_load_state('networkidle')
            time.sleep(5)
            if "Captcha is not valid!" in page.content():
                print(f"{Fore.RED}[ERROR] {Fore.RESET}Captcha is not valid! | {temp_name}")
                browser.close()
                return False
            page.goto('https://1337x.to/login',wait_until='networkidle',timeout=20000)
            page.query_selector('#contact-form > div:nth-child(1) > input').type(temp_name)
            page.query_selector('#contact-form > div:nth-child(2) > input').type(self.password)
            page.query_selector('#contact-form > div:nth-child(3) > input').click()
            time.sleep(3)
            # page.wait_for_load_state('networkidle')
            cookies  = page.context.cookies()
            for cookie in cookies:
                if "PHPSESSID" in cookie["name"]:
                    php_id = cookie['value']
                if "uid" in cookie["name"]:
                    uid = cookie['value']
                if "pass" in cookie["name"]:
                    pass_ = cookie['value']
            Utils.saveLogs(php_id,uid,pass_,username,self.password)
            print(f"{Fore.RED}[GENERATED] {Fore.RESET}PHPID: {php_id} UID: {uid} PASS: {pass_} | {username}")

            browser_engine.close()
            


            



if __name__ == "__main__":
    EmpressClown()