import random
import time
import math

class keyboardDisable():
    def __init__(self):
      import msvcrt
      self.on = False

    
    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def __call__(self): 
        while self.on:
          msvcrt.getwch()


    
x = 1
alltotal = 0
sessioncount = 0
roundcount = 0
print("Simple reaction test game")
print("You will input the number of rounds in each test")
print("Type 0 for the number of rounds to end the session, you will see your session stats")
print("egg")
print("----------------------------------------------------------------")
sessionstart = time.time()
while x != 0:
  sessioncount += 1
  x = input("Number of rounds: ")
  total = 0
  for i in range(0, int(x)):
      print("Ready?")
      text = input() # just press enter when it says Ready?
      time.sleep(random.randint(0,9000)/1000+1)
      disable = keyboardDisable()
      disable.start()
      print("Go!")
      disable.stop()
      time_start = time.time()
      text = input() # just press enter when it says Go!
      time_done = time.time()
      print(f"Time: {round(1000*(time_done-time_start))}ms")
      total += round(1000*(time_done-time_start))
      alltotal += round(1000*(time_done-time_start))
      roundcount+=1

  print(f"Mean of {x}: {round(total/int(x), 2)}ms")

sessionend = time.time()
print("Session stats:")
print(f"Total time elapsed in session: {math.floor((sessionend - sessionstart)/60)}min {sessionend - sessionstart - (math.floor((sessionend - sessionstart)/60))*60}sec")
print(f"Total number of games: {sessioncount}")
print(f"Total number of rounds: {roundcount}")
print(f"Average reaction time in session: {round(alltotal/roundcount, 2)}ms")

