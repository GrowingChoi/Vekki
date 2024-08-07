from flask import Flask, request, Response
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/get_headlines', methods=['GET'])
def get_headlines():
    url = 'https://news.naver.com'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    headlines = soup.select(".hdline_article_tit")
    headlines_text = [h.get_text(strip=True) for h in headlines]
    return Response("\n".join(headlines_text), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8010)

