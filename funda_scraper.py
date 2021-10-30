from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests


def find_listings():
    url = 'https://www.funda.nl/huur/amsterdam/0-1500/50+woonopp/2+kamers/sorteer-datum-af'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,nl;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': 'SNLBCORS=9c34c4a31ddaa4bbe1ce311da2c37432; SNLB=9c34c4a31ddaa4bbe1ce311da2c37432; .ASPXANONYMOUS=dSIBufCq506YXFkwU8XvWjxfswFM1_1JsGz-A9iXqBvIPpNyljBVDMOxSFeKQ0baxGoMENnhIGexgRHed1-sgfuRzvROZ3QEgHO6phgzoiNQ_uVXbToyWFdVPqKu7V-1jb8Ni5sXlZ9IiwDo3DgxLW2w7iU1; html-classes=js; OptanonAlertBoxClosed=2021-10-25T06:31:38.712Z; objectnotfound=objectnotfound=false; optimizelyEndUserId=oeu1635143499583r0.6118276687912725; ajs_anonymous_id=%22f1f21655-1b3e-4b9d-ba31-d0f439e96c33%22; fd-user-checked=true; sessionstarted=true; usbls=1; __RequestVerificationToken=GkG3B2rNMtUjhXoxV00esssuQhmlW5kaCSaxVCZURluYif2EZ9nU6ypdPsHsyAeZtkcwltTC9WLtkI8RruXVjzUvewQ1; lzo=huur=%2fhuur%2famsterdam%2f0-1500%2f50%2bwoonopp%2f2%2bkamers%2f; eupubconsent-v2=CPOnxjXPOnxjXAcABBENBzCgAPLAAAAAAChQILtF7S5dRGPCWG58ZtskOQQPoNSMJgQjABaJImgJwAKAMIQCkmASPATgBAACCAYAKAIBAANkGAAAAQAAQAAAAAGEQAAABAIIICIAgBIBCAAIAAQAAIAQQAAAgEACAEAAkwAAAIIAQEAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH9uAAAA8JAcAAQAAsACoAGQAOAAeABAADIAGgAPAAiABMACeAFUALAAbwBHACXAGGANUAfoBHACUgGKATEAuQBeYDJAgAgAB4AHwAWgB_AGaAQMBHoCVgwAUABYAbwCWgHUAX0GgBgBcgLQAtIC5BAAMABYAbwCWiIAIC5BQDMABoAD4AMAAyACIAFgAMYAfAB-AEwALkAXgBfgDCAMQAbQA8QB_AIIAQoAjgBJgCgAFQAK0AWQAzYBqAGrAOIA5AB5gEcAJNAS0BLoCeAJ6AUgAr8BaAFpALuAYEAxUBnAGdANAAacA4UB-gH7AQIAj0BIICYgE7gKIAU2AswBcgC84F8gX0MAVAAPgAwADIAIgAWAAxAB-AEwAL0AYQBiADbAH8AggBHACTAFAAKgAVoAsgBjwDUANWAcQByADzAI4AS2AngCegFIAK-AXcAxUBnAGdANBAaYBpwDhAH7AQIAj0BIICYgE7gKIAU2AswBeY4AsAAgAB4AFwAPgAtAByAD8ANAAfwBmgEDAIQAREAlsBgAGBAMyAa8BHoCVgExAKmAX0OgUAALAAqABkADgAIIAYgBkADQAHgAPgAiABMACeAFUALAAXAAvgBiADeAI6AS4BMACxAGGAMoAaIA3wB-gEWAI4ASmAtAC0gF1AMUAdQBF4CQQFWALZAXIAvMBkhAB8AAEABAACwAGgAPAAyACIAFgAMQAfwBMAE0AKoAXIAvAC_AGEAYgA0ABtADfAH8AgQBFgCOAEmAKAAVAArYBYgFkAM2AagBqgDfAHEAOQAeYBHACUgE4AJ4AUgArIBX4C0ALSAXcAwABigDMwGcAZ0A0EBpgGnAOEAdSA_QD9gIAAQIAj0BIICYgE7gKIAU2AswBbIC5IF8gX0SgLAAIAAWABkADgAMQAeABEACYAFUALgAXwAxABtAEcANUAjkBaAFpALqAYoA6gCLwF5kgBQAFwAcgBvAF8ANQAloBrwErAL2AX0UgNgALAAqABkADgAIIAYgBkADQAHgARAAmABPACqAFgAL4AYgBYgDKAGiANUAfoBFgCOAEpAReAuQBeYDJCgBMAC4AHwAWgA5AB-AG0AN4AjgBqADXAJaAXUAwABigDXgI9ATEAqYBfQ.flgAAAAAAAAA; sr=0%7cfalse; ak_bmsc=27FB80669B13DBB12B066CC87E6613A8~000000000000000000000000000000~YAAQ3Lk1VGaAwHV8AQAAoFMq0Q3tSIl+2SyQE/ciagBohhVEf8P62uEWysgEPDJZGY8wqsYUsvpI7xOTam5JP2uvWP+izJpti1zDYZ8lzhazxPd+glM/DL1bv5xkQ7H2J/D+rmGK1P0vef7f3j7SHTx/sOVuMj0d5PQI2/jcduB7vQDKc6TRKtgUkVeloQNWQUtFYY0FejOimFPqXrOBcCNgbUJP2fryZbMXWCcyGEI2PIswQQp00HToAJBXiCWDX0g2iMaYqMKQ0d3kUEdv9fXovbIswft75KgY4mMyekVzaXzHUvE1JNH2RIDCMkrKbma1evCj9bEQ5Sg8Wt4yKCQCCVSVkPsFEI58Ntp7AoisBoGfhwJLOdXpOXdnqqBWJLT68roHIjZK78vCeWZ43QJG1rCpXaQJgfzSNefolZ+QoIViPBqGLlvw3wC5l/cWpKRrhbQWvzf+qbaG9YZQ1xlvWw+53BwrHjUE2GBnKI7SQhpmgz16; OptanonConsent=isIABGlobal=false&datestamp=Sat+Oct+30+2021+14%3A26%3A24+GMT%2B0200+(Central+European+Summer+Time)&version=6.22.0&consentId=f00515d6-a1a4-4af7-a953-191a561b2ee7&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CF01%3A1%2CF02%3A1%2CF03%3A1%2CBG30%3A1%2CF04%3A1%2CC0004%3A1%2CF05%3A1%2CBG29%3A1%2CSTACK39%3A1&hosts=H41%3A1%2CH42%3A1%2CH44%3A1%2CH45%3A1%2CH5%3A1%2CH18%3A1%2CH21%3A1%2CH1%3A1%2CH37%3A1%2CH6%3A1%2CH38%3A1%2CH7%3A1%2CH35%3A1%2CH10%3A1%2CH34%3A1%2CH39%3A1%2CH43%3A1%2CH9%3A1%2CH11%3A1%2CH2%3A1%2CH12%3A1%2CH15%3A1%2CH40%3A1%2CH16%3A1%2CH17%3A1&AwaitingReconsent=false&geolocation=NL%3BNH; _gid=GA1.2.1645940635.1635596785; _ga_WLRNSHBY8J=GS1.1.1635596781.11.1.1635596783.0; _ga=GA1.1.1232349944.1634996289; bm_sv=F855A0C3FB1AFD9481C8F7B0E9BFA843~EeP3XC6s6MZ14U+V6B5r+lMswm9raCjKqS+KMy1yUvXpjixx61Mc+JiJBwCaPGKOssNu1RKM6/WnVot41xpgLGEA311OG1iik63azOt3vaOgq7HPNJv6m8Dw2BHMSJ/pZSrYS9l+G/q6tGsN7wOqVQ==; _dd_s=logs=1&id=fcaa9766-de97-4eb2-ad72-8387f884bed0&created=1635596780013&expire=1635597943677',
        'dnt': '1',
        'referer': 'https://www.funda.nl/huur/amsterdam/0-1500/50+woonopp/2+kamers/sorteer-datum-af/',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1'
    }
    html_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    listing = soup.find('ol', class_='search-results')
    if listing is None:
        print('listing is None..?')
        return True
    url = 'http://www.funda.nl' + listing.a['href']
    title = listing.find('h2', class_='search-result__header-title fd-m-none').text.strip()
    address = listing.find('h4', class_='search-result__header-subtitle fd-m-none').text.strip()
    price = listing.find('div', class_='search-result-info search-result-info-price')
    if price is not None:
        price = price.text.strip()
    area = listing.find('ul', class_='search-result-kenmerken').text.strip()

    subject = f'New Funda Listing: {title}'

    body = f'{url} \n' \
           f'{title} \n' \
           f'{address} \n' \
           f'{price} \n' \
           f'{area}  \n\n' \

    message = "From: Emiel Kempen\nSubject: %s\n\n%s""" % (subject, body)

    return message
