import pandas as pd

data = {
    "oblast": ["Donets'k", "Dnipropetrovs'k", 'Kiev City', 'Kharkiv', "L'viv", 'Odessa',
               "Luhans'k", 'Crimea', 'Zaporizhzhya', 'Kiev', 'Vinnytsya', 'Poltava',
               "Ivano-Frankivs'k", "Khmel'nyts'kyy", 'Transcarpathia', 'Zhytomyr',
               'Cherkasy', 'Rivne', 'Mykolayiv', 'Sumy', "Ternopil'", 'Kherson',
               'Chernihiv', 'Volyn', 'Kirovohrad', 'Chernivtsi', 'Sevastopol'],
    
    # Características ficticias: área (km²), densidad de población (hab/km²)
    "area_km2": [26517, 31923, 839, 31415, 21833, 33310, 26684, 27000, 27183, 28131, 
                 26513, 28748, 13928, 20629, 12777, 29832, 20900, 20047, 24598, 23834,
                 13852, 28461, 31900, 20143, 23923, 13090, 1079],
    
    "population_density": [165, 102, 3457, 86, 116, 72, 85, 73, 65, 61, 60, 50, 100, 
                           90, 92, 82, 60, 59, 47, 46, 78, 41, 33, 52, 40, 70, 480],
    
    # Población total de cada oblast (etiquetas que queremos predecir)
    "population": [4387702, 3258705, 2900920, 2720342, 2535476, 2387282, 2263676,
                   1963770, 1755663, 1731673, 1604270, 1440684, 1382721, 1296103,
                   1259497, 1249225, 1246166, 1162049, 1159634, 1115051, 1066523,
                   1063803, 1047023, 1042855, 974724, 910001, 509992]
}

df = pd.DataFrame(data)
