"""
Author: Garrett Guevara
Written/Tested: Python 3.5.2
Purpose: Make an API call to the Star Wars API, then create data visualizations with the results.
"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def call_swapi():
    names, heights = [], []
    for i in range(25):
        url = "http://swapi.co/api/people/{}/".format(i)
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            res_dict = res.json()
            names.append(res_dict['name'])
            heights.append(int(res_dict['height']))

    my_style = LS("#333366", base_style=LCS)
    chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
    chart.title = "Star Wars Characters' Heights"
    chart.x_labels = names
    chart.add('', heights)
    chart.render_to_file('sw_heights.svg')

call_swapi()
