

import re
import sys


kullancilar = {'kullanıcı adı': '','sifre':''}    #sisteme kayıt yapan kişinin kullanıcı ve şifresinin tutulacağı sözlük dizisi
hak = {'hak':1}       #en fazla 3 denemesi olması için gerek hak sayacı
def eski_kullanici():      #eğer sistemde kayıtlı bir hesabı varsa çalışacak olan fonksiyon

    kullanici_adi = input("Kullanıcı adı giriniz:") #kullanıcıdan kullanıcı adını istiyoruz
    sifre = input("Şifre giriniz") #kullanıcıdan şifresini istiyoruz
    if(
        kullanici_adi in kullancilar['kullanıcı adı'] and sifre in kullancilar['sifre'] #girdiği kullanıcı adı ve şifresinin kullanıcılar adlı sölzük dizisindeki konntrolünü yapıyoruz
    ):
        print("Sisteme Giriş Başarılı") #eğer kontrol sonucu kullanıcı adı şifre dizide bulunuyorsa sisteme giriş başarılı
    elif(
          hak['hak'] == 3
        ):
            print("Giriş Hakkınız kalmadı")
            sys.exit() #hak sayısı 3'e eşit olduğunda giriş hakı kalmıyor ve program sonlanıyor


    else:
         hak['hak'] += 1
         print("Kalan hak:", 4- hak['hak'])#girdiği her hatalı kullanıcı adı veya şifre de hakkı +1 oluyor ve hak == 3 olana kadar deneme şansı oluyor
         print("Kullanıcı adı veya parola hatalı")
         eski_kullanici() #hatalı giriş yaptığında tekrar kullanıcı adı şifre kısmına yönlendiriyor



def yeni_kullanici(): #eğer sistemde kayıtlı kullanıcı adı ve şifresi yoksa bu fonksiyon çalışıyor

 yeni_kullanici_adi = input("Kullanıcı adı giriniz") #kullanıcıdan kullanıcı adını istiyoruz
 yeni_sifre = input("Şifre giriniz") #kullanıcıdan şifresini istiyoruz

 if(

        yeni_kullanici_adi in kullancilar['kullanıcı adı'] #yeni girdiği kullanıcı adı  sözlükte mevcutmu diye kontrol sağlıyoruz
    ):
        print("Kullanıcı adı sistemde mevcut")
        yeni_kullanici() #eğer sistemde mevcutsa tekrar kullanıcı adı girmesini istiyoruz

 elif(
        yeni_kullanici_adi.isalnum() == False # kullanıcı adı harf ve sayılardan oluşmalı
    ):
        print("Kullanıcı adı sadece harf ve sayılardan oluşmalıdır.")
 elif(
        len(yeni_kullanici_adi)<= 8 #kullanıcı adı en az 8 karakter olmalı
    ):
        print("Kullanıcı adı en az 8 karakter olmalıdır.")

 elif (
            yeni_sifre.isalnum() == False #şifre harf ve sayılardan oluşmalı
    ):
        print("Şifreniz sadece harf ve sayılardan oluşmalıdır.")

 elif (
            len(yeni_sifre) <= 8 #şifre en az 8 karakter olmalı
    ):
        print("Şifreniz en az 8 karakter olmalıdır")


 if not re.search(r"[\d]+", yeni_sifre): #şifrede bir sayı olup olmadığını kontrol ediyoruz
        print("Şifreniz en az bir sayı içermelidir")
        yeni_kullanici()


 if not re.search(r"[A-Z]+", yeni_sifre): #şifrede bir büyük harf  olup olmadığını kontrol ediyoruz
        print("Şifrenizde bir büyük harf bulunmalıdır")
        yeni_kullanici()
 if not re.search(r"[a-z]+", yeni_sifre): #şifrede bir küçük harf  olup olmadığını kontrol ediyoruz
     print("Şifreniz en az bir küçük harf içermeli")
     yeni_kullanici()



 else:
        kullancilar['kullanıcı adı'] += yeni_kullanici_adi #eğer bütün kurallar uygunsa kullanıcı adı sözlükteki kullanıcı adı kısmına ekleniyor
        kullancilar['sifre'] += yeni_sifre #eğer bütün kurallar uygunsa şifre sözlükteki şifre kısmına ekleniyor
        print("Hesabınız Kaydedildi")







