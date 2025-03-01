import random
import math
pm = input("Put preformance here mode bad or good: ")
td = open(input())
exec(str("goals = [") + str(td.read() + ", 0") + str("]"))
en = []
gl = len(goals)
for i in range(gl):
   en.append(math.e ** goals[i])
tr = 1
tasks = []
l = 0
def randomneroun(small, large):
    return math.e ** random.randint(small, large)
def renforcementlearning(ma, mi):
   global tr
   global en
   global tasks
   global gl
   global l
   gl = len(en)
   randomness = 0
   rop = 0
   rpl = 0
   tr = 1
   l = mi + 1
   glp = 0
   while True:
      glp = gl
      randomness = randomneroun(ma, mi) * tr
      print(randomness)
      try:
         l = abs(l - en[0])
      except:
         pass
      if gl == 3:
         break
      elif randomness not in en:
         if en[0] < l:
            try:
               tr -= l * glp
            except:
               tr -= l * glp
         else:
            try:
               tr += l * glp
            except:
               tr += l * glp
         print(tr)
      elif randomness in en:
         print(tr)
         gl -= 1
         en.pop(0)
         print(str("removed ") + str(gl))
         tasks.append(tr)
      else:
         pass
if pm == "bad":
   __name__ = "__main__"
renforcementlearning(min(goals), max(goals))
print(tasks)
answers = []
tl = len(tasks)
for i in range(tl):
   answers.append(tasks[i] * random.randint(min(goals), max(goals)))
   print(answers)
if pm == "bad":
   __name__ = "__main__"
__name__ = ""
if __name__ == "__main__" & pm == "bad":
   main()
