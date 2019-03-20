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

from data_containers import get_data

# Example API calls
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/386.l.74973/'
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/386.l.74973/standings/'
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/386.l.74973/scoreboard/'
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/team/386.l.74973.t.1/'

def bombay_wrapper():
    """
    """

    url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/386.l.74973/'
    data = get_data(url)
    print(data)
