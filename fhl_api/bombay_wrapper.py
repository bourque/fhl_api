#! /usr/bin/env python

"""Wrapper for generating plots for the Bombay Believers and Achievers
Fantasy Hockey League.

Authors
-------

    - Matthew Bourque

Use
---

    Coming soon!

Dependencies
------------

    - ``yahoo_oauth``

References
----------

    - ``https://developer.yahoo.com/apps/``
    - ``https://developer.yahoo.com/fantasysports/guide/``
"""

from bokeh.plotting import figure, show, save, output_file

from constants import SEASONS
from data_containers import generate_date_list
from data_containers import get_data
from data_containers import get_league_data
from data_containers import get_time_series_stat
from data_containers import stat_categories

# Example API calls
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/386.l.74973/'
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/386.l.74973/standings/'
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/386.l.74973/scoreboard/'
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/team/386.l.74973.t.1/'


def clean_data(data):
    """Return the list of data, replacing dashes with zeros.

    Parameters
    ----------
    data : list or str
        The data to be cleaned

    Returns
    -------
    cleaned_data : list of str
        The data with dashes replaced with zeros
    """

    cleaned_data = []
    for item in data:
        if item == '-':
            cleaned_data.append(item.replace('-', '0'))
        else:
            cleaned_data.append(item)

    return cleaned_data


def bombay_wrapper():
    """The main function of the ``bombay_wrapper`` module.  See module
    docstring for further details.
    """

    # Initialize place to store results
    results_dict = {}
    results_dict['Goals'] = {}

    # Define time range
    dates = generate_date_list(
        SEASONS['2018']['regular_season_begin'],
        SEASONS['2018']['regular_season_end'],
        return_type='datetime')

    # Determine number of teams
    num_teams = int(get_league_data()['num_teams'])

    # Gather stats, place results in results_dict
    for team in range(1, num_teams + 1):

        print('Gathering stats for team {}'.format(team))
        stats = get_time_series_stat(
            'Goals',
            team,
            SEASONS['2018']['regular_season_begin'],
            SEASONS['2018']['regular_season_end'],
            verbose=False)
        stats = clean_data(stats)
        results_dict['Goals'][team] = stats


    # Create plot of results
    p = figure(title='Goals', x_axis_type='datetime')
    p.yaxis.axis_label = 'Goals'
    for team in results_dict['Goals']:
        p.circle(dates, results_dict['Goals'][team], label=team)
    output_file('plots/goals.html')
    show(p)
    save(p)

if __name__ == '__main__':

    bombay_wrapper()
