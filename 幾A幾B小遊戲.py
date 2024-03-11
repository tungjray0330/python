import random

answer=random.sample(range(0,10),4)
a=0;b=0

while a!=4:
  a=0;b=0
  guess=input('Guess a non-repeating four-digit number =')
  for i in range(0, 4):
      for j in range(0, 4):
          if i == j and guess[i] == str(answer[j]):
              a += 1
          elif i != j and guess[i] == str(answer[j]):
              b += 1
  print(a,end='');print("A",end='');print(b,end='');print("B")


while a==4 :
    print('Congratualations!You got the right number!')
    break
            
            
