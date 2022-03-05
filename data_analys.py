# request lxml and pandas

import pandas as pd
from pytrends.request import TrendReq

# hl => host language tz => timezone
pytrends = TrendReq(hl='en-US', tz=360)

# Build payload
all_keywords = ["michelin", "pirelli", "goodyear", "hankook", "bridgestone"]

# cat='438' => str => Roues et pneus wheels and tires search for it on the url defaul = 0,
# geo='' => str => tous les pays
# timeframe can be today 1-y

pytrends.build_payload(
    kw_list, cat='438', timeframe='today 5-y', geo='', gprop='')
