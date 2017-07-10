# ANRProxyGenerator

Tool to generate printout-ready images of entire Android:NetRunner decklists from netrunner.db for the purpose of proxying.

Usage:
`ANRProxyGenerator.py -d <deck id>`

Where deck id is the numeric identifier of the deck on netrunner.db. e.g. for https://netrunnerdb.com/en/deck/view/752593 the deck id is 752593.

Python Library Requirements (both found in pip):
Requests
Pillow
