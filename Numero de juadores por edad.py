import matplotlib.pyplot as plt
 
# Declaramos valores para el eje x (Rango de edades)
eje_x = ['Menores de 18 años', 'Entre 18 a 30 años', 'Entre 30 a 40 años', 'Entre 40 y 50 años', 'Mayores de 50 años']
 
# Declaramos valores para el eje y (Numero de jugadors)
eje_y = [820000000,750000000,500000000,180000000,7000000]

#Colocamas los colores a las barras
color = ["red", "blue", "black", "purple", "orange"]
 
# Creamos Gráfica
plt.bar(eje_x, eje_y, color=color)
 
# Legenda en el eje y (Jugadores)
plt.ylabel('jugadores (100 Millines)')
 
# Legenda en el eje x (Edades)
plt.xlabel('Edades de las personas')
 
# Título de Gráfica
plt.title('Numero de jugadores segun su rango de edad')
 
# Mostramos Gráfica
plt.show()