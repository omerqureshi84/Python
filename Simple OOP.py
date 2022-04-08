#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Sample():
    pass

my_sample = Sample()

type(my_sample)


# In[46]:


class Dog():
    
    spec = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
        
    def bark(self,number):
        print(f'woof! My name is {self.name} and the number is {number}')


# In[47]:


my_dog = Dog('Lab','ozy')


# In[48]:


my_dog.breed


# In[49]:


my_dog.name


# In[50]:


my_dog.spec


# In[51]:


my_dog.bark(1)


# In[61]:


class Circle():
    pi = 3.14
    
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi
        
    def get_circumference(self):
        return 2 * self.pi * self.radius


# In[62]:


my_circle = Circle(30)


# In[63]:


my_circle.get_circumference()


# In[64]:


my_circle.get_circumference()


# In[66]:


my_circle.area


# In[ ]:





# In[ ]:




