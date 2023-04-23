
from pytube import YouTube

link = input("Lütfen indirmek istediğiniz YouTube videosunun URL'sini girin: ")
yt=YouTube(link)
yr=yt.streams.get_highest_resolution()
print("Videonuz indiriliyor lütfen bekleyiniz...")

wait=1
for i in range(3):
    print("{}/3\n".format(wait))
    wait+=1
yr.download()
print("Video başarılı bir şekilde indirildi")