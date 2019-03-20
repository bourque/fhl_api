"""
"""

import json
import xmltodict

from oauth import SESSION

def get_data(url):
    """
    """

    # Get data from the Yahoo API
    data = SESSION.session.get(url)
    data = data.text

    # Convert the XML to json
    data = xmltodict.parse(data)
    data = json.dumps(data, indent=2)

    return data
