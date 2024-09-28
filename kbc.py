print('welcome to kbc')

a=[1000,2000,3000,4000]
Question = ["1.who is the best crickter in world?\n","2.which fruit is red in colour\n","3.what is the measurement of scale\n","4.which planet is largest in our solar system\n"]
answers = ['virat kohli','apple','15cm','jupitar']
i=0
while (i<4):
 answers1=input(Question[i])
 if answers1==answers[i]:
   print('coorect answer.you have won',a[i])
 else:
   if i==0:
    print('wrong answer. you have won nothing')
   else:
     print('wromg answer.you have won',a[i-1])
   
 i=i+1
if i==4:
  print('congrautulations you have won the game')
print('thank you for playing')
