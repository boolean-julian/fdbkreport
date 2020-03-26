#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams.update({'font.size': 14})

data = pd.read_csv("questionnaire.csv")

df = data
data.head(50)


# In[2]:


data.shape


# In[3]:


from matplotlib.ticker import MaxNLocator

data_age=data['1_Age']
ax1 = data_age.plot(kind='hist', title='age of participants')
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()


# In[4]:


version_count=data['implementation'].value_counts()
version_count.plot(kind='bar', title='Implementations')
plt.show()


# In[5]:


# https://usabilitygeek.com/how-to-use-the-system-usability-scale-sus-to-evaluate-the-usability-of-your-website/

sus_df = data.copy()
sus_df.drop(['date', 'timestamp', 'issues', 'offscreen', '1_Age', '2_priorExp', 'oq'], axis=1, inplace=True)

odd_q = ['3_SUS_1', '5_SUS_3', '7_SUS_5', '9_SUS_7', '11_SUS_9']
even_q = ['4_SUS_2', '6_SUS_4', '8_SUS_6', '10_SUS_8', '12_SUS_10']
all_q = odd_q + even_q

for question in odd_q:
    sus_df[question] = sus_df[question] - 1
for question in even_q:
    sus_df[question] = 5 - sus_df[question]
sus_df['total'] = 0
for question in all_q:
    sus_df['total'] = sus_df['total'] + sus_df[question]
sus_df['total'] *= 2.5 

sus_df.head(50)
#sus_df.to_csv('output.csv')


# In[6]:


# !!!!!!!!!
#sus_df = sus_df.drop(sus_df.index[[37]])


implementations = ["TM0", "MT0", "TM1", "MT1", "TM2", "MT2","TM3","MT3"]

sus_result = np.zeros(8)

for index, version in enumerate(implementations):
    sus_result[index]= sus_df.loc[(sus_df['implementation'] == version),'total'].mean()
    print(index, sus_result[index])
    
plt.bar(height=sus_result, x=implementations)
plt.axhline(y=68, linewidth=1, color='r')
plt.axvline(x=1.5, linewidth=0.5)
plt.axvline(x=3.5, linewidth=0.5)
plt.axvline(x=5.5, linewidth=0.5)
plt.title('SUS score for different test groups')
plt.show()



sus_result_imp = np.zeros(4)

for i in range(4):
    sus_result_imp[i] = (sus_result[2*i] + sus_result[2*i+1]) / 2
    
plt.bar(height=sus_result_imp, x=["0","1","2","3"])
plt.axhline(y=68, linewidth=1, color='r')
#plt.axvline(x=1.5, linewidth=0.5)
#plt.axvline(x=3.5, linewidth=0.5)
#plt.title('DUMMY: SUS score for different implementations')
plt.ylabel('SUS score')
plt.xlabel('case study group')
plt.savefig('plot_sus.pdf', bbox_inches='tight')
plt.plot()


# In[7]:


imp0 = np.zeros(10)
imp1 = np.zeros(10)
imp2 = np.zeros(10)
imp3 = np.zeros(10)

#for index, version in enumerate(implementations):
for qi, question in enumerate(all_q):
    imp0[qi] = sus_df.loc[(sus_df['implementation'] == 'TM0'),question].append(sus_df.loc[(sus_df['implementation'] == 'MT0'),question]).mean()
    imp1[qi] = sus_df.loc[(sus_df['implementation'] == 'TM1'),question].append(sus_df.loc[(sus_df['implementation'] == 'MT1'),question]).mean()
    imp2[qi] = sus_df.loc[(sus_df['implementation'] == 'TM2'),question].append(sus_df.loc[(sus_df['implementation'] == 'MT2'),question]).mean()
    imp3[qi] = sus_df.loc[(sus_df['implementation'] == 'TM3'),question].append(sus_df.loc[(sus_df['implementation'] == 'MT3'),question]).mean()

fig, (ax1,ax2, ax3, ax4) = plt.subplots(1,4, figsize=(15,5))    

ax1.bar(height=imp0, x=np.arange(1,11,1))
ax2.bar(height=imp1, x=np.arange(1,11,1))
ax3.bar(height=imp2, x=np.arange(1,11,1))
ax4.bar(height=imp3, x=np.arange(1,11,1))
ax1.grid('on')
ax2.grid('on')
ax3.grid('on')
ax4.grid('on')
ax1.set_title('feedback 0')
ax2.set_title('feedback 1')
ax3.set_title('feedback 2')
ax4.set_title('feedback 2')
plt.show()


# In[8]:


tag = np.asarray([data.tag1.sum(),data.tag2.sum(),data.tag3.sum(),data.tag4.sum()])


# In[9]:


tag


# In[10]:


plt.bar(height=tag, x=["app feedback","app controls","prototype","other"])
#plt.title('DUMMY: Amount of open question answers categorized by labels')
plt.savefig('plot_tags.pdf')
plt.ylabel('appearances')
plt.xlabel('answer category')
plt.xticks(rotation=20)
plt.savefig('plot_tags.pdf', bbox_inches='tight')
plt.plot()


# In[11]:


# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# width of the bars
barWidth = 0.18
 
# Choose the height of the blue bars
bars1 = [df[df["lvl"] == 0]["tag1"].sum(), df[df["lvl"] == 1]["tag1"].sum(), df[df["lvl"] == 2]["tag1"].sum(), df[df["lvl"] == 3]["tag1"].sum()]
bars2 = [df[df["lvl"] == 0]["tag2"].sum(), df[df["lvl"] == 1]["tag2"].sum(), df[df["lvl"] == 2]["tag2"].sum(), df[df["lvl"] == 3]["tag2"].sum()]
bars3 = [df[df["lvl"] == 0]["tag3"].sum(), df[df["lvl"] == 1]["tag3"].sum(), df[df["lvl"] == 2]["tag3"].sum(), df[df["lvl"] == 3]["tag3"].sum()]
bars4 = [df[df["lvl"] == 0]["tag4"].sum(), df[df["lvl"] == 1]["tag4"].sum(), df[df["lvl"] == 2]["tag4"].sum(), df[df["lvl"] == 3]["tag4"].sum()]
   
 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]

# Create bars
plt.bar(r1, bars1, width = barWidth, label='app feedback', edgecolor="black") 
plt.bar(r2, bars2, width = barWidth, label='app controls', edgecolor="black")
plt.bar(r3, bars3, width = barWidth, label='prototype', edgecolor="black")
plt.bar(r4, bars4, width = barWidth, label='other', edgecolor="black")

# general layout
plt.xticks([r + 1.5* barWidth for r in range(len(bars1))], ['0', '1', '2', '3'])
plt.ylabel('appearances')
plt.xlabel('case study group')
#plt.title('apperances of answers per case study group')
plt.legend()

# Show and save graphic
plt.savefig('plot_tags_implementations.pdf', bbox_inches='tight')
plt.show()


# In[12]:


df[df["lvl"] == 0][df["tag1"] == 1]['oq'].tolist()


# In[13]:


#print(df[df["lvl"] == 0][df["tag1"] == 1]['oq'].tolist(), sep="\n\n")
df[df["lvl"] == 1][df["tag1"] == 1]['oq'].tolist()


# In[14]:


df[df["lvl"] == 2][df["tag1"] == 1]['oq'].tolist()


# In[15]:


df[df["lvl"] == 3][df["tag1"] == 1]['oq'].tolist()


# In[ ]:





# In[ ]:





# In[ ]:




