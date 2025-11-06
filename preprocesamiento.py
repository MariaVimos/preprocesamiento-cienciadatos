import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def preprocesar_datos(ruta_csv):
    # Leer dataset
    df = pd.read_csv(ruta_csv)
    print("Datos :", df.shape)

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Rellenar valores nulos numéricos con la media
    df = df.fillna(df.mean(numeric_only=True))

    # Normalizar columnas numéricas
    scaler = MinMaxScaler()
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
    df[columnas_numericas] = scaler.fit_transform(df[columnas_numericas])

    # Codificar variables categóricas
    encoder = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = encoder.fit_transform(df[col])

    print("Datos procesados:", df.shape)
    return df

if __name__ == "__main__":
    
    # Ejemplo 
    df = preprocesar_datos("datos.csv")
    df.to_csv("datos_procesados.csv", index=False)
