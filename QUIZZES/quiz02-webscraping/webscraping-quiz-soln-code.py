# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:38:41 2026 @author: ifrommer

webscraping quiz 2 for IS, F'26
Practice by hand-writing web-scraping code
(can use nfl, billboard, or any other simple page with a table on it),
 then testing it out
Write down on your sheet what's most important
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# this page may need a header to allow for scraping
headers = {
    'User-Agent': (
        'MyApp/1.0 (https://example.com; myemail@example.com)'
    )
}
page = requests.get('https://en.wikipedia.org/wiki/List_of_Amtrak_routes',
                    headers=headers)
soup = BeautifulSoup(page.content,'html.parser')
#%%
# 1.
table = soup.find('table')
table

# 2.
rows = table.find_all('tr')
rows

# 3.
# Write Python code to remove the header row from rows.
hdr_row = rows.pop(0)

# 4.  Write code to select the 1st table row (the Acela row) from \texttt{rows}.
row = rows[0]   # given


# 5. Get all cells from \texttt{row}.
items = row.find_all('td')
items


# 6. Get text of those cells, store it in a list
item_text = []
for item in items:
    item_text.append(item.get_text())
print(item_text)

# 7. Get links from that row, put them in a list of strings
# 1 way
urls = row.find_all('a')
links = []
for url in urls:
    links.append(url['href'])
links

# 8. Put row values in a dictionary
hdrs = ['Name', 'Type', 'Route', 'Numbers', 'Daily round trips', 
        'FY2025 passengers', 'Route miles']  # this is given
row_dict = dict(zip(hdrs,item_text))
row_dict

# 9. Above extracts 1 row, write in words and pseudo-code how you would
# scale this up to scrap all rows, putting each one's content into a dictionary
row_dicts_list = []
for row in rows:
    items = row.find_all('td')
    item_text = []
    for item in items:
        item_text.append(item.get_text())
    row_dict = dict(zip(hdrs,item_text))
    row_dicts_list.append(row_dict)

row_dicts_list

# 10. Turn into a dataframe
df = pd.DataFrame(row_dicts_list)
df


