
import pandas as pd
import os
from datetime import date
from datetime import datetime
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
saidi_m_np = [17.592,16.184,14.890,13.699,12.603]
saidi_li_np = [17.504, 16.104, 14.815, 13.630, 12.540]
saidi_ls_np= [17.680, 16.265, 14.964, 13.767, 12.666]


# años de aplicacion
a = [2019,2020,2021,2022,2023]
# determinamos el tamaño del graficco
fig, ax = plt.subplots(figsize=(5,4))
fig.tight_layout()

# colocando la etiqueta a los ejes
ax.set_ylabel('SAIDI[h]')
ax.set_xlabel('año')

p = ax.plot(a, saidi_m_np, marker = 'o', color='black', label='meta SAIDI_M')
#ax.bar_label(p, label_type='edge')
ax.set_title('Tendencia de la meta para el  SAIDI')
ax.plot(a, saidi_li_np, linestyle = 'dotted', label='banda de indiferencia superior')
ax.plot(a, saidi_ls_np, linestyle = 'dotted', label='banda de indiferencia superior')

# set x, y-axis limits 
ax.set_xlim(2018, 2025)
ax.set_ylim(10, 20)

# se establece el formato para el eje x
ax.xaxis.set_minor_formatter(FormatStrFormatter('% 1.0f'))

# coloca la etiqueta sobre cada punto de la grafica
for x,y,text in zip(a, saidi_m_np, saidi_m_np):
   plt.text(x+0.01,y+0.05,text)

plt.legend(loc="lower left")

#muestro el grafico
plt.show()
    
