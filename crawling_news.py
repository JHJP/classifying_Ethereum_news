from requests_html import HTMLSession
import pandas as pd

url = 'https://news.google.com/rss/search?q=Ethereum%20when%3A1d&hl=en-US&gl=US&ceid=US%3Aen'
s = HTMLSession()
r = s.get(url)

text = []
for title in r.html.find('title'):
    text.append(title.text)

Corpus = pd.DataFrame(text, columns = ['news_title'])
Corpus.to_csv('1109news_headline.csv')
