#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:57:45 2019

@author: catiefinkenbiner
"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
'''
Approximate Baysian Calculation requires:
    1) observation dataset (df_obs)
    2) parameter sets (df_parms)
    3) model output (df_model)
    4) tolerance
    5) number of model runs
'''
#folder = '/Users/catiefinkenbiner/Documents/Summer Institute/CaseStudies/Case Study 0/FallCreekWS/SWMM_24000'
##df_obs = pd.read_csv(folder+'/observation_ts.csv')
#df_parms = pd.read_csv(folder+'/params.csv',header=None)
#df_parms.columns = ['w', 'n_imperv', 'n_perv', 's_imperv', 's_perv', 'k_sat', 'per_routed', 'cmelt', 'Tb', 'A1', 'B1']
##df_model = pd.read_csv(folder+'/simulation_ts.csv')
#df_OFs = pd.read_csv(folder+'/OF_values.csv')

def approx_bayes_calc_OF(parms,OFs,simulations):
    keep_nse = []; keep_pbias = []; keep_rmse = []
    for i in np.arange((simulations)):
        if tolerance_rmse < OFs.iloc[i,3]:
            keep_rmse.append(parms.loc[i])
            
        if np.absolute(OFs.iloc[i,4]) < tolerance_pbias:
            keep_pbias.append(parms.loc[i])
            
        if OFs.iloc[i,5] >= tolerance_nse:
            keep_nse.append(parms.loc[i])        
    return keep_nse,keep_pbias,keep_rmse

def make_histograms(df_parms,bayes_approx,bins,alpha,cc1,cc2,parameters):
    plt.figure(figsize=(12,12))
    for col in np.arange(1,((df_parms.iloc[0,:]).size)):
        plt.subplot(4,3,col)
        ax = df_parms.iloc[:,col].plot.hist(bins=bins,alpha=alpha,color=cc1)    
        ax = bayes_approx.iloc[:,col].plot.hist(bins=bins,alpha=alpha,color=cc2)
        ax.set_xlabel(str(parameters[col]))    
    plt.legend(['Output','ABC'],fancybox=True)
    plt.tight_layout()   

def runABC(df_parms,df_OFs,runs,bins,color1,color2):
    #df_obs = pd.read_csv(df_obs)
    #df_parms = pd.read_csv(df_parms)
    #df_model = pd.read_csv(df_model)
    results_nse,results_pbias,results_rmse = np.array(approx_bayes_calc_OF(df_parms,df_OFs,runs))
    
    bayes_approx_nse = pd.DataFrame(results_nse,columns=None)
    bayes_approx_pbias = pd.DataFrame(results_pbias,columns=None)
    bayes_approx_rmse = pd.DataFrame(results_rmse,columns=None)
    parameters = list(df_parms.columns.values)
    
    print('precent of models with NSE >= to',str(tolerance_nse),'are:',str(len(results_nse)/runs),'%')
    make_histograms(df_parms,bayes_approx_nse,bins,0.5,color1,color2,parameters)
    print('precent of models with',str(-tolerance_pbias),'<= p-bias >=',str(tolerance_pbias),'are:',str(len(results_pbias)/runs),'%')
    make_histograms(df_parms,bayes_approx_pbias,bins,0.5,color1,color3,parameters)
    print('precent of models with RMSE < to',str(tolerance_rmse),'are:',str(len(results_rmse)/runs),'%')
    make_histograms(df_parms,bayes_approx_rmse,bins,0.5,color1,color4,parameters)