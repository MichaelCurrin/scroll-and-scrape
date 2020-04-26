"""
Params module.

Values to use in search. For now this is hardcoded to searches for the MamaCity Improv Festival.
"""
import urllib.parse


# top
# https://twitter.com/search?vertical=default&q=mamacityif&src=typd

# latest
# https://twitter.com/search?f=tweets&vertical=default&q=mamacityif&src=typd

#
# If using #MCIF, remove unnecessary terms.
# -Maldives%20-McifMv%20-LongLivelilj&src=typd

text_query = '("MamaCity Improv" OR #MCIF2016 OR #MCIF2017 OR #MCIF2018 OR MamaCityImprovFest OR MamaCityIF OR mamacityimprovfestival.nutickets.co.za OR mamacityimprovfest.com) -MusicCityIrish -Ireland -Irish -MusicCity -nashville -Keeffe'
# Convert characters to be websafe. In particular spaces and punctuation, but keep brackets.
encoded_query = urllib.parse.quote(text_query, safe="()")

base_url = "https://twitter.com/search?f=tweets&q="
url = "{}{}".format(base_url, encoded_query)
