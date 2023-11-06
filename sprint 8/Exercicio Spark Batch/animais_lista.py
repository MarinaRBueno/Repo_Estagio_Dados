import csv


def animais_ordem_crescente():
    animais = ['Elefante', 'Girafa', 'Gato', 'Tigre', 'Zebra', 'Cobra', 'Macaco', 'Urso','Rinoceronte', 'Cachorro', 'Canguru', 'Gorila', 'Borboleta', 'Camelo', 'Panda', 'Lobo', 'Raposa', 'Coala', 'Cavalo', 'Tartaruga']

    animais.sort()

    with open('lista_animal.csv', 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        [print(animal) or writer.writerow([animal]) for animal in animais]


animais_ordem_crescente()
