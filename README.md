# Scroll and Scrape
> Store tweets from a Twitter search results, using browser scraping

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/scroll-and-scrape?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/scroll-and-scrape/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python->%3D3.6-blue?logo=python&logoColor=white)](https://python.org)
[![dependency - selenium](https://img.shields.io/badge/dependency-selenium-blue)](https://pypi.org/project/selenium)


## Purpose

This application uses Python and the browser (controlled through Selenium) to load a page and scrape the contents and save the data. The approach here loads the DOM (not possible when using plain HTTP request) and also adds in waiting and scrolling logic so that dynamic elements can be pulled in.

This project is aimed at scraping Tweets on a search, where scrolling is needed to load more. It could be used for a user timeline though.


## Requirements

- Python 3
- Chrome


## Installation

Clone the repo.

Install Python 3.

Create a virtual environment and activate it.

Install project packages.

```sh
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
```


## Usage

```sh
$ cd scrollscrape
$ python main.py
```


## Background

This is a simple Python 3 application, based on existing scripts which are included in the [research](/research/) directory. See also [gist](https://gist.github.com/artjomb/07209e859f9bf0206f76).

The goal is to get all the Twitter tweets for a search query, going back as far as possible. 

Using the Twitter API is restrictive - it only gives a week worth of data. Note that to keep this application simple, only the tweet ID needs to be stored and none of the tweet or author data. Since, once you have a tweet ID no matter how old, you can use the Twitter API to get all tweet and author data for a given tweet ID.


## Future development

So far the main script works okay, but it not getting all known tweets for a particular known so it needs improvement. The format can be improved - for now it is printing to stdout which can be redirected to a text file.

Also, this could be improved for efficiency using a headless browser. It could also use a more modern library such as [requests-html](https://github.com/kennethreitz/requests-html).


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
