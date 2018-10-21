
import sys

def recu(a , b):
   if len(b) == 0:
       return node(0 ,0 ," ")
   root = b[0]
   if len(a) == 1:
       return node(0, 0, root)


   j = 0
   for i in range(len(a)):
       if a[i] == root:
           break
       j += 1

   left_child = recu(a[0:j], b[1: j +1]) #substr
   right_child = recu(a[ j +1:len(a)], b[ j +1:len(a)])

   return node(left_child ,right_child ,root)

count = 0

maxlvl = 0
maxpos = 0

class node:
   def __init__(self, left, right, char):
       self.left = left
       self.right = right
       self.char = char

       self.place = None
       self.shown = False

   def compute_count(self, lvl = 0):
       node_list.append(self)
       self.lvl = lvl

       if self.left != 0:
           self.left.compute_count(lvl + 1)
       global count
       self.place = count
       count += 1
       if self.right != 0:
           self.right.compute_count(lvl + 1)
       global maxlvl

       maxlvl = max(self.lvl , maxlvl)

   # ef compute_count(self):
def main():
   global maxlvl, count, maxpos,node_list
   while (1):
       count = 0
       maxlvl = 0
       maxpos = 0

       s1 = input()
       s2 = input()

       three = recu(s1, s2)

       node_list = []
       levels = []

       three.compute_count()

       for i in range(maxlvl +1):
           levels.append([])


       for i in range(len(node_list)):
           # node_list[i].place = i
           levels[ node_list[i].lvl ].append(node_list[i])

       maxpos = len(node_list)
       #print(levels)
       for level in levels:
           showlvl = []
           for i in range(maxpos):
               showlvl.append(" ")

           for node in level:
               showlvl[node.place] = node.char

           ans = ""
           for i in range(len(showlvl)):
               ans += showlvl[i]

           print(ans)
   return 0
main()
