İP Changer

Bu Python scripti, belirli aralıklarla internet bağlantınızı yeniden başlatarak IP adresinizi otomatik olarak değiştirmenizi sağlar. Kali Linux ve diğer Linux sistemlerinde çalışır. VPN gerekmeden, mevcut ağ bağlantınızı kullanarak çalışır.
Özellikler

    Belirttiğiniz süre aralıklarında IP adresinizi değiştirir.
    Ağ bağlantınızı yönetmek için nmcli kullanır.
    Yeni IP adresinizi terminalde görüntüler.

Gereksinimler

Bu scriptin çalışması için aşağıdaki gereksinimlerin karşılanmış olması gerekir:

    Python 3.6+
    nmcli (NetworkManager CLI)
    curl (IP adresini kontrol etmek için)

Kurulum

    Depoyu Klonlayın:

git clone https://github.com/kullaniciadi/ip-changer.git
cd ip-changer

Bağımlılıkları Kontrol Edin: Gerekli araçların yüklü olduğundan emin olun:

sudo apt update
sudo apt install network-manager curl -y

Scripti Çalıştırın: Python scriptini çalıştırmak için:

    python3 ip_changer.py

Kullanım

    Ağ Bağlantınızı Öğrenin: Script çalışmadan önce aktif ağ bağlantınızı öğrenmelisiniz. Terminalde şu komutu çalıştırarak mevcut bağlantılarınızı listeleyin:

nmcli connection show

Çıktıdaki NAME sütununda bağlantınızın adını bulun. Örneğin:

NAME                UUID                                  TYPE      DEVICE
(Buradaki isimi belirteceksiniz)  (Kimlik numarası)  ethernet  eth0

Scripti Çalıştırın: Script çalıştırıldığında, sizden ağ bağlantı adını ve IP değiştirme süresini (saniye) girmeniz istenecektir:

    Ağ bağlantı adını girin (nmcli listeden kontrol edebilirsiniz): Wired connection 1
    IP değiştirme süresini saniye olarak girin: 30

    Sonuçları İzleyin: Her IP değişiminde, yeni IP adresiniz terminalde görünecektir.

Durdurma

Script çalışırken, Ctrl + C tuş kombinasyonuyla durdurabilirsiniz.
Notlar

    Script yalnızca dinamik IP adresleriyle çalışır. Eğer sabit bir IP kullanıyorsanız, değişiklik olmaz.
    Script çalıştırılmadan önce sistemdeki ağ bağlantısının aktif olduğundan emin olun.
