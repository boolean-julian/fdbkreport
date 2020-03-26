#!/usr/bin/env python
# coding: utf-8

# In[3]:


#get_ipython().system(' pip install -U seaborn')
#get_ipython().system(' pip install researchpy')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns
import researchpy as rp
from scipy import stats

## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('font',**{'family':'serif'})
plt.rcParams.update({'font.size': 14})


#sns.set()
print("seaborn version: ", sns.__version__)
# read in all video eval files
df = pd.read_csv("videos_clean.csv")

# put all in one df and keep the order
df.head(5)


# In[4]:


print('shape', df.shape)


# In[5]:


## prior experience
#print(df.priorExp.mean())
#sns.barplot(y='priorExp', x='lvl', data=df, ci=None)
#plt.title('DUMMY: Percentage of prior Experience')
#plt.grid('on')
#plt.savefig('plot_prior.pdf')
# 
#


# In[6]:


#print('***** Comparison of timings of different implementation level *****')
#
#tasks_time_features = ['t1_time', 't2_time', 't3_time', 'm1_time', 'm2_time', 'm3_time']
#
#sns.barplot(y='t2_time', x='lvl', data=df, ci="sd")
#plt.title('DUMMY: timings for task: t2')
#plt.grid('on')
#plt.savefig('plot_time_barplot.pdf')
# 
#
#for t in tasks_time_features:
#    #print('*****  ', t, '  *****')
#    print(df.loc[:,['lvl',t]].groupby('lvl').mean())
#    df.loc[:,['lvl',t]].groupby('lvl').mean().plot(kind='bar')
#    plt.title(['timings for task: ', t])
#     
#
#    
#print('***** Comparison of total time *****')
#
#df.loc[:,"tot_time"] = df.loc[:,"t1_time"] + df.loc[:,"t2_time"] + df.loc[:,"t3_time"] + df.loc[:,"m1_time"] + df.loc[:,"m2_time"] + df.loc[:,"m3_time"]
#df_tot = df.loc[:,['lvl', 'tot_time']]
#df_tot.groupby('lvl').mean().plot(kind='bar')
# 


# In[7]:


#df_t2 = df.loc[:,['lvl', 't2_time', 't2_hint_pt', 't2_hint_ar', 't2_pinch', 't2_tfr', 't2_offscrn']]
#print(df_t2.head(5))


# In[8]:


#print('***** Comparison of number of tfr for tasks t2 *****')
#
## with 0 tfr tries
#
df_t2_tfr = df.loc[:,['lvl','t2_tfr']]
print("complete shape: ", df_t2_tfr.shape)
#
#df_t2_tfr.groupby('lvl').mean().plot(kind='bar')
#plt.title("# of tfr tries in task t2 for different implementations, including 0 tfr")
#plt.grid('on')
# 
#print(df_t2_tfr.groupby('lvl').mean())
#
#
## without 0 tfr tries
#
df_t2_tfr = df_t2_tfr[df_t2_tfr.t2_tfr != 0]
print("shape after dropping 0s: ", df_t2_tfr.shape)
#
#df_t2_tfr.loc[:,['lvl']].plot(kind='hist')
#plt.title('remaining after 0-tfr drop in t1')
# 
#
#
#df_t2_tfr_m=df_t2_tfr#.mean()
##print(df_t2_tfr_m)
##print(list(df_t2_tfr_m))
##df_t2_tfr.groupby('lvl').mean().plot(kind='bar')
#
#sns.barplot(y='t2_tfr', x='lvl', data=df_t2_tfr, ci="sd")
#plt.title("DUMMY: # of tfr tries in task t2 for different implementations")
#plt.grid('on')
#plt.savefig('plot_tfr_barplot.pdf')
# 
#print(df_t2_tfr.groupby('lvl').mean())


# In[10]:
plt0 = plt.figure()

bplot = sns.boxplot(y="t2_tfr", x="lvl", data=df_t2_tfr, whis=1.5)
plt.title("Two-Finger Rotation Attempts")
bplot = sns.stripplot(y=df_t2_tfr["t2_tfr"], x=df_t2_tfr["lvl"], jitter=True, marker='o', alpha=0.3,color='black')
plt.xlabel("case study group")
plt.ylabel("appearances of gesture")
plt.savefig('plot_bplot_tfr.pdf', bbox_inches='tight')


#plt.rcParams.update({'font.size': 14})

