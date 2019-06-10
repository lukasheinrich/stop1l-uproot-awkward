import plotconfig
import glob
import os
import uproot
import uproot_methods
import numpy as np
import awkward.array.table
import json

config = plotconfig.get_plot_config('../exported/')

def process_entry(selection,observable, sample, is_MC = True):
    samplename = os.path.basename(sample.path)
    files = glob.glob(os.path.join(sample.path,'*.root*'))

    all_counts = None

    treepath = samplename + '_Nom' if is_MC else samplename


    for chunk in uproot.iterate(
        files,
        branches = [
            'jet_pt','jet_eta','jet_phi','jet_e',
            'weight','xs_weight',
            'n_*'
        ],
        treepath = treepath
    ):
        table = awkward.array.table.Table(chunk)
        oldlen = len(table)

        table = table[selection(table)]

        obs = observable(table)

        if is_MC:
            weights = table['weight'] * table['xs_weight'] * sample.lumi
        else:
            weights = np.ones_like(obs)

        counts, edges = np.histogram(obs, bins = observable.binning, weights = weights)
        all_counts = all_counts + counts if all_counts is not None else counts

    return all_counts.tolist(), edges.tolist()

def process_plot(selection,observable,cfg):
    stack = cfg['stack']
    data = cfg['data']

    stack_counts = []
    for s in stack:
        counts, edges = process_entry(selection,observable, s)
        stack_counts.append(
            {'label': s.label, 'counts': counts, 'edges': edges, 'color': s.color}
        )

    data_counts = []
    for s in data:
        counts, edges = process_entry(selection,observable, s, is_MC=False)
        data_counts.append(
            {'label': s.label, 'counts': counts, 'edges': edges, 'color': s.color}
        )

    return {
        'observed': data_counts,
        'stack': stack_counts
    }

def myselection(table):
    return table['n_mu'] > 0

def myobservable(table):
    jet_events = uproot_methods.classes.TLorentzVector.TLorentzVectorArray.from_ptetaphi(
        table['jet_pt'],
        table['jet_eta'],
        table['jet_phi'],
        table['jet_e']
    )
    theejet_mass = (jet_events[:,0] + jet_events[:,1] + jet_events[:,2]).mass
    return theejet_mass/1000.
myobservable.binning = np.linspace(0,5000,100)

json.dump(process_plot(myselection, myobservable, config),
    open('counts.json','w')
)