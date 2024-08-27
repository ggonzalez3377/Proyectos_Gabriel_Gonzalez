# Finance Proyects
Este repositorio contiene los principales proyectos desarrollados por Gabriel Gonzalez a traves de Python, y para una mejor visualizacion a traves del entorno de ejecucion de Jupyter

## 0). Python Basics
El cuaderno de Jupyter proporciona una introducción a Python, cubriendo variables, tipos de datos, operadores, entrada y salida de datos, y funciones integradas. También incluye ejemplos de programación orientada a objetos, abordando clases, herencia, polimorfismo, encapsulamiento y decoradores. Además, presenta ejercicios prácticos y conceptos fundamentales, lo que lo convierte en un recurso completo para principiantes en Python.

## 1). Trading Signals
El código "Algorithmic_Trading.ipynb" obtiene datos históricos de precios de acciones, aplica una estrategia de cruce de medias móviles para generar señales de compra y venta, y realiza backtesting para evaluar el rendimiento. En el backtesting, se calculan métricas clave como el win rate, Sharpe Ratio, Sortino Ratio y Calmar Ratio. Además, realiza un seguimiento de las posiciones en un DataFrame para monitorizar ganancias o pérdidas, y visualiza los resultados mediante gráficos para analizar la efectividad de la estrategia.

## 2). Stochastics Process Modeling
Code in progress...

## 3). Markowitz Portfolio
El código optimiza carteras de inversión usando el modelo de Markowitz a través de dos metodologías:
1. **Simulación de Montecarlo:** Genera múltiples portafolios aleatorios para construir la frontera eficiente, calculando sus rendimientos y riesgos para identificar la mejor combinación de activos.
2. **Optimización con `scipy`:** Utiliza técnicas de optimización para encontrar la cartera óptima que maximiza el Sharpe Ratio o minimiza el riesgo para un nivel de rentabilidad objetivo.
Además, realiza un seguimiento de las posiciones en un DataFrame para evaluar ganancias y pérdidas, calcula métricas clave como el Sharpe Ratio, Sortino Ratio, Calmar Ratio y win rate, y visualiza los resultados con gráficos para facilitar el análisis de la efectividad de las carteras.

## 4). Fama French Factors
El cuaderno de Jupyter se centra en el análisis de datos financieros utilizando el modelo de Fama y French. Descarga datos desde el sitio web de Fama y French, los descomprime y almacena en Google Drive. Luego, los datos se limpian y formatean para su análisis. El cuaderno también se conecta a Google Sheets para obtener datos adicionales y formatearlos adecuadamente. Finalmente, se realizan análisis y gráficos, incluyendo la comparación de fronteras eficientes de diferentes índices, mostrando desviaciones estándar y retornos esperados.

## 5). Options Valuation
Code in progress...

## 6). Firm Valuation
El cuaderno de Jupyter se enfoca en la valoración de empresas utilizando el Modelo de Descuento de Dividendos (DDM). Importa la librería Pandas y define variables clave como el retorno sobre el patrimonio (ROE), la tasa de retención de utilidades (Plowback), el capital inicial y la tasa de descuento. Se incluyen funciones para calcular y retornar un DataFrame con los detalles anuales de capital, utilidades, dividendos y capital acumulado durante 500 años, así como para calcular el valor presente de los dividendos descontados y determinar el valor de las acciones.

## 7). Bonds Analizer
El proyecto "Bonds_Analizer" es una herramienta de análisis financiero de bonos. Utiliza Python en un entorno Jupyter Notebook para calcular y visualizar métricas clave como precio, duración y rendimiento de bonos. Emplea bibliotecas como pandas y matplotlib para el manejo y representación de datos, permitiendo a los usuarios evaluar el desempeño y las características de sus inversiones en bonos de manera efectiva y precisa.

## 7). Stocks_Portfolio
El proyecto proporciona una herramienta avanzada para la optimización de carteras de acciones, utilizando datos históricos para calcular rentabilidades, riesgos y construir la frontera eficiente de un portafolio. Mediante técnicas estadísticas y de programación en Python, se evalúan diferentes combinaciones de activos para maximizar el rendimiento ajustado al riesgo. El proyecto facilita la identificación del portafolio óptimo con el mayor Sharpe ratio y el mínimo riesgo, permitiendo a los inversores tomar decisiones informadas para mejorar su rendimiento financiero, teniendo en cuenta tambien movimientos de las tasas cambiarias lo cual es un riesgo al que se expone un portafolio y de que manera estos movimientos afectan (excenso de contribucion) en ultima medida al rendimietno del portafolio.
