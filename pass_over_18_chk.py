# coding: utf-8

import requests
from bs4 import BeautifulSoup
def process_url (url):
    response    = requests.get(url)
    soup        = BeautifulSoup(response.text, 'lxml')
    articles    = soup.find_all('div', 'r-ent')
    links       = soup.find_all('div', 'btn-group btn-group-paging')
    return articles, links
def get_prv_page(links):
    href = links[0].find_all('a')[1].get('href')
    print (href)
    return (href)
def get_content_from_articles(articles, lookingfor):
    for article in articles:
        #print (article)
        meta = article.find('div', 'title').find('a')
        #print (meta)
        if(meta is None):
            continue
        else:
            title = meta.getText().strip()
            if(lookingfor in title):
                print (title)

if __name__ == '__main__':   

    url = 'https://www.ptt.cc/bbs/movie/index.html'
    ctr = 0
    #to pass the age checker
    payload = {
    'from' : '/bbs/Gossiping/index.html',
    'yes' : 'yes'
    }
    rs = requests.session()
    res = rs.post('https://www.ptt.cc/ask/over18', verify=False, data=payload)
    #res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', verify=False)
    #res = rs.get(url, verify=False)
    #print (res.text)

    while (ctr < 5):
        articles, links = process_url(url)
        url = get_prv_page(links)
        get_content_from_articles(articles, '告')
        url = "https://www.ptt.cc"+url
        print ("url: "+url)
        ctr += 1





