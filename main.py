import requests
from bs4 import BeautifulSoup
from random import choice



def get_proxy():    # parse html code and get ip-adress
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'lxml')

    tr_tags = soup.find('tbody').find_all('tr')[0:10]

    proxies = []

    for i in tr_tags:    # with tags get ip, port, https  
        td_tags = i.find_all('td')

        ip = td_tags[0].text.strip()
        port = td_tags[1].text.strip()
        http = 'https' if 'yes' in td_tags[6].text.strip() else 'http'    # change yes/no on http/https 
        
        proxy = {'http': http, 'ipaddress': ip + ':' + port}
        proxies.append(proxy)    

    return choice(proxies)    # return random elements 


def get_html(url):    # get html code from web page
    p = get_proxy()
    prox = {p['http']: p['ipaddress']}    # {'http': '103.13.228.180:8888'}

    r = requests.get(url, proxies=prox, timeout=5)
    return r.json()['origin']    # origin is own ip address



def main():
    # url = 'https://free-proxy-list.net/'
    url = 'http://httpbin.org/ip'

    print(get_html(url))



if __name__ == "__main__":
    main()