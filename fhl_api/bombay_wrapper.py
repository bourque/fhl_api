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

from data_containers import generate_date_list
from data_containers import get_data
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

    stats = get_time_series_stat('Goals', 1, '2019-01-01', '2019-01-30')
    stats = clean_data(stats)
    print(stats)


if __name__ == '__main__':

    bombay_wrapper()
