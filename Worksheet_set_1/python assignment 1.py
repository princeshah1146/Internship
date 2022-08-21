#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 11. Write a python program to find the factorial of a number


# In[1]:


num=int(input("enter the number\n"))

factorial=1

if num<0:
    print("factorial does not exit for negative number")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial of a given number is",factorial)


# In[2]:


# 12. Write a python program to find whether a number is prime or composite


# In[4]:


n=int(input("enter the number\n"))

for i in range(2,n):
    if n%i==0:
        print("given number is a composite number")
        break
    else:
        print("given number is a prime number")
        break


# In[5]:


# 13. Write a python program to check whether a given string is palindrome or not.


# In[8]:


def isPalindrome(s):
    return s==s[::-1]

s="malayalam"
ans=isPalindrome(s)

if ans:
    print("yes")
else:
    print("No")


# In[9]:


# 14. Write a Python program to get the third side of right-angled triangle from two given sides


# In[17]:


import math
def rightangled(a,b):
    c=math.sqrt(a*a+b*b)
    return c

print("third side of right angled triangle is: ",rightangled(3,4))
    


# In[18]:


# 15.Write a python program to print the frequency of each of the characters present in a given string


# In[20]:


test_str="GreeksforGreeks"

all_freq={}

for i in test_str:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1

print("count of all characters in GreeksforGreeks is:\n ",str(all_freq))


# In[ ]:




