"""
Sample script from:
    https://gist.github.com/suriyadeepan/da9d8bd4af44e009db9bae89db395f82
"""
from bs4 import BeautifulSoup
import requests

import time
import sys
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pickle


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("permissions.default.stylesheet", 2)
firefox_profile.set_preference("permissions.default.image", 2)
firefox_profile.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")

driver = webdriver.Firefox(firefox_profile=firefox_profile)

base_url = lambda hashtag: "https://twitter.com/hashtag/{}?src=hash".format(hashtag)


def get_soup(url):
    return BeautifulSoup(requests.get(url).content, "lxml")


# create driver
def crawl_page(url, n):
    # open url
    driver.get(url)

    # Set sticky timeout to implicitly wait for element to be found or
    # command to be complete.
    # To set timeout for calls to execute_async_script see set_script_timeout
    driver.implicitly_wait(15)

    # scroll for n seconds
    for i in range(n):
        elem = driver.find_element_by_tag_name("a")
        elem.send_keys(Keys.END)
        time.sleep(2)
        sys.stderr.write("\n{0}/{1} complete...".format(i + 1, n))
    # gather list items
    list_items = driver.find_elements_by_tag_name("ol")
    # get soup
    soup = BeautifulSoup(list_items[0].get_attribute("innerHTML"), "lxml")
    return soup


def extract_tweet_ids(soup):
    return [
        tag.get("data-item-id")
        for tag in soup.findAll("li")
        if "data-item-type" in tag.attrs and tag.attrs["data-item-type"] == "tweet"
    ]


def save_tweets(hashtags, n, group):
    # hashtag -> list of hashtags
    #  construct urls and gather tweets
    for hashtag in hashtags:
        print(">> Crawling for #{}".format(hashtag))
        # crawl page
        soup = crawl_page(base_url(hashtag), n)
        # get tweet tags
        tweet_ids = extract_tweet_ids(soup)
        print(">> Grabbed {0} tweets from {1}...".format(len(tweet_ids), hashtag))
        # check if group folder exists
        if not os.path.exists("save/" + group):
            os.makedirs("save/" + group)
        # write to file
        with open("save/{0}/{1}.p".format(group, hashtag), "wb") as f:
            pickle.dump(tweet_ids, f)


if __name__ == "__main__":
    """
    hashtags = [ 'Ferguson', 'LoveWins', 'BlackLivesMatter',
            'IndyRef', 'Sandy', 'IceBucketChallenge',
            'BringBackOurGirls', 'PrayForJapan',
            'YesAllWomen', 'GivingTuesday']
    #hashtags = [ 'CharlieHebdo', 'JeSuisCharlie', 'PrayForParis',
    hashtags = [ 'PrayForParis',
            'AskRachel', 'DonaldTrump', 'IStandWithAhmed',
            'WakeUpAmerica', 'Obama', 'SandraBland', 'tcot' ]
    """
    hashtags = [
        "SaferThanATrumpRally",
        "FeelTheBern",
        "NeverTrump",
        "ImWithHer",
        "MakeDonaldDrumpfAgain",
        "StudentLoanDebt",
        "Syria",
        "HillaryEmails",
        "GunControl",
        "StopGunViolence",
        "CampaignZero",
        "Election2016",
        "StopGunViolence",
        "IStandWithPP",
        "ClimateChange",
        "GlobalWarming",
        "StudentLoanForgiveness",
    ]
    save_tweets(hashtags, n=400, group="set3")
    driver.quit()
