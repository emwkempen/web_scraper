from bs4 import BeautifulSoup

with open('Rental Apartments Amsterdam.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('li', class_='search-list__item search-list__item--listing')

    for listing in course_cards:
        listing_name = listing.h2.text
        price = listing.a

        print(listing_name)
        # print(price)