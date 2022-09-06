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

#chuyen toan bo mang ve int or str
print(list(map(int,["1","2"])))

#in ra tap con

from itertools import combinations
comb = combinations([1, 2, 3], 2)
for i in list(comb):
    print (i)
    
#loc cac phan tu 
vao = [s for s in vao if s != "null"]


k = [s for s in range(1,4)]
#chia cac chuoi giong nhau dung canh nhau
from itertools import groupby
test_str = 'ggggffggisssbbbeessssstt'
res = ["".join(group) for ele, group in groupby(test_str)]
print("Consecutive split string is : " + str(res))

#chia chuỗi thành subword cạnh nhau
def combos(s):
  if not s:
    return
  yield (s,)
  for i in range(1, len(s)):
    for c in combos(s[i:]):
      yield (s[:i],) + c
for c in combos('Bang'):
  print(c)

# tim tap giao
X = set([1, 3, 5, 7]) 
Y = set([2, 3, 5, 8]) 
print(X.intersection(Y))
