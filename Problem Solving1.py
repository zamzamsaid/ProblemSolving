#!/usr/bin/env python
# coding: utf-8

# In[9]:


#list
candles=[4,1,4,3]
#find max
max_candle=candles[0]
for candle in candles:
    if candle>max_candle:
        max_candle=candle
print(max_candle)

#find count
count=0
for candle in candles:
    if candle == max_candle:
        count=count+1
print(count)


# In[ ]:





# In[ ]:




