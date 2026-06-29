def busca_binaria(array, valor, inicio, fim):
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if array[meio] == valor:
        return meio

    if valor < array[meio]:
        return busca_binaria(array, valor, inicio, meio - 1)

    return busca_binaria(array, valor, meio + 1, fim)


lista = [2, 4, 6, 8, 10, 12, 14]
print(busca_binaria(lista, 10, 0, len(lista)-1))