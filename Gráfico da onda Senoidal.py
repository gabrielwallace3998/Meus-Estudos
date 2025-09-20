# Importa as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Cria um vetor com 100 valores igualmente espaçados de 0 a 10
x = np.linspace(0, 10, 100)

# Calcula o seno para cada valor do vetor x, criando o vetor y
y = np.sin(x)

# Cria a figura e o eixo do gráfico
fig, ax = plt.subplots()

# Plota o vetor y em função do vetor x
ax.plot(x, y)

# Exibe o gráfico na tela
plt.show()