bplot = sns.boxplot(y=df["t2_time"], x=df["lvl"], whis=1.5)
plt.title("Time")
bplot = sns.stripplot(y=df["t2_time"], x=df["lvl"], jitter=True, marker='o', alpha=0.3,color='black')
plt.xlabel('case study group')
plt.ylabel('time in seconds')
plt.savefig('plot_bplot_time.pdf', bbox_inches='tight')
 

df["t2_time"].describe()


# 
#     Boxplots:
#     Bottom black horizontal line of plot is minimum value
#     First black horizontal line of rectangle shape is First quartile or 25%
#     Second black horizontal line of rectangle shape is Second quartile or 50% or median.
#     Third black horizontal line of rectangle shape is third quartile or 75%
#     Top black horizontal line of rectangle shape is maximum value.
#     Small diamond shape is outlier data or erroneous data.
#     (min/max values are set by 1.5 times the IQR
# 

# In[11]:


## df with lvl, time and tfr for task 2, with more then 0 tfr tries
##cmap_list = {[Colormap  is not recognized. Possible values are: Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, twilight, twilight_r, twilight_shifted, twilight_shifted_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r]
#
df_t2_corr = df.loc[:,['lvl','t2_tfr','t2_time']][df.t2_tfr != 0]
df.loc[:,'group'] = df.loc[:,'lvl']
##print(df)
#splot = sns.scatterplot(x='t2_tfr', y='t2_time', data=df_t2_corr, hue=df['group'])
##plt.title('DUMMY: Scatterplot of time needed for task t2 dependend on tfr tries')
#plt.grid('on')
#plt.xlabel('two finger rotation attempts')
#plt.ylabel('time needed for the task')
#plt.savefig('plot_scatter.pdf')
##plt.legend(['aaa','bbb','ccc','ddd'])
# 
#


print("Correlation matrix:\n", np.corrcoef(x=df_t2_corr["t2_tfr"], y=df_t2_corr['t2_time']))


# In[12]:


# scatterplot with matplotlib

df_t2_corr = df.loc[:,['lvl','t2_tfr','t2_time']][df.t2_tfr != 0]
df.loc[:,'group'] = df.loc[:,'lvl']
#print(df)

for i in range(4):
    plt.scatter(x=df_t2_corr[df['group']==i]['t2_tfr'], y=df_t2_corr[df['group']==i]['t2_time'], edgecolors='face')#, label='group 0')#, data=df_t2_corr, hue=df['group'])
#plt.title('DUMMY: Scatterplot of time needed for task t2 dependend on tfr tries')
plt.grid('on')
plt.xlabel('two-finger rotation attempts')
plt.ylabel('time needed for the task')
#axes = plt.gca()
#axes.set_xlim([0,33])
#plt.legend(['0','1','2','3'], title='group:', loc="upper right")
#plt.legend(['Gp 0','Gp 1','Gp 2','Gp 3'])#, title='group:', loc="upper right")
plt.legend(['Group 0','Group 1','Group 2','Group 3'])#, title='group:', loc="upper right")
plt.savefig('plot_scatter.pdf', bbox_inches='tight')
 


# In[10]:


# statistics, YEAH!!! -.-



print(rp.summary_cont(df.groupby("lvl")['t2_time']))
print(rp.summary_cont(df.groupby("lvl")['t2_tfr']))

df_0 = df[(df['lvl'] == 0)]
df_0.reset_index(inplace= True)
df_1 = df[(df['lvl'] == 1)]
df_1.reset_index(inplace= True)
df_2 = df[(df['lvl'] == 2)]
df_2.reset_index(inplace= True)
df_3 = df[(df['lvl'] == 3)]
df_3.reset_index(inplace= True)

print('\n\n\n')
# check on homogenious variances
print('levene t2_tfr: ', stats.levene(df_0['t2_tfr'], df_3['t2_tfr']))
print('levene t2_time: ', stats.levene(df_0['t2_time'], df_3['t2_time']))

# check on normality *** 1 ***
print("\n\n##### Implementation 1 ######")
diff_tfr = df_0['t2_tfr'] - df_1['t2_tfr']
stats.probplot(diff_tfr, plot= plt)
plt.title("probability plot for tfr")
 
diff_time = df_0['t2_time'] - df_1['t2_time']
stats.probplot(diff_time, plot= plt)
plt.title("probability plot for times")
 
