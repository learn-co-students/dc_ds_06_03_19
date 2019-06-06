#!/usr/bin/env python
# coding: utf-8

# In[1]:


fun_dictionary = {'Stephen': [31.0, 'Curry'], 'Draymond': [29.0, 'Green'], 'Klay': [29.0, 'Thompson'], 'DeMarcus': [28.0, 'Cousins'], 'Kevin': [30.0, 'Durant']}


# In[2]:


fun_dictionary.pop('Kevin')


# In[3]:


fun_dictionary


# In[4]:


fun_dictionary['DeMarcus'][0] = 28.1


# In[5]:


ages = []
for baller in fun_dictionary:
    print(fun_dictionary[baller][1])
    ages.append(fun_dictionary[baller][0])
    
ages


# In[6]:


total_age = 0
for baller in fun_dictionary:
    total_age = total_age + fun_dictionary[baller][0]

mean = total_age/len(fun_dictionary)
mean


# In[7]:


median = None
for age in ages:
    count = {'greater': 0, 'equal': 0}
    for other_age in ages:
        if age > other_age:
            count['greater'] = count['greater'] + 1
        elif age == other_age:
            count['equal'] = count['equal'] + 1
        else:
            pass
    if count['greater'] + count['equal'] == int(len(ages)/2):
        median = age
    elif count['greater'] + count['equal'] >= int(len(ages)/2) >= count['greater']:
        median = age
    else:
        pass
print('', median)


# In[ ]:




