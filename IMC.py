nome = input('Qual é seu nome? : ')
altura = float(input('Qual é sua altura? : '))
peso = int(input('Qual é seu peso? : '))
imc = peso /altura ** 2

print(nome,'Sua altura é',altura, 'Seu peso é',peso, 'e seu IMC é', imc) 