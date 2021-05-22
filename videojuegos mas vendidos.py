import matplotlib.pyplot as plt
 
# Declaramos valores para el eje x (Videojuegos)
eje_x = ['Minecraft', 'Wii Sports', 'GTA V', 'Tetris', 'PUBG']
 
# Declaramos valores para el eje y (Ventas)
eje_y = [360000000,82900000,145000000,100000000,70000000]

#Colocamas los colores a las barras
color = ["red", "blue", "black", "purple", "orange"]
 
# Creamos Gráfica
plt.bar(eje_x, eje_y, color=color)
 
# Legenda en el eje y (entas
plt.ylabel('Ventas (100 Millones)')
 
# Legenda en el eje x videojuegos
plt.xlabel('Videojuegos')
 
# Título de Gráfica
plt.title('Videojuegos mas vendidos')
 
# Mostramos Gráfica
plt.show()