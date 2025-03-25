#### 4. `04_visualizaciones.md`
Describe las visualizaciones realizadas, como gráficos de líneas para mostrar tendencias de suicidio.

```markdown
# Visualizaciones

Una de las primeras visualizaciones fue un gráfico de línea que muestra la evolución del número de suicidios por año:

```python
import seaborn as sns
plt.figure(figsize=(10,6))
sns.lineplot(data=data, x='year', y='suicides_no')
plt.title('Número de suicidios por año')
plt.savefig('./output/suicide_plot.png')
plt.show()
