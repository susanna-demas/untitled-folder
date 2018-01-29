
# coding: utf-8

# In[18]:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.tools.plotting import scatter_matrix
get_ipython().magic('matplotlib inline')

data = pd.read_csv("Desktop/combined.csv")
data.head()


# In[19]:

data


# In[20]:

data.count()


# In[21]:

data[' VIEWCOUNT'].mean()


# In[22]:

data[' LIKECOUNT'].mean()


# In[23]:

data[' DISLIKECOUNT'].mean()


# In[24]:

data[' FAVOURITECOUNT'].mean()


# In[25]:

data.dropna()


# In[26]:

data.count()


# In[27]:

data[' FAVOURITECOUNT'].mean()


# In[28]:

data[' COMMENTCOUNT'].mean()


# In[29]:

data.sort_values([' VIEWCOUNT'], ascending=False)[['NAME', ' VIEWCOUNT']].head(10)


# In[30]:

group_by_views=pd.cut(data[' VIEWCOUNT'],(1000,2000,3000))
grouping_views=data.groupby(group_by_likes).mean()
grouping_views[' VIEWCOUNT'].plot.bar()


# In[50]:

plt.plot(range(1,51), data.sort_values([' LIKECOUNT'], ascending = [0])[[' LIKECOUNT']], 'r', range(1,51), data.sort_values([' VIEWCOUNT'], ascending = [0])[[' VIEWCOUNT']], 'b')
plt.show()


# In[ ]:



