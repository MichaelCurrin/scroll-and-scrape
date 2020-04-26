#!python3
"""
Modified sample code from:
    https://medium.com/@dawran6/twitter-scraper-tutorial-with-python-requests-beautifulsoup-and-selenium-part-2-b38d849b07fe

See tutorial on installing the webdriver.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
base_url = "https://twitter.com/search?f=tweets&q="
query = "%40mamacityif"
url = "{}{}".format(base_url, query)


browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name("body")

for _ in range(50):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

tweets = browser.find_elements_by_class_name("tweet-text")
for tweet in tweets:
    print(tweet.text)

# Twitter API data is stored in a tweet tag and not used directly in the
# output for the user.
tweets = browser.find_elements_by_class_name("tweet")

for tweet in tweets:
    t = tweet.find_element_by_class_name("_timestamp")
    id_ = tweet.get_attribute("data-tweet-id")
    path = tweet.get_attribute("data-permalink-path")
    screen_name = tweet.get_attribute("data-screen-name")
    print(t.text, screen_name, id_, path)

    msg = tweet.find_element_by_class_name("TweetTextSize")
    text = msg.text
    print(text)

    print("###################################")

# Quits anyway when script is over but stays open on crashes.
# Consider putting this in finally statement, with debug mode to not exit in case
# you want to check what the browser view contains.
browser.quit()
