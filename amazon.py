# -*- coding: utf-8 -*-
# kozmonot20 - Professional Amazon Hardcore Survival Core v4.6 (Premium Edition)
import time, random, sys

def telemetri_yaz(metin):
    for harf in metin:
        sys.stdout.write(harf); sys.stdout.flush(); time.sleep(0.002)
    print()

class MegaAmazonSimulasyonu:
    def __init__(self):
        self.saglik, self.enerji, self.zehirlenme, self.parazit_yuku, self.gun = 100, 90, 0, 0, 1
        self.aku_voltaj, self.yakit_ron, self.yakit_tortu, self.telsiz_sarj_suresi = 4.2, 0, 0.0, 0
        self.diyot_takili, self.gazojen_aktif, self.siber_yengeç_aktif = False, False, False
        self.hava_durumu = "Açık ve Güneşli"
        
    def durum_raporu(self):
        self.hava_durumu = random.choice(["⛈️ Şiddetli Fırtına", "🔥 Aşırı Termal Sıcaklık", "🌫️ Yoğun Nem", "☀️ Net Hava"])
        print(f"\n🌍 HAVA: {self.hava_durumu} | 📊 GÜN {self.gun} | ❤️ SglK: %{self.saglik} | ⚡ Enrj: %{self.enerji} | 🤢 Zhr: %{self.zehirlenme}")
        print(f"🔋 Voltaj: {self.aku_voltaj:.1f}V/12V | 🔌 Diyot: {self.diyot_takili} | ⛽ Yakıt: {self.yakit_ron} RON (%{self.yakit_tortu*10:.1f} Tortu)")
        if self.siber_yengeç_aktif: print("🦀 UYARI: Siber-Yengeç şu anda ormanda otonom devriyede!")
        print("-" * 75)

    def ormana_kesif_ve_avlanma(self):
        print("\n🌲 ORMAN KEŞFİ\n1) Yılan avla\n2) Meyve/Kök topla\n3) Balık avla\n4) Yumurta topla\n5) 🦀 Siber-Yengeç'i otonom göreve sal")
        try: secim = int(input(">> (1-5): "))
        except: return
        if secim == 1:
            print("\n🔥 PİŞİRME: 1)Çiğ 2)Orta 3)Kurutulmuş 4)Haşlama 5)Kızartma")
            try: p = int(input(">> (1-5): "))
            except: return
            if p == 1: self.zehirlenme += 50; self.parazit_yuku += 40; self.enerji += 15
            elif p == 2: self.zehirlenme += 20; self.parazit_yuku += 15; self.enerji += 30
            elif p == 3: self.enerji += 45; self.zehirlenme = max(0, self.zehirlenme - 10)
            else: self.enerji += 25; self.parazit_yuku += 5
        elif secim == 2:
            print("\n🍓 BİTKİ: 1)Kırmızı 2)Manyok 3)Eğrelti 4)Orkide 5)Mantar")
            try: m = int(input(">> (1-5): "))
            except: return
            if m == 2: self.enerji += 30; telemetri_yaz("✅ Manyok kökü enerji verdi.")
            elif m in (1, 5): self.zehirlenme += 45; telemetri_yaz("⚠️ Toksin aldınız!")
            else: self.enerji += 15
        elif secim == 3: self.enerji += 25; self.parazit_yuku += 10
        elif secim == 4: self.enerji += 35
        elif secim == 5:
            self.siber_yengeç_aktif = True; self.enerji -= 10
            telemetri_yaz("🦀 ESP32 ve Qwen Nano aktif! Siber-Yengeç kilitleri gevşetip ormana daldı.")
        self.enerji = max(0, self.enerji - 10)

    def biyolojik_ve_tibbi_mudahale(self):
        print("\n🩺 TIBBİ MÜDAHALE\n1) Kendini kustur\n2) Kömür çayı iç\n3) Steril hidrasyon\n4) Ağaç kabuğu çiğne\n5) Parazit hapı yut")
        try: secim = int(input(">> (1-5): "))
        except: return
        if secim == 1: self.zehirlenme = max(0, self.zehirlenme - 60); self.saglik -= 15; telemetri_yaz("🤮 Toksin atıldı, mide bozuldu.")
        elif secim == 2: self.zehirlenme = max(0, self.zehirlenme - 35); self.enerji -= 15; telemetri_yaz("🍵 Kömür zehri bağladı.")
        elif secim == 3: self.saglik = min(100, self.saglik + 10); telemetri_yaz("💧 Su depoları yenilendi.")
        elif secim == 4: self.parazit_yuku = max(0, self.parazit_yuku - 20)
        elif secim == 5: self.parazit_yuku = max(0, self.parazit_yuku - 70); self.zehirlenme += 10

    def yakit_laboratuvarı_ve_kimya(self):
        print("\n🧪 KİMYA & YAKIT\n1) Palmiye distilasyonu [35 RON]\n2) Odun külüyle nötrleme [69 RON]\n3) Kireçle dehidrasyon [75 RON]\n4) Toluen/MMT reaktifi [90 RON]\n5) GAZOSEN (Odun Gazı) kazanı kur")
        try: secim = int(input(">> (1-5): "))
        except: return
        if secim == 5:
            self.gazojen_aktif, self.yakit_ron, self.yakit_tortu, self.enerji = True, 85, 0.0, self.enerji - 40
            telemetri_yaz("🪵 GAZOSEN kuruldu! Tortu riski bitti.")
        else:
            self.gazojen_aktif = False
            self.yakit_ron = {1:35, 2:69, 3:75, 4:90}.get(secim, 35)
            self.yakit_tortu = {1:8.5, 2:4.0, 3:1.5, 4:0.2}.get(secim, 8.5)
            self.enerji -= 20

    def jeneratör_ve_propulsion_ayarları(self):
        if self.yakit_ron == 0 and not self.gazojen_aktif: print("❌ Depo boş! Önce yakıt üret."); return
        print("\n🛠️ MOTOR AYARI\n1) Standart\n2) Spacer Conta\n3) Retard Timing\n4) Geniş Meme (%25)\n5) Tüm kombinasyonlar")
        try: secim = int(input(">> (1-5): "))
        except: return
        sp, rt, zg = secim in (2, 5), secim in (3, 5), secim in (4, 5)
        v_esik = 0 if self.gazojen_aktif else max(0, (105 - self.yakit_ron) - (25 if sp else 0) - (20 if rt else 0) - (15 if zg else 0))
        egt, cht = 600, 180
        if self.hava_durumu == "🔥 Aşırı Termal Sıcaklık": egt += 50; cht += 30
        telemetri_yaz("\n⚡ STATİK TAM GÜÇ TESTİ BAŞLIYOR...")
        for s in range(1, 11):
            egt += random.randint(30, 50) if rt else random.randint(10, 20)
            cht += random.randint(5, 12) if zg else random.randint(25, 45)
            if not self.gazojen_aktif: cht += int(self.yakit_tortu * 3.5)
            print(f"⏱️ T+{s}s | CHT: {cht}°C | EGT: {egt}°C"); time.sleep(0.1)
            if v_esik > 30 and not self.gazojen_aktif: print("\n💥 MOTOR PATLADI! Düşük oktan vuruntusu!"); self.yakit_ron = 0; return
            if egt > 800 or cht > 340: print("\n🔥 TERMAL ERİME! Motor alev aldı!"); self.yakit_ron = 0; return
            if self.yakit_tortu * s > 22 and not self.gazojen_aktif: print("\n🛢️ ZİFT TIKANMASI! Karbüratör kilitlendi."); self.yakit_ron = 0; return
            sarj_verimi = 2.0 if (sp and rt) else 1.2
            self.aku_voltaj = min(12.0, self.aku_voltaj + sarj_verimi)
            if self.aku_voltaj >= 12.0: self.telsiz_sarj_suresi += 1

    def telsiz_istasyonu_ve_kurtulus(self):
        print("\n📡 TELSİZ ÜNİTESİ\n1) Diyot lehimle\n2) 121.5 MHz SOS\n3) 243.0 MHz Askeri\n4) HF Amatör bandı\n5) Telsizi kapat")
        try: secim = int(input(">> (1-5): "))
        except: return
        if secim == 1: self.diyot_takili = True; telemetri_yaz("🔌 Diyot aktif. Ters akım önlendi!")
        elif secim in (2, 3, 4):
            if self.aku_voltaj < 12.0 or self.telsiz_sarj_suresi < 5: print("❌ Voltaj yetersiz!"); return
            telemetri_yaz("\n📡 Sinyal yakalandı! 1)Mandala bas 2)Kapat")
            try: m = int(input(">> (1-2): "))
            except: return
            if m == 1:
                fırtına_bonusu = 35 if self.hava_durumu != "⛈️ Şiddetli Fırtına" else 75
                if random.randint(1, 100) < fırtına_bonusu and not self.diyot_takili:
                    print("\n⚡ [YILDIRIM DÜŞTÜ!] Fırtınada antene yüksek statik şok vurdu!"); self.telsiz_sarj_suresi = 999
                else: telemetri_yaz("✅ BAŞARILI: Çağrı ulaştı. Koordinat alındı!"); self.telsiz_sarj_suresi = 999
        else: telemetri_yaz("🔋 Koruma modu aktif.")

    def ana_dongu(self):
        while self.saglik > 0 and self.telsiz_sarj_suresi < 999:
            self.durum_raporu()
            if self.siber_yengeç_aktif:
                if random.choice([True, False]):
                    self.enerji = min(100, self.enerji + 25); telemetri_yaz("🦀 SİBER-YENGEÇ: Operatör Utku'ya taze yaban mersini getirdi!")
                else: telemetri_yaz("🦀 SİBER-YENGEÇ: Çevrede devriye attı, tehlike yok.")
                self.siber_yengeç_aktif = False
            print("1)🌲Orman | 2)🩺Tıbbi | 3)🧪Kimya | 4)🛠️Motor | 5)📡Telsiz")
            try: ham = int(input(">> Seçim (1-5): "))
            except: continue
            if ham == 1: self.ormana_kesif_ve_avlanma()
            elif ham == 2: self.biyolojik_ve_tibbi_mudahale()
            elif ham == 3: self.yakit_laboratuvarı_ve_kimya()
            elif ham == 4: self.jeneratör_ve_propulsion_ayarları()
            elif ham == 5: self.telsiz_istasyonu_ve_kurtulus()
            self.gun += 1
            if not self.diyot_takili: self.aku_voltaj = max(4.2, self.aku_voltaj - 0.5)
            if self.zehirlenme > 40: self.saglik -= 20; telemetri_yaz("🤢 Zehir can alıyor!")
            if self.parazit_yuku > 50: self.saglik -= 15; telemetri_yaz("🐛 Parazit hasarı!")
            self.saglik = max(0, min(100, self.saglik))
        if self.telsiz_sarj_suresi == 999: print("\n🏆 MİSYON BAŞARILI! Kurtuldun kanka! 73! 📡🦾")
        else: print("\n💀 OPERATÖR KAYIP. Sistem çöktü.")

if __name__ == "__main__":
    sim = MegaAmazonSimulasyonu()
    sim.ana_dongu()
