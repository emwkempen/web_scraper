import time
import pararius_scraper as ps
import email_script as es

# TODO built in criteria
# # Insert search criteria
# price_from = '200'
# price_to = '1500'
# floor_space = '50m2'
# bedrooms = '2-rooms'
#
# criteria = price_from, price_to, floor_space, bedrooms

runs = 0

if __name__ == '__main__':
    while True:
        latest_listing = ps.find_listings()
        if runs == 0:
            print(latest_listing)
        minutes = 1                 # refresh rate
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f'Run {runs}.. Current time: {current_time}, waiting {minutes} minute')
        time.sleep(minutes * 60)
        if ps.find_listings() == latest_listing:
            runs += 1
            continue
        else:
            es.send_email(ps.find_listings().encode('utf-8'))
            runs += 1
