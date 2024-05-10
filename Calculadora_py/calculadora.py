print("Escolha um dos sinais: '+' (soma), '-' (subtração), '/'  (divisao), '*' (multiplicação)")

while True:
    
    T = input("Um sinal para efetuar a conta: ")
    number_1 = int(input("número_1: "))
    number_2 = int(input("número_2: "))
    
    if T == "q":
        break
    
    if T == "+":
      R = number_1 + number_2

    if T == "-":
      R = number_1 - number_2

    if T == "/":
      R = number_1/ number_2
  
    if T == "*":
      R = number_1*number_2

    print(R)
    
  
   