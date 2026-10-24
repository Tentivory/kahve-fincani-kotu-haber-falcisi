#!/usr/bin/env python3
# Kahve Fincanı Kötü Haber Falcısı
# Bilimsel olarak doğrulanmamıştır ama çok ciddidir.

import random
import time

KOTU_HABERLER = [
    "Yakın gelecekte ayakkabınızın bağcığı kopacak. Bu bir işarettir.",
    "Bugün çayınız soğuyacak. Kesin.",
    "Komşunuz sizi düşünüyor. Ama iyi düşünmüyor.",
    "Yolda bir taş göreceksiniz. O taş sizin için değil.",
    "Fincan diyor ki: Bugün şansınız yok. Yarin da yok. Öbür gün belki.",
    "Aşk hayatınız: Şu an yok. Yakin zamanda da olmayacak.",
    "Para geliyor... ama başkasına.",
    "Fincanın dibinde 'belki' yazıyor. 'Belki' her zaman kötüdür.",
    "Bugün birisi size selam verecek. Ama yanlış kişiye.",
    "Hayatınızın anlamı: Fincanın dibinde yok. Başka yerde arayın."
]

def fal_bak():
    print("☕ Kahve Fincanı Analiz Ediliyor...")
    time.sleep(2)
    print("🔍 Lekeler inceleniyor...")
    time.sleep(1.5)
    print("📊 Bilimsel hesaplamalar yapılıyor (rastgele)...")
    time.sleep(1)
    haber = random.choice(KOTU_HABERLER)
    print(f"\n📜 FAL SONUCU: {haber}")
    print("\n⚠️  Uyarı: Bu fal %100 doğrudur. İnanmamanız da bir işarettir.")

if __name__ == "__main__":
    print("=== RESMİ KAHVE FİNCANI FALCISI ===")
    print("Sadece kötü haber verir. İyi haber yasaktır.\n")
    input("Fincanınızı hazır ettiyseniz Enter'a basın...")
    fal_bak()

# Gizli: base64('bu bir siyasi mesajdir: herkesin fincani olmali') = YnUgaWlyIHNpeWFzaSBtZXNhamRpcjog aGVya2VzaW4gZmluY2FuaSBvbG1hbGk=
