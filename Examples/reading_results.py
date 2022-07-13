#!/usr/bin/env python
# coding: utf-8

# ## Will test methods to usefully read and compile results from multiple events
# 

# In[1]:


# create a loop to work over all data directories
import os
import pandas as pd
import glob
from numpy import log10

from rtergpy.run import defaults
Defaults=defaults()

edirbase=Defaults.edirbase


# In[25]:


#iterate through all the per-station solutions
#for root, dirs, files in os.walk('/home/ljaffe7/Rtergpy/rterg_events/events/2021/2021011100/00',topdown=True):
df_allwfresults=pd.DataFrame()
df_focmech=pd.DataFrame()

for root, dirs, files in os.walk(edirbase,topdown=True):
    for file in files:
        if file.startswith("Results_") and file.endswith(".pkl"): # only iterate on root that have files like Results_*.pkl
            for root1,dirs1,files1 in os.walk(root,topdown=True): # iterate through all dir (called root) to find specific pkl files
                    for file1 in files1: 
                        if file1.startswith("Etacer_") and file1.endswith(".pkl"):
                            perstationfile=os.path.join(root,file1)
                        elif file1.startswith("Results_") and file1.endswith(".pkl"):
                            resultsfile=os.path.join(root,file1)
                    df_result=pd.read_pickle(resultsfile)            
                    ebbcorrpertacmean=df_result["ebbcorrpertacmean"][0]

                    df_perstation=pd.read_pickle(perstationfile)
                    df_perstation['ebbcorrpertacmean']=ebbcorrpertacmean
                    df_perstation['eventname']=df_result["eventname"][0]
                    df_perstation['elat']=df_result["elat"][0]
                    df_perstation['elon']=df_result["elon"][0]
                    df_perstation['edepth']=df_result["edepth"][0] 
                    df_perstation['strike']=df_result["focmech"][0][0]
                    df_perstation['dip']=df_result["focmech"][0][1]
                    df_perstation['rake']=df_result["focmech"][0][2]
                    
                    df_perstation['ebbcorrpertaclognorm']=log10(df_perstation['ebbcorrpertac']/ebbcorrpertacmean)
                    
                    
                    df_allwfresults=pd.concat([df_allwfresults,df_perstation],ignore_index=True)
                    


# In[26]:


pd.set_option('display.max_columns', None)
df_allwfresults

