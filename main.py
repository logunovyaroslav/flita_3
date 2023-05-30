import networkx as nx
import matplotlib.pyplot as plt

# Запрос количества вершин и ребер у пользователя
number = input("Введите количество вершин: ")
while not number.isnumeric():
    print("Невозможное значение")
    number = input("Введите количество вершин: ")
n = int(number)
while n < 0:
    print("Количество вершин не может быть отрицательным")
    n = int(input("Введите количество вершин: "))
# Создание пустого графа
G = nx.Graph()
# Добавление вершин в граф
for i in range(n):
    G.add_node(i+1)
while True:
    action = input("Для создания нового соединения напишите - 'add'; для отображения графа напишите - 'draw'; "
                   "для того что бы закончить напишите - 'end': \n")
    match action:
        case 'add':
            str_x = input("Введите исходящую вершину графа: ")
            while not str_x.isnumeric():
                print("Невозможное значение")
                str_x = input("Введите исходящую вершину графа: ")
            x = int(str_x)
            while x > n or x <= 0:
                print("Невозможное значение")
                x = int(input("Введите исходящую вершину графа: "))
            str_y = input("Введите приходящую вершину графа: ")
            while not str_y.isnumeric():
                print("Невозможное значение")
                str_y = input("Введите приходящую вершину графа: ")
            y = int(str_y)
            while y > n or y <= 0:
                print("Невозможное значение")
                y = int(input("Введите исходящую вершину графа: "))
            G.add_edge(x, y)
            # проверяем связанность графа
            if nx.is_connected(G):
                print("\nГраф связный\n")
            else:
                print("\nГраф не связный\n")
        case 'draw':
            # Отображение графа
            nx.draw(G, with_labels=True)
            plt.show()
        case 'end':
            break
        case _:
            print("Неизвестное действие")
