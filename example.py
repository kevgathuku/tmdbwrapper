from __future__ import print_function
from tmdbwrapper import TV

popular = TV.popular()

for number, show in enumerate(popular['results'], start=1):
    print("{num}. {name} - {pop}".format(num=number,
                                         name=show['name'], pop=show['popularity']))
