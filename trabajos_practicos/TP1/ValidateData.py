import pandas as pd
def validar_columnas(df):
    validacion_df = pd.DataFrame(columns=['columna', 'valores_unicos', 'n_valores_unicos', 'cantidad_de_nulos_de_col.'])
    for col in df.columns:
        n_valores_unicos = df[col].nunique()
        cantidad_de_nulos_de_col = df[col].isnull().sum()
        porcentaje_de_valores_nulos = (cantidad_de_nulos_de_col / len(df)) * 100
        validacion_df = validacion_df.append({
            'Column': col,
            'valores_unicos': df[col].unique(),
            'n_valores_unicos': n_valores_unicos,
            'cantidad_de_nulos_de_col.': cantidad_de_nulos_de_col,
            '%_Null_Values': porcentaje_de_valores_nulos
        }, ignore_index=True)

    return validacion_df