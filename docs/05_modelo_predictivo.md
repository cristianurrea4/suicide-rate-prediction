#### 5. `05_modelo_predictivo.md`
Aquí introduces los modelos de machine learning que utilizarás, explicando el proceso de entrenamiento y predicción.

```markdown
# Modelo Predictivo

Para predecir las tasas de suicidio, utilizamos diversos modelos de machine learning:

- **Regresión Lineal**
- **Random Forest**
- **XGBoost**
- **LightGBM**
- **CatBoost**
- **Logistic Regression**

Cada modelo fue entrenado utilizando los datos preprocesados y luego se evaluaron utilizando métricas como Recall, F1 y ROC AUC.

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)
