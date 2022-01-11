from google_play_scraper import Sort, reviews_all


print('____________________ Starting Scraper')
# App Scraping Alexa - google play
br_reviews = reviews_all(
    'com.amazon.dee.app', 
    lang='pt', 
    sleep_milliseconds=0, 
    country='br', 
    sort=Sort.NEWEST
) 


