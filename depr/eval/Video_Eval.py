# Video Evaluation. Needs "videos_clean.csv" as input.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns
import researchpy as rp
from scipy import stats



# change font to latex font
rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)



# change font sizes for all elements
TICKS_AND_LEGEND_SIZE = 16
AXES_TITLE_SIZE = 22
PLOT_TITLE_SIZE = 22

plt.rc('font', size=TICKS_AND_LEGEND_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=PLOT_TITLE_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=AXES_TITLE_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=TICKS_AND_LEGEND_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=TICKS_AND_LEGEND_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=TICKS_AND_LEGEND_SIZE)    # legend fontsize
plt.rc('figure', titlesize=PLOT_TITLE_SIZE)  # fontsize of the figure title



# read in video csv file
df = pd.read_csv("videos_clean.csv")

# check data
print(df.head(5))
print('shape', df.shape)

print('make: plot_bplot_tfr.pdf')
df_t2_tfr = df.loc[:,['lvl','t2_tfr']]
df_t2_tfr = df_t2_tfr[df_t2_tfr.t2_tfr != 0]
print("shape after dropping 0s for tfr: ", df_t2_tfr.shape[0])

plt.figure()
bplot = sns.boxplot(y="t2_tfr", x="lvl", data=df_t2_tfr, whis=1.5)
plt.title("Two-Finger Rotation Attempts")
bplot = sns.stripplot(y=df_t2_tfr["t2_tfr"], x=df_t2_tfr["lvl"], jitter=True, marker='o', alpha=0.3,color='black')
plt.xlabel("case study group")
plt.ylabel("appearances of gesture")
plt.savefig('plot_bplot_tfr.pdf', bbox_inches='tight')


print('make: plot_bplot_time.pdf')
plt.figure()
bplot = sns.boxplot(y=df["t2_time"], x=df["lvl"], whis=1.5)
plt.title("Time")
bplot = sns.stripplot(y=df["t2_time"], x=df["lvl"], jitter=True, marker='o', alpha=0.3,color='black')
plt.xlabel("case study group")
plt.ylabel("time in seconds")
plt.savefig('plot_bplot_time.pdf', bbox_inches='tight')
plt.figure()



print('make: plot_scatter.pdf')
df_t2_corr = df.loc[:,['lvl','t2_tfr','t2_time']][df.t2_tfr != 0]
df.loc[:,'group'] = df.loc[:,'lvl']

print("Correlation matrix:\n", np.corrcoef(x=df_t2_corr["t2_tfr"], y=df_t2_corr['t2_time']))

df_t2_corr = df.loc[:,['lvl','t2_tfr','t2_time']][df.t2_tfr != 0]
df.loc[:,'group'] = df.loc[:,'lvl']

for i in range(4):
    plt.scatter(x=df_t2_corr[df['group']==i]['t2_tfr'], y=df_t2_corr[df['group']==i]['t2_time'], edgecolors='face')
plt.grid('on')
plt.xlabel('two-finger rotation attempts')
plt.ylabel('time needed for the task')
plt.legend(['Group 0','Group 1','Group 2','Group 3'])
plt.savefig('plot_scatter.pdf', bbox_inches='tight')
plt.figure()



print('statistics, YEAH!!!')
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

# check on homogenious variances
print('levene t2_tfr: ', stats.levene(df_0['t2_tfr'], df_3['t2_tfr']))
print('levene t2_time: ', stats.levene(df_0['t2_time'], df_3['t2_time']))

# check on normality *** 1 ***
print("normality implementation 1:")
diff_tfr = df_0['t2_tfr'] - df_1['t2_tfr']
#stats.probplot(diff_tfr, plot= plt)
#plt.title("probability plot for tfr")
#plt.show()
diff_time = df_0['t2_time'] - df_1['t2_time']
#stats.probplot(diff_time, plot= plt)
#plt.title("probability plot for times")
#plt.show()
print('normality tfr diff: ', stats.shapiro(diff_tfr)[1])
print('normality time diff:', stats.shapiro(diff_time)[1])

print('Welch tfr: ', stats.ttest_ind(df_0['t2_tfr'], df_1['t2_tfr'], equal_var = False).pvalue)
print('Welch time:', stats.ttest_ind(df_0['t2_time'], df_1['t2_time'], equal_var = False).pvalue)

