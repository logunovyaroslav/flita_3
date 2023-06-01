import networkx as nx
import matplotlib.pyplot as plt


def read_file():
    edges = []
    with open('input.txt', 'r') as file:
        for line in file:
            edges.append(line.replace('\n', '').split(' '))
        for i in range(len(edges)):
            for j in 0, 1:
                try:
                    edges[i][j] = int(edges[i][j])
                except:
                    raise Exception('Invalid input')
    return edges


def find_max(arrays):
  max_val = float('-inf')
  for array in arrays:
    for num in array:
      if num > max_val:
        max_val = num
  return max_val


# Запрос количества вершин и ребер у пользователя
edges = read_file()
n = int(find_max(edges))
# Создание пустого графа
G = nx.Graph()
# Добавление вершин в граф
for i in range(n):
    G.add_node(i+1)
for n in range(len(edges)):
    for q in range(len(edges[n])):
        if q % 2 == 0:
            x = edges[n][q]
            y = edges[n][q + 1]
            G.add_edge(x, y)
if nx.is_connected(G):
    print("\nГраф связный\n")
else:
    print("\nГраф не связный\n")

nx.draw(G, with_labels=True)
plt.show()
