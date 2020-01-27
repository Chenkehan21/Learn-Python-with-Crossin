#!/usr/bin/env python
# coding: utf-8

# # 字符串拼接
# 通过 % 将 name, age, code 拼接成一句话
# 输出 Crossin is 18, he writes Python.

# In[1]:


name = 'Crossin'
age = 18
code = 'Python'
print("%s is %d, he writes %s" % (name, age, code))


# # 类型转换

# In[2]:


num1 = '3.3'
num2 = 2.5
num1 = float(num1)
print(num1 + num2)


# # bool

# In[3]:


print(bool(-123))
print(bool(0)) # pay attention!
print(bool('abc'))
print(bool('False'))
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(['']))
print(bool(None))