# check on normality ***2***
print("normality implementation 2:")
diff_tfr = df_0['t2_tfr'] - df_2['t2_tfr']
#stats.probplot(diff_tfr, plot= plt)
#plt.title("probability plot for tfr")
#plt.show()
diff_time = df_0['t2_time'] - df_2['t2_time']
#stats.probplot(diff_time, plot= plt)
#plt.title("probability plot for times")
#plt.show()
print('normality tfr diff: ', stats.shapiro(diff_tfr)[1])
print('normality time diff:', stats.shapiro(diff_time)[1])

print('Welch tfr: ', stats.ttest_ind(df_0['t2_tfr'], df_2['t2_tfr'], equal_var = False).pvalue)
print('Welch time:', stats.ttest_ind(df_0['t2_time'], df_2['t2_time'], equal_var = False).pvalue)

# check on normality ***3***
print("normality implementation 3:")
diff_tfr = df_0['t2_tfr'] - df_3['t2_tfr']
#stats.probplot(diff_tfr, plot= plt)
#plt.title("probability plot for tfr")
#plt.show()
diff_time = df_0['t2_time'] - df_3['t2_time']
#stats.probplot(diff_time, plot= plt)
#plt.title("probability plot for times")
#plt.show()
print('normality tfr diff: ', stats.shapiro(diff_tfr)[1])
print('normality time diff:', stats.shapiro(diff_time)[1])

print('Welch tfr: ', stats.ttest_ind(df_0['t2_tfr'], df_3['t2_tfr'], equal_var = False).pvalue)
print('Welch time:', stats.ttest_ind(df_0['t2_time'], df_3['t2_time'], equal_var = False).pvalue)

#df.loc[:,"tot_pz"] = df.loc[:,"t1_pinch"] + df.loc[:,"t2_pinch"] + df.loc[:,"t3_pinch"] + df.loc[:,"m1_pinch"] + df.loc[:,"m2_pinch"] + df.loc[:,"m3_pinch"]
#df.loc[:,"tot_tfr"] = df.loc[:,"t1_tfr"] + df.loc[:,"t2_tfr"] + df.loc[:,"t3_tfr"] + df.loc[:,"m1_tfr"] + df.loc[:,"m2_tfr"] + df.loc[:,"m3_tfr"]
#df.loc[:,"tot_offscrn"] = df.loc[:,"t1_offscrn"] + df.loc[:,"t2_offscrn"] + df.loc[:,"t3_offscrn"] + df.loc[:,"m1_offscrn"] + df.loc[:,"m2_offscrn"] + df.loc[:,"m3_offscrn"]




# tfr vs pinch zoom per task
TFR = [df.loc[:,"t1_tfr"].sum(), df.loc[:,"t2_tfr"].sum(), df.loc[:,"t3_tfr"].sum(), df.loc[:,"m1_tfr"].sum(), df.loc[:,"m2_tfr"].sum(), df.loc[:,"m3_tfr"].sum()]
PZ = [df.loc[:,"t1_pinch"].sum(), df.loc[:,"t2_pinch"].sum(), df.loc[:,"t3_pinch"].sum(), df.loc[:,"m1_pinch"].sum(), df.loc[:,"m2_pinch"].sum(), df.loc[:,"m3_pinch"].sum()]

plt.bar(height=TFR, x=["t 1","t 2","t 3","m 1","m 2","m 3"])
axes = plt.gca()
axes.set_ylim([0,225])
plt.axvline(x=2.5, linewidth=0.5, color='black')
plt.title("Two-Finger Rotation")
plt.xlabel("task")
plt.ylabel("appearances of gesture")
plt.savefig('plot_tfr.pdf', bbox_inches='tight')
plt.figure()

plt.bar(height=PZ, x=["t 1","t 2","t 3","m 1","m 2","m 3"], color='orange')
axes = plt.gca()
axes.set_ylim([0,225])
plt.axvline(x=2.5, linewidth=0.5, color='black')
plt.title("Pinch-Zoom")
plt.xlabel("task")
plt.ylabel("appearances of gesture")
plt.savefig('plot_pz.pdf', bbox_inches='tight')
plt.figure()