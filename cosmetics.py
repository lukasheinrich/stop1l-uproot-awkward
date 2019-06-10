import json
import matplotlib 
matplotlib.use('PS')

import numpy as np
import matplotlib.pyplot as plt


data = json.load(open('counts.json'))


bottom = None
for d in reversed(data['stack']):
    e = np.asarray(d['edges'])
    wdt  = (e[1:]-e[:-1])
    ctrs = e[:-1]+wdt/2.

    counts = np.asarray(d['counts'])
    plt.bar(ctrs,counts,
        width = wdt,
        facecolor = d['color'],
        alpha = 1.0,
        bottom = np.zeros_like(counts) if bottom is None else bottom, 
        label = d['label']
    )

    bottom = counts if bottom is None else bottom + counts

alldata = np.sum([np.asarray(d['counts']) for d in data['observed']], axis=0)

e = np.asarray(data['observed'][0]['edges'])
wdt  = (e[1:]-e[:-1])
ctrs = e[:-1]+wdt/2.

plt.scatter(ctrs,alldata, c = 'k', zorder = 999)

plt.semilogy(True)
plt.legend()
plt.savefig('plot.pdf')
