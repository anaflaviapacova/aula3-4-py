
def soma(a, b):
	return a + b

def subtracao(a, b):
	return a - b

def multiplicacao(a, b):
	return a * b

def divisao(a, b):
	if b == 0:
		return None
	return a / b

print("-----Calculadora-----")
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
op = input("Digite o número da operação desejada: ")

n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

if op == '1':
	resultado = soma(n1, n2)
	print(f"A soma é: {resultado:.2f}")
elif op == '2':
	resultado = subtracao(n1, n2)
	print(f"A subtração é: {resultado:.2f}")
elif op == '3':
	resultado = multiplicacao(n1, n2)
	print(f"A multiplicação é: {resultado:.2f}")
elif op == '4':
	resultado = divisao(n1, n2)
	if resultado is None:
		print("Divisão por zero não é permitida.")
	else:
		print(f"A divisão é: {resultado:.2f}")
else:
	print("Operação inválida.")
