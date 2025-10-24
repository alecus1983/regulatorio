import matplotlib.pyplot as plt

# --- 1. Datos extraídos de la tabla ---

# Eje X (Abscisas): Etiquetas de Tensión Nominal (Categorías)
labels_tension = [
    "hasta 1",
    "7,6/11,4/13,2/13,8",
    "33/34,5",
    "44",
    "57,5/66",
    "110/115",
    "220/230",
    "500"
]

# Eje Y (Ordenadas): Valores de Distancia mínima (m)
distancia_m = [0.80, 0.95, 1.10, 1.20, 1.40, 1.80, 2.8, 5.5]

# --- 2. Creación del gráfico de barras ---

# Definir un tamaño para la figura (ancho, alto)
plt.figure(figsize=(10, 7))

# Crear el gráfico de barras y guardar los objetos 'bars'
bars = plt.bar(labels_tension, distancia_m, color='skyblue')

# --- 3. AÑADIR ETIQUETAS A CADA BARRA ---
# Iteramos sobre cada objeto 'bar' devuelto por plt.bar()
for bar in bars:
    # Obtenemos la altura de la barra (valor Y)
    yval = bar.get_height()
    
    # Usamos plt.text() para poner el texto
    plt.text(
        bar.get_x() + bar.get_width()/2.0,  # Posición X (en el centro de la barra)
        yval,                               # Posición Y (en la parte superior de la barra)
        f'{yval:.2f} m',                    # El texto a mostrar (valor con 2 decimales y "m")
        va='bottom',                        # Alineación vertical (bottom = justo encima)
        ha='center',                        # Alineación horizontal (centrada)
        fontsize=9
    )

# --- 4. Añadir etiquetas y títulos ---

# Etiqueta del eje X (Abscisas)
plt.xlabel('Tensión nominal entre fases (kV)')

# Etiqueta del eje Y (Ordenadas)
plt.ylabel('Distancia mínima (m)')

# Título principal del gráfico
plt.title('Distancias mínimas de seguridad para trabajos cerca a redes y líneas energizadas')

# Rotar las etiquetas del eje X para que no se superpongan
plt.xticks(rotation=45, ha='right', fontsize=9)

# Añadir una rejilla (cuadrícula) en el eje Y para mejor lectura
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Dar un poco más de espacio en el eje Y para que la etiqueta más alta quepa
# Obtenemos el límite actual y lo aumentamos un 10%
plt.ylim(0, max(distancia_m) * 1.1) 

# Ajustar el layout para asegurar que todo quepa
plt.tight_layout()

# Mostrar el gráfico
plt.show()
