from colorama import Fore, Style

def menu_goster():
    print(Fore.BLUE + "FAİZ HESAPLAMA UYGULAMAMIZA HOŞGELDİNİZ\n" + Style.RESET_ALL)
    print("İşlemler")
    print("1. Faiz Hesaplama Aracı")
    while True:
        try:
            islemsecmek = int(input("yapmak istediğiniz işlemin numarasını girin: "))
            if islemsecmek == 1:
                print("Faiz Hesaplama Aracına Yönlendiriliyorsunuz!")
                return islemsecmek
            else:
                print("yanlış bir tuşlama yaptınız!")
        except ValueError:
            print("Tekrar Deneyin.")
            






def butce_sor():
    while True:
        try:
            butce = int(input("lutfen butcenizi girin: "))
            onay = input(f"butceniz {butce} TL' dir. Doğruysa 'o' ya basıp onaylayın: ")
            if onay == "o":
                print("butceniz kaydedildi!")
                return butce
            else:
                cikis = input("butce girisiniz kaydedilemedi, cikmak istiyorsanız 'q' ya basın, istemiyorsanız 'r' ye basın: ")
                if cikis == "q":
                    print("Çıktınız.")
                    exit()
        except ValueError:
            print("Lütfen sadece sayı girin!")

def faiz_orani_sor():
    while True:
        try:
            faiz_orani = int(input("Lütfen faiz oranını yüzde işareti kullanmadan giriniz: "))
            devammi = input(f"faiz oraniniz %{faiz_orani} olarak kaydedilsin istiyorsanız 'o' istemiyorsanız 'n' yazın:")
            if devammi == "o":
                print(f"faiz oraniniz %{faiz_orani} olarak kaydedilmiştir")
                return faiz_orani
            elif devammi == "n":
                print("uygulamadan çıkılıyor...")
                break
            else:
                print("hatalı tuşlama yaptınız başa döndürülüyorsunuz!")
        except ValueError:
                print("Lütfen % kullanmadan sayı girin!")

def vade_sayisi_sor():
    while True:
        try:
            vade_gun = int(input("Vade gün sayısı girin: "))
            kayit1 = input(f"Vade gün sayınız {vade_gun} olarak kaydedilecektir onaylıyorsanız 'o' ya basın: ")
            if kayit1 == "o":
                print("kayıt edildi.")
                return vade_gun
            else:
                print("yanlış bir girdi girdiniz tekrar deneyin.")
                continue
        except ValueError:
            print("Lütfen bir sayı girin!")
           
def tax_rate_asker():
    while True:
        try:
            taxrate = int(input("Varsa Vergi oranını sayı olarak girin, yoksa 0 yazın."))
            if taxrate > 0:
                print(f"vergi oranınız %{taxrate} olarak kaydedilmiştir.")
                return taxrate
            elif taxrate == 0:
                print("vergi oranı yoktur veyahut dikkate alınmayacaktır!")
                return 0
        except ValueError:
            print("Lütfen bir sayı girin!")

def faiz_hesaplama_araci(butce, faiz_orani, vade_gun, taxrate):

    brut_getiri = (((butce * faiz_orani)/100/365) * vade_gun)
    net_getiri = (((butce * faiz_orani)/100/365) * vade_gun - ((((butce * faiz_orani)/100/365) * vade_gun) * taxrate/100))
    vade_sonu_brut = (butce + (((butce * faiz_orani)/100/365) * vade_gun))
    vade_sonu_net_miktar = (butce + (((butce * faiz_orani)/100/365) * vade_gun - ((((butce * faiz_orani)/100/365) * vade_gun) * taxrate/100)))
    print(Fore.RED + "FAİZ HESAPLAMA İŞLEMİ SONUÇLARI\n" + Style.RESET_ALL)
    print(f"Brüt getiriniz: {brut_getiri:.2f} TL' dir.")
    print(Fore.GREEN + f"Net Getiriniz: {net_getiri:.2f} TL' dir." + Style.RESET_ALL)
    print(f"Vade Sonu Brüt Miktar: {vade_sonu_brut:.2f} TL' dir.")
    print(Fore.GREEN + f"Vade Sonu Net Miktar: {vade_sonu_net_miktar:.2f} TL' dir." + Style.RESET_ALL)



while True:
    islemsecmek = menu_goster()
    butce = butce_sor()
    faiz_orani = faiz_orani_sor()
    vade_gun = vade_sayisi_sor()
    taxrate = tax_rate_asker()
    faiz_hesaplama_araci(butce, faiz_orani, vade_gun, taxrate)
    
    yeniden_hesaplama = input("Tekrar hesaplama yapmak isterseniz 'o' ya, çıkmak için herhangi bir tuşa basabilirsiniz.")
    if yeniden_hesaplama == "o":
        continue
    else:
        print("Hoşcakalın!")
    exit()

    




