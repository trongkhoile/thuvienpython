#xoay mảng
import collections
a_list = collections.deque([1, 2, 3, 4, 5])
a_list.rotate(2)
shifted_list = list(a_list)
print(shifted_list)

#hoán vị
import itertools
print(list(itertools.permutations([1, 2, 3])))

#de quy quay lui
n = 3
x = n*[0]
def fine_print(x):
   tmp = '' 
   for i in x:
       for j in range():
      tmp += str(i)
   return tmp
   
def bin_gen(i):
   for j in range(0,2):
      x[i] = j
      if i == n-1:
         print(fine_print(x))
      else:
         bin_gen(i+1)
bin_gen(0)

