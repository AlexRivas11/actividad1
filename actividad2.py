# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

estaciones = pd.read_csv('estaciones_bici.csv', sep=";", index_col=0)

# print(estaciones)

totales = estaciones[estaciones["total"] == 30]
# totales = totales["estation"]
# totales.plot()

# print(totales.estation.drop_duplicates().shape)
estations = totales.estation.drop_duplicates()
# print(estations.count())

# print(estaciones)

medias = estaciones[["available", "estation", "download_date"]]
aux = 0
data_estation_max_mediun = medias[medias["estation"].isin([1])]
estation_max_mediun = 0
for i in medias.estation.drop_duplicates():
    media = medias[medias["estation"].isin([i])].median()
    # print("Estacion: ", i, " Media: ", media.available)
    if media.available>aux:
        aux = media.available
        estation_max_mediun = media.estation
        data_estation_max_mediun = medias[medias["estation"].isin([i])]

# print("Estacion: ", estation_max_mediun, " Media: ", aux)
data_estation_max_mediun.hist(column="available")




plt.show()