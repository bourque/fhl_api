#! /usr/bin/env python

"""Wrapper for generating plots for the Bombay Believers and Achievers
Fantasy Hockey League.

Authors
-------

    - Matthew Bourque

Use
---

Dependencies
------------

References
----------

"""

from data_containers import generate_date_list
from data_containers import get_data
from data_containers import stat_categories

# Example API calls
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/386.l.74973/'
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/386.l.74973/standings/'
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/386.l.74973/scoreboard/'
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/team/386.l.74973.t.1/'

def bombay_wrapper():
    """
    """

    stat_category_dict = stat_categories()
    date_list = generate_date_list()

    stats = []
    for date in date_list:
        url = '/team/386.l.74973.t.1/stats;type=date;date={}'.format(date)
        data = get_data(url)
        team_stats = data['team']['team_stats']['stats']['stat']
        for stat in team_stats:
            if stat['stat_id'] == stat_category_dict['Goals']:
                stats.append(stat['value'])

    print(stats)


if __name__ == '__main__':

    bombay_wrapper()
