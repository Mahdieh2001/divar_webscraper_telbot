from bs4 import BeautifulSoup
import requests
import time

province = 'azarbaijan-east-province'
rent_or_buy = 'rent'
building_type = 'villa'

html_text = requests.get(f'https://divar.ir/s/{province}/{rent_or_buy}-{building_type}').text
soup = BeautifulSoup(html_text, 'lxml')
ad_list = []

def preprocess(soup):
    ads = soup.find_all('div', class_='post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46')
    for item in ads:
        title = item.find('h2', class_='kt-post-card__title').text
        parent = item.find('div', class_='kt-post-card__description')
        deposit = parent.text.split()[-2]
        rent = parent.next_sibling.text.split()[-2]
        link = 'https://divar.ir' + item.a['href']

        ad = {
            'title': title,
            'deposit': deposit,
            'rent': rent,
            'link': link
        }
        ad_list.append(ad)
    return ad_list


if __name__ == '__main__':
    while True:
        response = preprocess(soup)
        print(response)
        wait_time = 24
        time.sleep(wait_time*3600)
