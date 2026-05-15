
temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

maior_quantidade_criticos = -1
sala_maior_risco = 0


for i in range(0, len(temperaturas)):
    soma = 0
    registros_criticos = 0

    for j in range(0, len(temperaturas[i])):
        soma += temperaturas[i][j]

        if temperaturas [i][j] >= 33:
            registros_criticos += 1

    media = soma / len(temperaturas[i])
    numero_sala = i +1

    print("Sala: ", numero_sala)
    print("Media: ", media)
    print("Registros criticos: ", registros_criticos)

    if registros_criticos > maior_quantidade_criticos:
        maior_quantidade_criticos = registros_criticos
        sala_maior_risco = numero_sala
print(f"Sala com maior risco: Sala {sala_maior_risco}")

