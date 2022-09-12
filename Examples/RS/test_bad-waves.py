#!/usr/bin/env python3

"""
Uses the std output from GT's searchCMT algo to pull and process multiple events.
Andrew Newman Fri Oct 29 13:17:32 EDT 2021

It took 10.25 minutes to process 17 events including pulling data from NEIC (these were done in series)
"""
from rtergpy.run import defaults, event, etime2name, src2ergs
from obspy import UTCDateTime
import pandas as pd

Defaults=defaults()
Event=event()
Defaults.src='RASPISHAKE'
Event.newData=True # True is default
Event.ecount='00'
edateold=""
# events older than available in NEIC
#CMTS=pd.read_csv('CMTS_NEIC.txt', sep='\s+', comment="#")  # any amount of whitespace
CMTS=pd.read_csv('test.txt', sep='\s+', comment="#")  # any amount of whitespace
for index, EQ in CMTS.iterrows():
    print(EQ)
    eloc = [EQ.LAT,EQ.LONG,EQ.DEPTH] 
    year,mo,dd = EQ.DATE.split('/')
    hh,mn,sec = EQ.TIME.split(':')
    if float(sec) >= 60:
        mn = int(mn) + 1
        sec = float(sec) - 60
    if int(mn) >= 60:
        hh = int(hh) + 1
        mn = int(mn) - 60
    etime=(UTCDateTime(int(year),int(mo),int(dd),int(hh),int(mn),float(sec)))
    # iterate ecount
    if EQ.DATE == edateold:
        Event.ecount=str(int(Event.ecount)+1).zfill(2)
    else:
        Event.ecount='00'
    edateold=EQ.DATE
    Event.eventname=etime2name(etime,ecount=Event.ecount)
    Event.origin=[eloc,etime]
    Event.focmech=[EQ.STK, EQ.DP, EQ.RKE] # phi,delta,lmbda

    print("\n\n"+Event.eventname+" ===============================")
    #try:
    src2ergs(Defaults=Defaults,Event=Event)  # need to export run output in a coherent way
    #except:
    #    print("ERROR: running on "+Event.eventname+" failed!!!!\n\n")
