# Archivo para la realización de gráficas
# a partir de series de datos

import pandas as pd
import os
from datetime import date
from datetime import datetime
from sklearn.linear_model import LinearRegression
#import plotly.express as px
#import plotly.graph_objects as go
import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator,
                               FormatStrFormatter,
                               AutoMinorLocator)

# directorio en donde se encuentran los archivos a remplazar
ph = os.path.abspath(os.getcwd())
#metas del saidi
semi_aislado_132 = {'2':184, '1/0':241, '4/0': 355, '266.8-250':458, '336.8-350':530}
xlpe_al =  {'2':120, '1/0':155, '4/0':230, '266.8-250':250, '336.8-350':305, '500':370, '750':470}
xlpe_cu =  {'2':155, '1/0':200, '4/0':295, '266.8-250':325, '336.8-350':390, '500':465, '750':585}
mm = {'2':33.62, '1/0':53.5, '4/0':107.21, '266.8-250':135.1, '336.8-350':170.3, '500':254, '750':380}

corriente = list(semi_aislado_132.values())
conductor = list(semi_aislado_132.keys())
a = list(range(0,len(semi_aislado_132)))


# determinamos el tamaño del graficco
fig, ax = plt.subplots(figsize=(5,4))
fig.tight_layout()

# colocando la etiqueta a los ejes
ax.set_ylabel('corriente [A]')
ax.set_xlabel('Conductor')

p = ax.plot(conductor, corriente, marker = 'd', color='black', label='red semi aislada')
#ax.bar_label(p, label_type='edge')
ax.set_title('Capacidad de corriente de los conductores')
#ax.plot(a, saidi_li_np, linestyle = 'dotted', label='banda de indiferencia superior')
#ax.plot(a, saidi_ls_np, linestyle = 'dotted', label='banda de indiferencia superior')

# set x, y-axis limits 
#ax.set_xlim(2018, 2025)
ax.set_ylim(0, 700)

# se establece el formato para el eje x
ax.xaxis.set_minor_formatter(FormatStrFormatter('% 1.0f'))

# coloca la etiqueta sobre cada punto de la grafica
for x,y,text in zip(a, corriente, corriente):
   plt.text(x-0.1,y+10,text)

############################################################
   
# datos para la capacidad de corriente xlpe_al
corriente = list(xlpe_al.values())
conductor = list(xlpe_al.keys())
a = list(range(0,len(xlpe_al)))

ax.plot(conductor, corriente, marker = 'o', color='red', label='xlpe_al')

# coloca la etiqueta sobre cada punto de la grafica
for x,y,text in zip(a, corriente, corriente):
   plt.text(x-0.1,y+10,text)

###############################################################

# datos para la capacidad de corriente xlpe_al
corriente = list(xlpe_cu.values())
conductor = list(xlpe_cu.keys())
a = list(range(0,len(xlpe_cu)))

ax.plot(conductor, corriente, marker = 'o', color='green', label='xlpe_cu')

# coloca la etiqueta sobre cada punto de la grafica
for x,y,text in zip(a, corriente, corriente):
   plt.text(x-0.1,y+10,text)
###############################################################

# datos para los milimetros de cobre
corriente = list(mm.values())
conductor = list(mm.keys())
a = list(range(0,len(mm)))

ax.plot(conductor, corriente, marker = 's', color='blue', label='mm2')

# coloca la etiqueta sobre cada punto de la grafica
for x,y,text in zip(a, corriente, corriente):
   plt.text(x-0.1,y+15,text)

plt.legend(loc="lower right")

#muestro el grafico
plt.show()
    
