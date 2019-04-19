"""
"""

import datetime
import json
import os
import xmltodict

from oauth import SESSION


def generate_date_list(begin, end, return_type='str'):
    """
    """

    # Convert string inputs to datetime
    begin = datetime.datetime.strptime(begin, '%Y-%m-%d')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')

    # Generate date list
    date_list = []
    for i in range((end - begin).days + 1):
        date_list.append(begin + datetime.timedelta(i))

    if return_type == 'datetime':
        pass

    elif return_type == 'str':
        date_list = [str(date) for date in date_list]
        date_list = [date.split()[0] for date in date_list]

    else:
        raise NotImplementedError('Unsupported return_type: {}'.format(return_type))

    return date_list


def get_data(url, verbose=False):
    """
    """

    full_url = 'https://fantasysports.yahooapis.com/fantasy/v2' + url
    if verbose:
        print('Getting data from {}'.format(full_url))

    # Get data from the Yahoo API
    data = SESSION.session.get(full_url)
    data = data.text

    # Convert the XML to json to python dictionary
    data = xmltodict.parse(data)
    data = json.dumps(data, indent=2)
    data = json.loads(data)

    return data['fantasy_content']


def get_league_data():
    """
    """

    url = '/league/386.l.74973/'
    data = get_data(url)

    return data['league']


def get_time_series_stat(category, team, begin, end, verbose=False):
    """Return a dictionary of stats for the given category, team, and
    time period.

    Parameters
    ----------
    category : str
        The stat category of interest (e.g. ``Goals``)
    team : int
        The team identifier (e.g. 1)
    begin : str
        The begin date in ``YYYY-MM-DD`` format (e.g. ``2019-01-01``)
    end : str
        The begin date in ``YYYY-MM-DD`` format (e.g. ``2019-01-31``)
    verbose : bool
        Enable/disable standard output
    """

    # Gather needed data
    stat_category_dict = stat_categories()
    date_list = generate_date_list(begin, end)

    # Get stat over time period
    stats = []
    for date in date_list:
        url = '/team/386.l.74973.t.{}/stats;type=date;date={}'.format(team, date)
        data = get_data(url, verbose)
        team_stats = data['team']['team_stats']['stats']['stat']
        for stat in team_stats:
            if stat['stat_id'] == stat_category_dict[category]:
                stats.append(stat['value'])

    return stats


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
