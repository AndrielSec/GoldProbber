import sys
import requests
from concurrent.futures import ThreadPoolExecutor

BANNER = r"""
   _____       _     _____             _               
  / ____|     | |   |  __ \           | |              
 | |  __  ___ | | __| |__) | __ ___ | |__   ___ _ __ 
 | | |_ |/ _ \| |/ _`  ___/ '__/ _ \| '_ \ / _ \ '__|
 | |__| | (_) | | (_| |   | | | (_) | |_) |  __/ |   
  \_____|\___/|_|\__,_|_|   |_|  \___/|_.__/ \___|_|   
                        [ImhaTeam]
"""

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}

OUTPUT_FILE = "canli_sublar.txt"

def scan(domain):
    domain = domain.strip()
    if not domain: return
    url = domain if domain.startswith(('http://', 'https://')) else f"http://{domain}"
    
    try:
        res = requests.get(url, headers=HEADERS, timeout=3, allow_redirects=False)
        sc = res.status_code
        srv = res.headers.get('Server', 'Bilinmiyor')
        
        if sc == 200:
            log = f"[+] [200 OK] -> {url} [Sunucu: {srv}]"
        elif sc in [301, 302]:
            loc = res.headers.get('Location', '-')
            log = f"[*] [{sc} Yonlendirme] -> {url} => {loc}"
        elif sc in [403, 401]:
            log = f"[-] [{sc} Yasak] -> {url} [Sunucu: {srv}] <-- Bypass denenebilir!"
        else:
            log = f"[-] [{sc}] -> {url} [Sunucu: {srv}]"
            
        print(log)
        with open(OUTPUT_FILE, "a+", encoding="utf-8") as f:
            f.write(log + "\n")
            
    except requests.exceptions.RequestException:
        pass

def main():
    print(BANNER)
    
    if len(sys.argv) < 2:
        print("[!] Kullanım: python3 prober.py <liste.txt> [thread_sayisi]")
        print("[>] Örnek: python3 prober.py subdomains.txt 30")
        sys.exit()
        
    dosya = sys.argv[1]
    threads = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    
    try:
        with open(dosya, 'r') as f:
            targets = f.readlines()
    except FileNotFoundError:
        print(f"[!] Dosya bulunamadı: {dosya}")
        sys.exit()
        
    with open(OUTPUT_FILE, "w") as f: 
        f.write("# Prober - Sonuçlar\n")
        
    print(f"[*] Toplam {len(targets)} subdomain yüklendi.")
    print(f"[*] Hız: {threads} Thread | Çıktı dosyası: {OUTPUT_FILE}")
    print("=" * 60)
    
    with ThreadPoolExecutor(max_workers=threads) as worker:
        worker.map(scan, targets)
        
    print("=" * 60)
    print(f"[+] Tarama bitti. Canlı sublar '{OUTPUT_FILE}' dosyasına kaydedildi.")

if __name__ == "__main__":
    main()
