import requests
from bs4 import BeautifulSoup


def get_html(url):    # get html code from web page
    # proxies = {'https': 'ipaddress:5000'}
    r = requests.get(url)
    return r.text


def get_proxy(html):    # parse html code and get ip-adress
    soup = BeautifulSoup(html, 'lxml')

    tr_tags = soup.find('tbody').find_all('tr')[0:10]

    for i in tr_tags:    # with tags get ip, port, https  
        td_tags = i.find_all('td')

        ip = td_tags[0].text.strip()
        port = td_tags[1].text.strip()
        http = 'https' if 'yes' in td_tags[6].text.strip() else 'http'
        
        proxy = {'ipaddres': ip + ':' + port, 'http': http}
        print(proxy)



def main():
    url = 'https://free-proxy-list.net/'

    get_proxy(get_html(url))




if __name__ == "__main__":
    main()