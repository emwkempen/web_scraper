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
    html_text = requests.get('https://www.pararius.com/apartments/amsterdam/200-1500/2-rooms/50m2').text
    soup = BeautifulSoup(html_text, 'lxml')
    listing = soup.find('li', class_='search-list__item search-list__item--listing')
    if listing is None:
        print('listing is None..?')
        return True
    # status = listing.find('span', class_='listing-status listing-status--new')
    url = 'https://www.pararius.com' + listing.h2.a['href']
    title = listing.find('h2', class_='listing-search-item__title').text.strip()
    address = listing.find('div', class_='listing-search-item__location').text.strip()
    price = listing.find('span', class_='listing-search-item__price')
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
