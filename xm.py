# Importación
from pydataxm.pydatasimem import ReadSIMEM, CatalogSIMEM

# Buscar el id del conjunto de datos
catalogo = CatalogSIMEM('Datasets')
data_catalogo = catalogo.get_data()
print(data_catalogo.query("nombreConjuntoDatos.str.contains('Generación Real')"))

# Crear una instancia de ReadSIMEM
dataset_id = 'E17D25'
fecha_inicio = '2024-04-01'
fecha_fin = '2024-04-30'
generacion = ReadSIMEM(dataset_id, fecha_inicio, fecha_fin)

# Recuperar datos
data = generacion.main(filter=False)
print(data)
