import matplotlib.pyplot as plt
import os

input = os.getcwd()
input += r"\image in text.txt"

x = []
y = []

with open(input, "r") as file:
    line_num = 0
    for line in file:
        temp = []
        for letter in line:
            if letter != '\n':
                temp.append(letter)
                
        y.append(temp)
        line_num += 1

image_size = line_num

x = list(range(image_size))

y_height = []
for i in range(image_size):
    y_height.extend(x)

x_flat = []
y_flat = []

for x, y_list in zip(x, y):
    x_flat.extend([x] * len(y_list))
    y_flat.extend(y_list)

colors = []
point_num = 0
for point in y_flat:
    color = 'gray'
    match y_flat[point_num]:
        case '1':
            color = 'red'
        case '2':
            color = 'orange'
        case '3':
            color = 'yellow'
        case '4':
            color = 'blue'
        case '5':
            color = 'green'
        case '6':
            color = 'purple'
        case '7':
            color = 'white'
        case '8':
            color = 'black'
    colors.append(color)
    point_num += 1

plt.scatter(x_flat, y_height, c=colors)

plt.show()