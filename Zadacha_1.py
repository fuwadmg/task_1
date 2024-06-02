import json
import numpy as np
import os
import matplotlib.pyplot as plt

# Создание директории для сохранения результатов
directory = os.path.join(os.getcwd(), "results")
if not os.path.exists(directory):
    os.makedirs(directory)

# Задание параметров функции и интервала
a = -0.25
x_min = -10
x_max = 10
step = 0.1

# Создание массива значений x
x = np.arange(x_min, x_max + step, step)

# Расчет значений функции
f = lambda x: sum([i * np.cos((i + 1) * x + i) for i in range(1, 6)])*sum([i * np.cos((i + 1) * x + a) for i in range(1, 6)])
y = f(x)


# Создание словаря для сохранения результатов
data = {
    "x": list(x),
    "y": list(y)
}

# Преобразование словаря в JSON
json_data = json.dumps(data)

# Сохранение результатов в JSON-файл
filename = os.path.join(directory, "results.json")
with open(filename, "w") as file:
    file.write(json_data)

# Построение графика
plt.plot(x, y)
plt.title("График функции f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