print('normality tfr diff: ', stats.shapiro(diff_tfr)[1])
print('normality time diff:', stats.shapiro(diff_time)[1])
#print('normality tfr 0: ', stats.shapiro(df_0['t2_tfr']))
#print('normality tfr 3:', stats.shapiro(df_3['t2_tfr']))
#print('normality time 0: ', stats.shapiro(df_0['t2_time']))
#print('normality time 3:', stats.shapiro(df_3['t2_time']))
#print('(2nd value is p-value)')
print('Welch tfr: ', stats.ttest_ind(df_0['t2_tfr'], df_1['t2_tfr'], equal_var = False).pvalue)
print('Welch time:', stats.ttest_ind(df_0['t2_time'], df_1['t2_time'], equal_var = False).pvalue)


# check on normality ***2***
print("\n\n##### Implementation 2 ######")
diff_tfr = df_0['t2_tfr'] - df_2['t2_tfr']
stats.probplot(diff_tfr, plot= plt)
plt.title("probability plot for tfr")
 
diff_time = df_0['t2_time'] - df_2['t2_time']
stats.probplot(diff_time, plot= plt)
plt.title("probability plot for times")
 
print('normality tfr diff: ', stats.shapiro(diff_tfr)[1])
print('normality time diff:', stats.shapiro(diff_time)[1])
#print('normality tfr 0: ', stats.shapiro(df_0['t2_tfr']))
#print('normality tfr 3:', stats.shapiro(df_3['t2_tfr']))
#print('normality time 0: ', stats.shapiro(df_0['t2_time']))
#print('normality time 3:', stats.shapiro(df_3['t2_time']))
#print('(2nd value is p-value)')
print('Welch tfr: ', stats.ttest_ind(df_0['t2_tfr'], df_2['t2_tfr'], equal_var = False).pvalue)
print('Welch time:', stats.ttest_ind(df_0['t2_time'], df_2['t2_time'], equal_var = False).pvalue)


# check on normality ***3***
print("\n\n##### Implementation 3 ######")
diff_tfr = df_0['t2_tfr'] - df_3['t2_tfr']
stats.probplot(diff_tfr, plot= plt)
plt.title("probability plot for tfr")
 
diff_time = df_0['t2_time'] - df_3['t2_time']
stats.probplot(diff_time, plot= plt)
plt.title("probability plot for times")
 
print('normality tfr diff: ', stats.shapiro(diff_tfr)[1])
print('normality time diff:', stats.shapiro(diff_time)[1])
#print('normality tfr 0: ', stats.shapiro(df_0['t2_tfr']))
#print('normality tfr 3:', stats.shapiro(df_3['t2_tfr']))
#print('normality time 0: ', stats.shapiro(df_0['t2_time']))
#print('normality time 3:', stats.shapiro(df_3['t2_time']))
#print('(2nd value is p-value)')
print('Welch tfr: ', stats.ttest_ind(df_0['t2_tfr'], df_3['t2_tfr'], equal_var = False).pvalue)
print('Welch time:', stats.ttest_ind(df_0['t2_time'], df_3['t2_time'], equal_var = False).pvalue)


# In[11]:


#print('relates sus score, t2 time and t2 tfr for all data points')
#sns.pairplot(data=df, vars=['sus', 't2_tfr', 't2_time'], hue='lvl')
# 
#
#print('relates sus score, t2 time and t2 tfr for all non-0 tfr data points')
#sns.pairplot(data=df[df.t2_tfr != 0], vars=['sus', 't2_tfr', 't2_time'], hue='lvl')
# 


# In[12]:


df.loc[:,"tot_pz"] = df.loc[:,"t1_pinch"] + df.loc[:,"t2_pinch"] + df.loc[:,"t3_pinch"] + df.loc[:,"m1_pinch"] + df.loc[:,"m2_pinch"] + df.loc[:,"m3_pinch"]
df.loc[:,"tot_tfr"] = df.loc[:,"t1_tfr"] + df.loc[:,"t2_tfr"] + df.loc[:,"t3_tfr"] + df.loc[:,"m1_tfr"] + df.loc[:,"m2_tfr"] + df.loc[:,"m3_tfr"]
df.loc[:,"tot_offscrn"] = df.loc[:,"t1_offscrn"] + df.loc[:,"t2_offscrn"] + df.loc[:,"t3_offscrn"] + df.loc[:,"m1_offscrn"] + df.loc[:,"m2_offscrn"] + df.loc[:,"m3_offscrn"]


# In[13]:


print(df.loc[:,"tot_tfr"].sum())
print(df.loc[:,"tot_pz"].sum())
print(df.loc[:,"tot_offscrn"].sum())

