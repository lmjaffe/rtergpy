#!/usr/bin/env python3
#from rtergpy.run import mergeResults
import pandas as pd
from rtergpy.run import defaults
import glob
Defaults=defaults()


def mergeResults(edirbase,iteration='00',**kwargs):
    """
    Reads all processed event information and returns a master dataframe of summary result information
    """
    import pandas as pd
    files= glob.glob(edirbase +'/[12]???/[12]*/'+iteration+'/pkls/Results*.pkl')
    prior='' 
    for file in files:
        if not prior: # create first time
            df=pd.read_pickle(file)
            prior=1  # no longer first
        else:
            dflocal=pd.read_pickle(file)
            df=df.append(dflocal,ignore_index=True)
    # replace list ttimes wih columsn of individual values
    dfttimes=pd.DataFrame(df['ttimes'].to_list(), columns = ['tacer', 't25', 't75'])
    df.drop('ttimes', axis=1, inplace=True)
    df.insert(16, 'tacer', dfttimes['tacer'],True)
    df.insert(17, 't25', dfttimes['t25'],True)
    df.insert(18, 't75', dfttimes['t75'],True)
    df.sort_values(by=['eventname'],inplace=True,ignore_index=True) 
    return df

CMTS=pd.read_csv('CMTS_NEIC.txt', sep='\s+', comment="#")
# Get the Raspberry Shake results (these are my defaults)
#
runs=mergeResults(edirbase=Defaults.edirbase, iteration='00')
runs=runs.assign(Mom=CMTS['Mom'])
runs=runs.assign(Mw=CMTS['Mw'])
runs=runs.assign(CMTNAME=CMTS['CMTNAME'])
runs.to_pickle("Combined_Results_RS.pkl")
print(runs)

# Get the BB GSN results (these are Andy's results)
edirbase = '/home/ljaffe7/Rtergpy/rterg_events/BBevents'

run2=mergeResults(edirbase=edirbase,iteration='00')
run2=run2.assign(Mom=CMTS['Mom'])
run2=run2.assign(Mw=CMTS['Mw'])
run2=run2.assign(CMTNAME=CMTS['CMTNAME'])
run2.to_pickle("Combined_Results_BB.pkl")
print(run2)
