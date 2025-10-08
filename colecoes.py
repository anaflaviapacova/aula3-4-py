numeros = [8, 3, 15, 7, 2]

print(f"Lista original: {numeros}")
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")

numeros_ordenados = sorted(numeros)
print(f"Lista ordenada: {numeros_ordenados}")

print(f"Quantidade de elementos: {len(numeros)}")

media = sum(numeros) / len(numeros)
print(f"Média dos valores: {media:.2f}")
