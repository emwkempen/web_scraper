from bs4 import BeautifulSoup
import requests

# TODO built in criteria
# price_from, price_to, floor_space, bedrooms = criteria
# html_url = 'https://www.pararius.com/apartments/amsterdam/' + price_from\
#            + '-' + price_to + "/" + bedrooms + "/" + floor_space

# proxies = {
#     'http': 'http://192.168.178.30',
#     'https': 'http://192.168.178.30',
# }


def find_listings():
    url = 'https://www.pararius.com/apartments/amsterdam/0-1650/2-rooms/50m2'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36}',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,nl;q=0.7',
        'cookie': '_ga=GA1.2.1891300135.1634888993; OptanonAlertBoxClosed=2021-10-26T13:23:31.140Z; eupubconsent-v2=CPOsA0gPOsA0gAcABBENBzCsAP_AAH_AAChQITNf_X__b3_j-_59f_t0eY1P9_7_v-0zjhfdt-8N2f_X_L8X42M7vF36pq4KuR4Eu3LBIQdlHOHcTUmw6okVrzPsbk2Mr7NKJ7PEmnMbO2dYGH9_n93TuZKY7__8___z__-v_v____f_7-3_3__5_X---_e_V399zLv9____39nN___9v-_wQhAJMNS8gC7MscGTaNKoUQIwrCQ6AUAFFAMLRFYQMrgp2VwEeoIWACE1ATgRAgxBRgwCAAQSAJCIgJADwQCIAiAQAAgBUgIQAEbAILACwMAgAFANCxAigCECQgyOCo5TAgKkWignsrAEoO9jTCEMt8CKBR_RUYCNZogWBkJCwcxwBICXiyQAAAAA.f_gAD_gAAAAA; _gid=GA1.2.1801037369.1635595257; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Oct+30+2021+15%3A49%3A18+GMT%2B0200+(Central+European+Summer+Time)&version=6.24.0&isIABGlobal=false&hosts=&consentId=5c5f779c-f997-415e-8c72-c76c0a941bc1&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CSTACK42%3A1&AwaitingReconsent=false&geolocation=NL%3BNH; _gat_gtag_UA_742557_1=1',
        'dnt': '1',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1'
        }
    html_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    listing = soup.find('li', class_='search-list__item search-list__item--listing')
    if listing is None:
        print('listing is None..?')
        return True
    # status = listing.find('span', class_='listing-status listing-status--new')
    url = 'https://www.pararius.com' + listing.h2.a['href']
    title = listing.find('h2', class_='listing-search-item__title').text.strip()
    address = listing.find('div', class_='listing-search-item__location').text.strip()
    price = listing.find('div', class_='listing-search-item__price')
    if price is not None:
        price = price.text.strip()
    area = listing.find('li', class_='illustrated-features__item illustrated-features__item--surface-area')
    if area is not None:
        area = area.text
    rooms_number = listing.find('li', class_='illustrated-features__item illustrated-features__item--number-of-rooms').text
    interior = listing.find('li', class_='illustrated-features__item illustrated-features__item--interior')
    if interior is not None:
        interior = interior.text
    else:
        interior = 'unknown'
    construction_year = listing.find('li', class_='illustrated-features__item illustrated-features__item--construction-period')
    if construction_year is not None:
        construction_year = construction_year.text
    else:
        construction_year = 'unknown'

    # hyperlink_format = '<a href="{link}">{text}</a>'
    # hyper_title = hyperlink_format.format(link=url, text=title)
    # print(hyper_title)

    subject = f'New Pararius Listing: {title}'

    body = f'{url} \n' \
        f'{title} \n' \
        f'{address} \n' \
        f'{price} \n' \
        f'{area} \n' \
        f'{rooms_number} \n' \
        f'Interior: {interior} \n' \
        f'Construction year: {construction_year} \n\n' \
        # f'Search criteria are:\n' \
        # f''

    message = "From: Emiel Kempen\nSubject: %s\n\n%s""" % (subject, body)

    return message
