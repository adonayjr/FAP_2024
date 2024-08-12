def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial não é definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial

print(calcular_fatorial(5))  # Saída: 120
print(calcular_fatorial(3))  # Saída: 6
print(calcular_fatorial(7))  # Saída: 5040
