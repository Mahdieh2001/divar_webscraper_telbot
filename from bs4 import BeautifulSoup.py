from bs4 import BeautifulSoup
import requests


province = 'azarbaijan-east-province'
rent_or_buy = 'rent'
building_type = 'villa'

def web_scraper(province, rent_or_buy, building_type):
    province_0 = province
    rent_or_buy_0 = rent_or_buy
    building_type_0 = building_type
    html_text = requests.get(f'https://divar.ir/s/{province_0}/{rent_or_buy_0}-{building_type_0}').text
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
    return response        

print (web_scraper(province, rent_or_buy, building_type))
