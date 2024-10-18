# exercicio 1    
# numero = float(input('digite um numero: '))
# if numero >=1:
#     print('o numero é positivo')
# elif numero == 0:
#     print('O numero é zero')
# else:
#     print('O numero é negativo')

# # exercicio 2
# idade = int(input('digite idade: '))
# if idade >=18:
#     print('maior de idade')
# else:
#     print('menor de idade')

# # 
# # exercicio 3
# numero = int(input('digite um numero: '))
# if numero % 2 == 0:
#     print('O numero em par')
# else:
#     print('O numero e impar')

# # exercicio 4
# numero1 = int(input('digite preimeiro numero: '))
# numero2 = int(input('didite segundo numero: '))
# if numero1 > numero2:
#     print(f'O numero{numero1} e maior ')
# else:
#     print(f'O numero {numero2} e maior')
# # exercicio 5
# produto = float(input('digite um valor: '))
# if produto >= 100:
#     print('desconte de 10%',produto - (produto * 0.10))
# else:
#     print('sem desconto')

# # exercicio 6
# numero = int(input('digite um numero: '))
# if numero % 5 == 0:
#     print('O numero e multiplo')
# else: 
#     print('O numero não e multiplo')

# # exercicio 7
# nota_1 = float(input('digite primeira nota: '))
# nota_2 = float(input('digite segunda nota: '))
# nota_3 = float(input('digite terçeira nota: '))
# media = (nota_1 + nota_2 + nota_3) / 3
# if media >= 7:
#     print('Parabens foi aprovado')
# else:
#     print('Reprovado')

# # exercicio 8
# senha = input('digite senha de acesso: ')
# if senha == 'python123_EFG':
#  print('Acesso permitido')
# else:
#    print('Acesso negado')
    
# # exercicio 9
# idade = int(input('digite sua indade: '))
# if idade <= 5 :
#  print('Entrada Gratuita')
# elif idade >= 60:
#  print('Entrada gratuita')
# else:  
#  print('Entrada não gratuita') 

# exercicio 10
# numero = int(input('digite um nota de 0 a 10: '))
# if numero >= 0 and numero <=10:
#  print('tudo certo')
# else:
#  print('erro informe numero valido')
 
# # exercicio 11
# idade = int(input('digite idade: '))
# if idade < 12:
#  print('criança')
# elif idade <=17 and 12:
#  print('Adolescente')
# else:
#  print('Adulto') 

# # exercicio 12
# numero1 = int(input('digite primeiro numero: '))
# numero2 = int(input('digite segundo numero: '))
# numero3 = int(input('digite terceiro numero: '))
# if numero1 > numero2 and numero3:
#  print('O maior numero é: ',numero1)
# elif numero2 > numero3 and numero1:
#  print('O maior numero é: ',numero2)
# else: 
#  print('O maior numero é: ',numero3)

# # exercicio 13

# num1 = int(input('digite primeiro numero: '))
# num2 = int(input('digite segundo numero: '))
# if num2 ==0:
#  print('A divisão não e posivel')
# else:
#  soma = num1 / num2
# print('A divisão é ', soma)

# # exercicio 14
# numero = int(input('informe um numero: '))
# if numero >=10 and numero <=50:
#  print('está entre 10 e 50')
# else:
#  print('Não esta entre 10 e 50')
 
# # exercicio 15
# media = float(input('insira a media: '))
# if media >=7:
#  print('Parabens foi "Aprovado"')
# elif media >= 5 and media < 7:
#  print('Está de recuperação')
# else:
#  print('Está Reprovado') 

# #exercicio 16
# peso = float(input('insira seu peso: '))
# altura = float(input('insira altura: '))
# imc = peso /(altura*altura)
# if imc < 18.5:
#  print(f'imc: {imc: .2f} Está abaixo do peso!!')
# elif imc >= 18.5 and imc < 25:
#  print(f'imc: {imc: .2f} peso normal!!') 
# else:
#  print(f'imc: {imc: .2f} está acima do peso!!')

#exercicio 17
# lado_1 = float(input('informe um lado: '))
# lado_2 = float(input('infotme segundo lado: '))
# lado_3 = float(input('informe terçeiro lado: '))

# if lado_1 > (lado_2 + lado_3) or lado_2 > (lado_1 + lado_3) or lado_3 > (lado_1 + lado_2):
#  print('não pode ser triangulo')
# elif lado_1 == lado_2 == lado_3:
#  print('Equilatero')
# elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
#  print('isosceles')
# else:
#  print('Escaleno') 

# #exercicio 18

# adm = input('insira usuario: ')
# senha = input('senha de acesso: ')
# if adm == 'admin' and senha == '1234':
#  print('login bem sucedido')
# else:
#  print('Acesso negado!!') 

# # exercicio 19

# idade = int(input('digite a idade: '))
# dirigir = 18 - idade
# if idade >=18:
#  print(f'com {idade} pode dirigir')
# else:
#   print(f'Falta {dirigir} anos para dirigir')