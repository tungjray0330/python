import time
import random
left=30
remain=left%5
y=(left-remain)//5
print("Try not to get the last spot by taking away 1-3 spots at a time.")
time.sleep(1)
def circles(times):
    for c in range(times):
      print("○ "*5)
print()
circles(y)
if remain !=0:
    print("○ "*remain)
print("// 30 spots left")
time.sleep(1.5)
print()
print("I go first")
time.sleep(1)

firstanswer=random.sample(range(1,4),1)
firstanswer=int(firstanswer[0])
left=30-firstanswer
remain=left%5
y=(left-remain)//5
print("I'll take ",firstanswer,end="")
if firstanswer==1:
    print(" spot away")
else:
    print(" spots away")
time.sleep(0.5)
print()
circles(y)
if remain !=0:
    print("○ "*remain)
print("// ",left,"spots left")
print()
time.sleep(1)
print("Now is your turn")
time.sleep(1)

while 0< left <= 30 :
  number=input("Enter the quantity of spots that you want to take away:")
  number=int(number)
  if 1 <= number <= 3:
      left=left-number
      left=int(left)
      remain=left%5
      y=(left-remain)//5
      print()
      circles(y)
      if remain !=0:
          print("○ "*remain)
      if left==1:
          print("// ",left,"spot left")
          print()
          time.sleep(1)
          print("I get the last spot.")
          print()
          time.sleep(1)
          print("You win!")
          break
      elif left==0:
          print("// ",left,"spot left")
          print()
          time.sleep(1)
          print("You get the last spot.")
          print()
          time.sleep(1)
          print("You lose!")
          break
      else:
          print("// ",left,"spots left")
          time.sleep(1)
          print()
          print("Now is my turn")
          time.sleep(1)
      if left%4 ==3:
          print("I'll take 2 spots away ")
          left=left-2
          remain=left%5
          y=(left-remain)//5
          time.sleep(0.5)
          print()
          circles(y)
          if remain !=0:
              print("○ "*remain)
          if left != 1:
              print("// ",left,"spots left")
              time.sleep(1)
              print()
              print("Now is your turn")
          else:
              print("// ",left,"spot left")
              time.sleep(1)
              print()
              print("You lose!")
              left=0
      elif left%4 ==1:
          random_answer=random.sample(range(1,4),1)
          random_answer=int(random_answer[0])
          print("I'll take ",random_answer,end="")
          if random_answer==1:
              print(" spot away")
          else:
              print(" spots away")
          left=left-random_answer
          time.sleep(0.5)
          remain=left%5
          y=(left-remain)//5
          print()
          circles(y)
          if remain !=0:
              print("○ "*remain)
          if left !=1:
              print("// ",left,"spots left")
              time.sleep(1)
              print()
              print("Now is your turn")
      elif left%4 ==0:
          print("I'll take 3 spots away ")
          left=left-3
          remain=left%5
          y=(left-remain)//5
          time.sleep(0.5)
          print()
          circles(y)
          if remain !=0:
              print("○ "*remain)
          if left !=1:
              print("// ",left,"spots left")
              time.sleep(1)
              print()
              print("Now is your turn")
          else :
              print("// ",left,"spot left")
              time.sleep(1)
              print()
              print("You lose!")
              left=0
      else:
          print("I'll take 1 spot away ")
          left=left-1
          remain=left%5
          y=(left-remain)//5
          time.sleep(0.5)
          print()
          circles(y)
          if remain !=0:
              print("○ "*remain)
          if left !=1:
              print("// ",left,"spots left")
              time.sleep(1)
              print()
              print("Now is your turn")
          else :
              print("// ",left,"spot left")
              time.sleep(1)
              print()
              print("You lose!")
              left=0
  else:
      print("The number you choose must be between 1 to 3")


    

    
    
    
    
    
    
    
    
    
    
    
    
    