# request lxml and pandas

import pandas as pd
from pytrends.request import TrendReq

# hl => host language tz => timezone
pytrends = TrendReq(hl='en-US', tz=360)

# Build payload
kw_list = ["michelin", "pirelli", "goodyear", "hankook", "bridgestone"]
#timeframes = ["today 5-y", "today 12-m", "today 3-m", "today 1-m"]

# cat='438' => str => Roues et pneus wheels and tires, search for it on the url defaul = 0,
# geo='' => str => countries, default '' => world wilde
# timeframe can be 'today 1-y'

pytrends.build_payload(
    kw_list, cat='438', timeframe='today 5-y', geo='', gprop='')
