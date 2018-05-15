total = int(input())
for _ in range(total) :
   number = int(input())
   if number < 38 or number % 5 < 3: 
      print(number)
   elif number % 5 > 2 :
      print(number + ( 5 - number % 5))