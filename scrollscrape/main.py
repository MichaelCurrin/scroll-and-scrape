"""
Scroll and Scrape main application file.
"""
import time

from selenium import webdriver

import params


browser = webdriver.Chrome()

MAX_STOPS = 3


def scroll(url):
    """
    Scroll through HTML for given url.

    Stop scrolling since height has not increased since last scroll.
    This might also mean that the connection has stopped and the script is
    not aware of the connection error.

    When the end appears to be reached, add in a check to wait a bit and then
    check again a few times, to check we are really at the end. Reset the count
    whenever we have scrolled successfully.
    """
    global browser

    browser.get(url)
    time.sleep(2)

    current_height = browser.execute_script("return document.body.scrollHeight")

    stops = 0
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == current_height:
            stops += 1
            if stops == MAX_STOPS:
                break
            else:
                time.sleep(5)
        else:
            current_height = new_height
            stops = 0


def main():
    """
    Main command-line function.
    """
    scroll(params.url)

    tweets = browser.find_elements_by_class_name('tweet')

    tweet = None
    for tweet in tweets:
        tweet_id = tweet.get_attribute('data-tweet-id')
        print(tweet_id, end=" ")
    print()

    print("Count: {}".format(len(tweets)))
    if tweet:
        tweet_time = tweet.find_element_by_class_name('_timestamp').text
        print("Oldest tweet: {}".format(tweet_time))
    else:
        print("No")

    browser.quit()


if __name__ == '__main__':
    main()
