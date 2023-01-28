

import odev2_soru1_modul
durum =""

def girisekrani(): #başlangıçta kayıtlı hesabı olup olmadığını sormak için bu fonksiyonu kullanıyoruz
 durum = input("Kayıtlı bir hesabınız var mı ? (evet/hayır)")

 if (
                durum == "hayır"
        ):
            print("Yeni Kayıt Ekranı")
            odev2_soru1_modul.yeni_kullanici()     #eğer kullanıcı hayır derse modülden yeni_kullanıcı fonksiyonunu çağırıyoruz
            girisekrani() #kullanıcıyı kayıt yaptıtan sonra tekrar giriş ekranına yönlendiriyoruz

 elif (
                durum == "evet"
        ):
            print("Kayıtlı Kullanıcı")
            odev2_soru1_modul.eski_kullanici() #eğer kullanıcı evet derse modülden eski_kullanıcı fonksiyonunu çağırıyoruz

girisekrani()
