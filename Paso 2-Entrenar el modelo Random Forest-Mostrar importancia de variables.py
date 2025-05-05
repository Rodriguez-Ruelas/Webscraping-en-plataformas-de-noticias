"""
Entrenamiento y evaluación de un modelo Random Forest para la clasificación
del impacto de incendios forestales en México.

Autor: Raúl Rodríguez Ruelas  
Fecha: 2025-05-04  
Versión: 1.1  

Este script carga un conjunto de datos ya preprocesado, entrena un modelo de clasificación
usando Random Forest, evalúa su desempeño mediante métricas estándar, y visualiza tanto
la matriz de confusión como las variables más importantes. También incluye una visualización
exploratoria de las variables clave mediante un pairplot.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# === 1. Cargar datos ===
df = pd.read_excel("datos_para_random_forest.xlsx")

# === 2. Separar X y y ===
objetivo = "Clasificación primer orden"
X = df.drop(columns=[objetivo])
y = df[objetivo]

# === 3. Pairplot exploratorio con variables continuas ===
try:
    print("🧪 Visualización exploratoria de variables continuas (pairplot)...")
    columnas_numericas = ['Superficie', 'Latitud', 'Longitud', 'Total días / persona']
    
    df_vis = pd.concat([X[columnas_numericas], y.reset_index(drop=True)], axis=1)
    sns.pairplot(df_vis, hue=objetivo, palette='Set2')
    plt.suptitle("Distribución de variables continuas según clasificación", y=1.02)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print("⚠️ No se pudo generar el pairplot:", e)

# === 4. División de datos ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# === 5. Entrenamiento ===
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# === 6. Evaluación ===
y_pred = modelo.predict(X_test)

print("🔎 Reporte de Clasificación:")
print(classification_report(y_test, y_pred))

# === 7. Matriz de Confusión ===
print("\n📊 Matriz de Confusión:")
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicción")
plt.ylabel("Valor real")
plt.title("Matriz de Confusión")
plt.tight_layout()
plt.show()

# === 8. Importancia de Variables ===
importancias = pd.Series(modelo.feature_importances_, index=X.columns)
plt.figure(figsize=(8, 6))
importancias.sort_values(ascending=False).head(20).plot(kind='barh')
plt.gca().invert_yaxis()
plt.title("Top 20 Variables Más Importantes")
plt.xlabel("Importancia")
plt.tight_layout()
plt.show()