print(df.loc[:,"t2_tfr"].sum())
print(df.loc[:,"t2_pinch"].sum())
print(df.loc[:,"t2_offscrn"].sum())

print(df.loc[:,"t2_tfr"].sum()/df.loc[:,"tot_tfr"].sum())
print(df.loc[:,"t2_pinch"].sum()/df.loc[:,"tot_pz"].sum())
print(df.loc[:,"t2_offscrn"].sum()/df.loc[:,"tot_offscrn"].sum())

print(df.loc[:,"tot_tfr"].sum()/(df.loc[:,"tot_tfr"].sum()+df.loc[:,"tot_pz"].sum()))

print()

print(df.sum())


# In[14]:


## Values of each group
#bars1 = [df.loc[:,"tot_tfr"].sum(), df.loc[:,"t2_tfr"].sum()]
#bars2 = [df.loc[:,"tot_pz"].sum(), df.loc[:,"t2_pinch"].sum()]
# 
## Heights of bars1 + bars2
#bars = np.add(bars1, bars2).tolist()
# 
## The position of the bars on the x-axis
#r = [0,1]
# 
## Names of group and bar width
#names = ['total','task toaster-2']
##barWidth = 0.8
# 
## Create brown bars
#plt.bar(r, bars1)#, color='#7f6d5f', edgecolor='white')
## Create green bars (middle), on top of the firs ones
#plt.bar(r, bars2, bottom=bars1)#, color='#557f2d', edgecolor='white')
## Create green bars (top)
##plt.bar(r, bars3, bottom=bars, color='#2d7f5e', edgecolor='white', width=barWidth)
# 
## Custom X axis
#plt.xticks(r, names)#, fontweight='bold')
#plt.xlabel("incorrect usages appearences")
#plt.legend(['tfr','pz']) 
## Show graphic
#plt.savefig('plot_tfr_v_pz.pdf')
# 


# In[15]:


## tfr pinch zoom per task
#
#TFR = [df.loc[:,"t1_tfr"].sum(), df.loc[:,"t2_tfr"].sum(), df.loc[:,"t3_tfr"].sum(), df.loc[:,"m1_tfr"].sum(), df.loc[:,"m2_tfr"].sum(), df.loc[:,"m3_tfr"].sum()]
#
#PZ = [df.loc[:,"t1_pinch"].sum(), df.loc[:,"t2_pinch"].sum(), df.loc[:,"t3_pinch"].sum(), df.loc[:,"m1_pinch"].sum(), df.loc[:,"m2_pinch"].sum(), df.loc[:,"m3_pinch"].sum()]
#PZ


# In[16]:


# tfr pinch zoom per task

TFR = [df.loc[:,"t1_tfr"].sum(), df.loc[:,"t2_tfr"].sum(), df.loc[:,"t3_tfr"].sum(), df.loc[:,"m1_tfr"].sum(), df.loc[:,"m2_tfr"].sum(), df.loc[:,"m3_tfr"].sum()]

PZ = [df.loc[:,"t1_pinch"].sum(), df.loc[:,"t2_pinch"].sum(), df.loc[:,"t3_pinch"].sum(), df.loc[:,"m1_pinch"].sum(), df.loc[:,"m2_pinch"].sum(), df.loc[:,"m3_pinch"].sum()]
PZ

plt.bar(height=TFR, x=["t 1","t 2","t 3","m 1","m 2","m 3"])
axes = plt.gca()
axes.set_ylim([0,225])
plt.axvline(x=2.5, linewidth=0.5, color='black')
plt.title("Two-Finger Rotation")
plt.xlabel("task")
plt.ylabel("appearances of gesture")
plt.savefig('plot_tfr.pdf', bbox_inches='tight')
 

plt.bar(height=PZ, x=["t 1","t 2","t 3","m 1","m 2","m 3"], color='orange')
axes = plt.gca()
axes.set_ylim([0,225])
plt.axvline(x=2.5, linewidth=0.5, color='black')
plt.title("Pinch-Zoom")
plt.xlabel("task")
plt.ylabel("appearances of gesture")
plt.savefig('plot_pz.pdf', bbox_inches='tight')
 


# In[17]:


#df[(df['lvl'] == 3)]
#df['tot_offscrn'] = df['t1_offscrn'] + df['t2_offscrn'] + df['t3_offscrn'] + df['m1_offscrn'] + df['m2_offscrn'] + df['m3_offscrn']
#df[(df['tot_offscrn'] != 0)]


# In[ ]:



