class Sample(object):
    def __init__(self, path, label, color, lumi = None, cut = None):
        self.path = path
        self.label = label
        self.color = color
        self.lumi = lumi
        self.cut = cut

S = Sample

lumiByYear = {
    '2015': 3219.56,  # /pb
    '2016': 32988.1,  # /pb
    '2017': 44307.4,  # /pb
    '2018': 58450.1,  # /pb
}

intLumi_2015 = lumiByYear['2015']
intLumi_2016 = lumiByYear['2016']

def get_plot_config(ntupleDir):
    return {
    'stack': [
        S(ntupleDir + 'ttbar_mc16a',
          't#bar{t} 2(e,#mu)',
          "#A5C6E8",
          lumi=intLumi_2015 + intLumi_2016,
          cut="(tt_cat==0 || tt_cat==3 || tt_cat==6 )"),
        S(ntupleDir + 'ttbar_mc16a',
          't#bar{t} 1(e,#mu)',
          "#0F75DB",
          lumi=intLumi_2015 + intLumi_2016,
          cut="(tt_cat==1 || tt_cat==2 || tt_cat==4 || tt_cat==5)"),
        S(ntupleDir + 'ttbar_mc16a',
          't#bar{t} 0(e,#mu)',
          "#003972",
          lumi=intLumi_2015 + intLumi_2016,
          cut="(tt_cat==7 || tt_cat==8 || tt_cat==9 || tt_cat==10)"),
        S(ntupleDir + 'wjets_mc16a',
          'W+jets',
          "#FCDD5D",
          lumi=intLumi_2015 + intLumi_2016),
        S(ntupleDir + 'zjets_mc16a',
          'Z+jets',
          "#FCA420",
          lumi=intLumi_2015 + intLumi_2016),
        S( ntupleDir + 'singletop_mc16a',  'Single top',       "#82DE68", lumi= intLumi_2015 + intLumi_2016  ),
        S( ntupleDir + 'multibosons_mc16a', 'Diboson',          "#3C9E55", lumi= intLumi_2015 + intLumi_2016  ),
        S( ntupleDir + 'ttV_mc16a',        't#bar{t}+V',       "#E67067", lumi= intLumi_2015 + intLumi_2016  ),
        S( ntupleDir + 'dijet_mc16a',        'multijets (MC)',       "#918467", lumi= intLumi_2015 + intLumi_2016  ),
        
    ],
    'overlay': [
    ],
    'systematics': [
    ],
    'data': [
        S(ntupleDir + 'data15', 'data', '#000000'),
        S(ntupleDir + 'data16', 'data', '#000000'),
    ],
    'atlas': "Internal",
    'auto-scale': True,
    'auto-others': False,
    'hide-sf': True,
}
