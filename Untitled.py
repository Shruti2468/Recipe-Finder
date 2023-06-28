#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


recipes=pd.read_csv('recipes.csv')
reviews=pd.read_csv('reviews.csv')


# In[3]:


print(recipes.shape)
print(reviews.shape)


# In[4]:


recipes.isnull().sum()


# In[5]:


recipes=recipes[['RecipeId','Name','AuthorName','Images','Description','Calories','RecipeInstructions']]
recipes.isnull().sum()


# In[6]:


reviews.isnull().sum()


# In[7]:


reviews=reviews[['RecipeId','Rating','Review','AuthorId']]


# In[8]:


rating=reviews.merge(recipes,on='RecipeId')
rating


# In[9]:


rating["Review"].fillna("No Comment", inplace = True)
rating["Description"].fillna("No Comment", inplace = True)


# In[10]:


avg_num_rating=rating.groupby('RecipeId')['Rating'].mean().reset_index()
avg_num_rating.rename(columns={'Rating':'avg_rating'},inplace=True)
avg_num_rating.head(111)


# In[11]:


combines_files=avg_num_rating.merge(rating,on='RecipeId').drop_duplicates('RecipeId')

combines_files


# In[62]:


##top 500 dishes

y=rating.groupby('RecipeId').count()['Rating']>1500
y=y[y].index
ratingfiltered=rating[rating['RecipeId'].isin(y)]
toplist=ratingfiltered.drop_duplicates('RecipeId')
toplist


# In[57]:


def search (word):
    matches =combines_files['Name'].str.contains(word,case=False)
    matches=combines_files[matches].index
    matches
    for i in matches:
        id= combines_files.loc[i][0]
        name = combines_files.loc[i][5]
        print(f"{id} :{name}")
        
def item(dish): 
    index = combines_files[combines_files['Name'] == dish].index[0]
    row = combines_files.iloc[index]    
    item = []
    item.append(combines_files.loc[index, 'RecipeId'])
    item.append(combines_files.loc[index, 'Name'])
    item.append(combines_files.loc[index, 'Images'])
    item.append(combines_files.loc[index, 'avg_rating'])
    item.append(combines_files.loc[index, 'Description'])
    item.append(combines_files.loc[index, 'Calories'])
    item.append(combines_files.loc[index, 'RecipeInstructions'])
    return item
    
def recommendation(dish):
    index = combines_files[combines_files['Name'] == dish].index[0]
    value = combines_files.loc[index, 'AuthorName']
    rowsv = combines_files[combines_files['AuthorName'] == value]
    return rowsv
    
    
    


# In[64]:


item('Corn and Potato Chowder')


# In[63]:


recommendation('Corn and Potato Chowder')


# In[16]:


search('chicken ')


# In[17]:


# import pickle


# In[18]:


# pickle.dump(combines_files,open('combined.pkl','wb'))
# pickle.dump(toplist,open('toplist.pkl','wb'))

