#!/usr/bin/env python
# coding: utf-8

# # Grid Drawer

# In[ ]:


def draw_grid(m=2, n=3):
    index = 0
    while index < m:
        print('+'+' - - +'*n)
        print('/'+'     /'*n)
        print('/'+'     /'*n)
        index = index + 1
    print('+'+' - - +'*n)


# In[ ]:


if __name__ == '__main__':    
    draw_grid()
    draw_grid(3, 2)


# # Estimate pi

# In[ ]:


import math
def estimate_pi():
    k = 0
    s = 0.0
    t = 0.0
    while True:
        t = (math.factorial(4*k)*(1103+26390*k))/(math.pow(math.factorial(k), 4)*math.pow(396, (4*k)))
        s += t
        k += 1
        if t < 1e-15:
            break
    
    s *= (2*math.sqrt(2))/9801
    return 1/s


# In[ ]:


if __name__ == '__main__':    
    print(estimate_pi() == math.pi)
    print(estimate_pi())
    print(math.pi)


# # Reverse Pair

# In[ ]:


def find_reverse_pair(word_list, case_sensitive = False):
    reverse_pair_list = []
    
    if not case_sensitive:
        word_list = [word.lower() for word in word_list]
    
    for word in word_list:
        if word[::-1] in word_list[word_list.index(word) + 1::]:
            reverse_pair_list.append([word, word[::-1]])
            
    return reverse_pair_list


# In[ ]:


if __name__ == '__main__':   
   import time
   time_start = time.time()

   with open(r'C:\Users\88697\Downloads\words.txt', 'r') as file:
       word_list = file.read().splitlines()
       reverse_pair_list = find_reverse_pair(word_list)

   time_end = time.time()

   print('Finish executing after', time_end - time_start, 's\n')
   print('Found', len(reverse_pair_list), 'reverse pairs\n', )
   print(reverse_pair_list)


# # Reverse Lookup

# In[ ]:


def reverse_lookup(d, v):
    k = []
    if v in d.values():
        for k1 in d:
            if d.get(k1) == v:
                k.append(k1)
    return k


# In[ ]:


if __name__ == '__main__':
    ben = {'name':'James', 'age':26, 'best friend':'James', 'shoe size':26, 24:'James', 23:26}
    print(reverse_lookup(ben, 'James'))

