import pytube
import os
import subprocess


 #다운받을 동영상 URL 지정

song_ad = str(input("다운로드할 동영상의 주소를 입력해주세요"))
yt = pytube.YouTube(song_ad)

video = yt.streams.all()

#print("출력:",video)

for i in range(len(video)) : #range(6) 0~5
    print(i,',',video[i])


cNum = int(input("다운 받을 화질은?(0~21 입력!)"))
down_dir = "C:/youtube"

video[cNum].download(down_dir)

newFileName = input("변환 할 MP3 파일명은?")
oriFileName = video[cNum].default_filename #원본 동영상 파일

# down_dir,oriFileName -->"C:/youtube/Kim Yeon Ja -  Amor Fati (Original).mp4"
subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
    ])

print("동영상 다운로 및 mp3 변환 완료!")
