#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA = ['libcrd14', 'mar76']

CATEGORICAL_VARS_WITH_NA_FREQ = ['libcrd14', 'mar76']

#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = ['iqscore', 'kww']

#Varibles para transformación logaritmia
NUMERICALS_LOG_VARS = ["lwage76"]

#Variables para hacer mapeo categorico 
BINARY_VARS =  ['smsa66', 'smsa76', 'nearc2', 'nearc4', 'nearc4a', 'nearc4b', 'nodaded', 'nomomed', 'momdad14', 'sinmom14',
                'step14', 'south66', 'south76', 'black', 'enroll76', 'libcrd14']
MAR_VARS = ['mar76']

#Mapeos de variables categoricas
BINARY_MAP = {'no': 0, 'yes': 1, 'nan': 0, 'Nan': 0}

MAR_MAP = {'nan': 0, 'Nan': 0, 'no': 0, 'yes': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}

#Variables seleccionadas según análisis de Lasso
FEATURES = ['smsa66', 'smsa76', 'nearc2', 'nearc4', 'nearc4a', 'nearc4b', 'ed76', 'ed66',
       'age76', 'daded', 'nodaded', 'momed', 'nomomed', 'momdad14', 'sinmom14',
       'step14', 'south66', 'south76', 'lwage76', 'famed', 'black', 'enroll76',
       'kww', 'iqscore', 'mar76', 'libcrd14', 'exp76']