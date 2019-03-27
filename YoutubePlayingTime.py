# 유튜브의 재생목록 화면 URL을 넣어서
# 해당 재생목록 안에 있는 동영상들의 총 재생시간을 구합니다.

from bs4 import BeautifulSoup
import urllib.request as req

url = "원하는 URL 삽입"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

times = soup.select("td.pl-video-time span")
hour = 0
minute = 0
second = 0

for time in times:
    timesegment = time.text.strip().split(":")
    timesegment = list(map(int, timesegment))
    if len(timesegment)==3:
        hour += timesegment[0]
        minute += timesegment[1]
        second += timesegment[2]
    else:
        minute += timesegment[0]
        second += timesegment[1]

minute += (second // 60)
second = second%60

hour += (minute // 60)
minute = minute%60

print(str(hour)+":"+str(minute)+":"+str(second))
