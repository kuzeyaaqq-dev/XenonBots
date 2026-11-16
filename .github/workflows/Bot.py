import urllib.request
import urllib.error

URL = "https://sites.google.com/view/xenonhacks/ana-sayfa"

def siteyi_kontrol_et():
    try:
        req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                print(f"[AKTİF] Siteniz çalışıyor! Durum Kodu: {response.status}")
                return True
    except Exception as e:
        print(f"[ÇÖKTÜ / ERİŞİLEMİYOR] Hata: {e}")
        exit(1)

if __name__ == "__main__":
    siteyi_kontrol_et()


