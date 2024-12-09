import os
import time
import subprocess

def change_ip(network_connection, interval):
    """
    Belirtilen ağ bağlantısını kullanarak IP adresini belirli aralıklarla değiştirir.
    
    Args:
        network_connection (str): Ağ bağlantı adı (Wi-Fi veya Ethernet).
        interval (int): IP değişim süresi (saniye).
    """
    try:
        while True:
            print("[INFO] IP adresi değiştiriliyor...")
            # Ağ bağlantısını kes
            disconnect_command = f'nmcli con down id "{network_connection}"'
            subprocess.run(disconnect_command, shell=True, check=True)
            print("[INFO] Ağ bağlantısı kesildi.")
            
            # Bekleme süresi
            time.sleep(5)
            
            # Ağ bağlantısını yeniden kur
            connect_command = f'nmcli con up id "{network_connection}"'
            subprocess.run(connect_command, shell=True, check=True)
            print("[INFO] Ağ bağlantısı yeniden kuruldu.")
            
            # Yeni IP adresini göster
            print("[INFO] Yeni IP adresi:")
            os.system("curl ifconfig.me")
            print("\n")
            
            # Belirtilen süre kadar bekle
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[INFO] Uygulama durduruldu.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Komut çalıştırılamadı: {e}")

if __name__ == "__main__":
    print("Kali Linux IP Değiştirici")
    network_name = input("Ağ bağlantı adını girin (nmcli listeden kontrol edebilirsiniz): ")
    interval = int(input("IP değiştirme süresini saniye olarak girin: "))
    change_ip(network_name, interval)
