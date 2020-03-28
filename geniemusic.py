import requests
from bs4 import BeautifulSoup
from datetime import datetime
## 지니뮤직 순위 / 곡 제목 / 가수 (네이버영화 실습과 동일하게 진행)
# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd='+datetime.today().strftime("%Y%m%d"),headers=headers)


# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
#############################
# (입맛에 맞게 코딩)
soup = BeautifulSoup(data.text, 'html.parser')

length = len(soup.select('div.music-list-wrap > table.list-wrap > tbody > tr.list'))

print("지니뮤직",datetime.today().strftime("%Y")+"년",datetime.today().strftime("%m")+"월", datetime.today().strftime("%d")+"일","실시간 TOP", str(length))

for i in range(0, length):
    title = soup.select('div.music-list-wrap > table.list-wrap > tbody > tr >td.info > a.title.ellipsis')[i].text.strip()
    artist = soup.select('div.music-list-wrap > table.list-wrap > tbody > tr >td.info > a.artist.ellipsis')[i].text
    i += 1
    print(str(i) + ".", artist, "-" , title)
