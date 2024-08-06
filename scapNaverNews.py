import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 페이지에서 HTMLㅇㅡㄹ 가져옴
response = requests.get("https://news.naver.com/")

# BeatifulSoup 객체 생성
soup = BeautifulSoup(response.text,'html.parser')

# 뉴스 헤드라인 선택
headlines = soup.select("div.cjs_channel_card div.cjs_journal_wrap._item_contents div.cjs_news_tw div.cjs_t")

for headline in headlines:
    print(headline.text.strip())


