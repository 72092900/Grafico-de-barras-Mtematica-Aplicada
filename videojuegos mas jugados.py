import matplotlib.pyplot as plt
 
# Declaramos valores para el eje x (Juegos)
eje_x = ['POBG', 'CroosFire', 'Dungeon Fighter Online', 'QQ Speed/GKART/Speed', 'Minecfat']
 
# Declaramos valores para el eje y (Personas que los jugaron)
eje_y = [1037000000,1000000000,700000000,700000000,700000000]

#Colocamas los colores a las barras
color = ["purple", "red", "black", "blue", "orange"]
 
# Creamos Gráfica
plt.bar(eje_x, eje_y, color=color)
 
# Legenda en el eje y (jugadores)
plt.ylabel('Número de personas que lo jugaron (100 Billones)')
 
# Legenda en el eje x (juegos)
plt.xlabel('Videojuegos')
 
# Título de Gráfica
plt.title('Videojuegos mas jugados')
 
# Mostramos Gráfica
plt.show()