# Scroll and Scrape
> Find and store tweet data from Twitter search results, using Python and Selenium

This is a relatively Python3 simple application, based on existing scripts, which are included in the [research](/research) directory.

The goal is to get all the Twitter tweets for a search result, going back as far as possible. Using the Twitter API is restrictive - it only gives a week worth of data. Note that to keep this application simple, only the tweet ID needs to be stored and none of the tweet or author data. As once you have a tweet ID no matter how old, you can use the Twitter API to get the tweet and author data for it.

So far the main script works okay, but it not getting all known tweets for a particular known so it needs improvement. The format can be improved - for now it is printing to stdout which can be redirected to a text file.

Also, this could be improved for efficiency using a headless browser. It could also use a more modern library such as [requests-html](https://github.com/kennethreitz/requests-html).
