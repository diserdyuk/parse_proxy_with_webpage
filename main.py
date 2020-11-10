import requests
from bs4 import BeautifulSoup


def get_html(url):    # get html code from web page
    proxy = {}
    r = requests.get(url)
    return r.text


def get_proxy(html):    # parse html code and get ip-adress
    soup = BeautifulSoup(html, 'lxml')

    tbody = soup.find('tbody').find_all('tr')
    print(tbody)

    # cnt = 0
    # for i in tbody:
    #     td_ip = i.find_all('td')[0].text
    #     cnt += 1
    #     print(cnt, td_ip)



def main():
    url = 'https://free-proxy-list.net/'

    print(get_proxy(get_html(url)))




if __name__ == "__main__":
    main()