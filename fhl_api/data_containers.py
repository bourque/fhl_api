"""
"""

import datetime
import json
import os
import xmltodict

from oauth import SESSION


SEASON_BEGIN = datetime.date(2019, 1, 1)
SEASON_END = datetime.date(2019, 1, 30)

def generate_date_list(begin=SEASON_BEGIN, end=SEASON_END):
    """
    """

    date_list = []

    for i in range((end - begin).days + 1):
        date_list.append(begin + datetime.timedelta(i))
    date_list = [str(date) for date in date_list]

    return date_list

def get_data(url):
    """
    """

    full_url = 'https://fantasysports.yahooapis.com/fantasy/v2' + url
    print('Getting data from {}'.format(full_url))

    # Get data from the Yahoo API
    data = SESSION.session.get(full_url)
    data = data.text

    # Convert the XML to json to python dictionary
    data = xmltodict.parse(data)
    data = json.dumps(data, indent=2)
    data = json.loads(data)

    return data['fantasy_content']

def stat_categories():
    """
    """

    url = '/league/386.l.74973/settings'
    data = get_data(url)

    stat_category_data = data['league']['settings']['stat_categories']['stats']['stat']
    stat_categories = {}
    for stat in stat_category_data:
        stat_categories[stat['name']] = stat['stat_id']

    return stat_categories
