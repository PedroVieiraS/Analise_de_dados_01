numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

if(numero1 > numero2):
  print(f"o {numero1} é maior que o {numero2}")
elif(numero2 > numero1):
  print(f"o {numero2} é maior que o {numero1}")
elif(numero1 == numero2):
  print(f"o {numero1} é igual ao {numero2}")