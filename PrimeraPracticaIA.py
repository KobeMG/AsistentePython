# librerias para leer y manipular datos
import pandas as pd
# librerias para machine learning
#librerias para graficas
from matplotlib import style
style.use("ggplot")


# los datos se cargaran en variable
df_original = pd.read_csv("train.csv")
# print(df_original.head(3))


# eliminar las columnas irrelevantes...
df_dropped_features = df_original.drop(["PassengerId","Name","Embarked","Parch","Cabin"], axis = 1)
print(df_dropped_features.head(3))
print("")
# ver los difgerentes valores que puede tener la variable
# print("Sex: ", df_dropped_features["Sex"].unique())

# categorizar los diferentes features
df_categorized = pd.get_dummies(df_dropped_features)
print(df_categorized.head(3))