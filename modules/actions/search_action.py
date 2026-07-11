"""
Search Action
Project PEGASUS
Author: Sai Ganesh
"""

import webbrowser
import urllib.parse


class SearchAction:

    def execute(self, query):

        query = urllib.parse.quote(query)

        url = f"https://www.google.com/search?q={query}"

        webbrowser.open(url)

        return True