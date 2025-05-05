"""
Limpieza, transformación y codificación de una base de datos de incendios forestales en México
para su uso en modelos de clasificación (Random Forest).

Autor: Raúl Rodríguez Ruelas
Fecha: 2025-05-04
Versión: 1.0
Descripción: Este script realiza la carga de un archivo Excel, limpieza de datos,
codificación de variables categóricas mediante One-Hot Encoding, y guarda el conjunto listo 
para análisis predictivo.
"""

import pandas as pd
import numpy as np

# === 1. Cargar archivo ===
# El encabezado real se encuentra en la segunda fila del archivo
df = pd.read_excel("Incendios concentrado.xlsx", header=1)

# === 2. Eliminar registros sin clasificación ===
objetivo = "Clasificación primer orden"
df = df[df[objetivo].notna()]

# === 3. Imputar y convertir columnas categóricas ===
cat_fill_cols = [
    'Área natural protegida', 'Tipo vegetación', 'Posible causa',
    'Tipo de atención', 'Estado', 'Municipio'
]
for col in cat_fill_cols:
    df[col] = df[col].fillna("No especificado").astype(str)

# === 4. Conversión segura de columnas numéricas ===
num_cols = ['Superficie', 'Total días / persona', 'Latitud', 'Longitud']
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Eliminar filas con valores nulos en columnas clave
df = df.dropna(subset=num_cols)

# === 5. Codificación One-Hot para variables categóricas ===
columnas_categoricas = [
    'Estado', 'Municipio', 'Posible causa',
    'Tipo vegetación', 'Área natural protegida',
    'Tipo de atención'
]
df_encoded = pd.get_dummies(df, columns=columnas_categoricas, drop_first=True)

# === 6. Separar variables predictoras (X) y objetivo (y) ===
X = df_encoded.drop(columns=[objetivo])
y = df[objetivo].astype(str)

# === 7. Combinar y exportar ===
df_final = pd.concat([X, y.reset_index(drop=True)], axis=1)

# Forzar consistencia de tipos
for col in df_final.columns:
    if df_final[col].dtype == 'object':
        df_final[col] = df_final[col].astype(str)

# Guardar como Excel limpio para modelado
df_final.to_excel("datos_para_random_forest.xlsx", index=False, engine="openpyxl")

print("✅ Archivo limpio y válido guardado como 'datos_para_random_forest.xlsx'")
