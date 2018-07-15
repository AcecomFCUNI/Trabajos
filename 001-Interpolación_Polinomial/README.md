# Interpolación polinomial
## @autor: Luis Vasquez Espinoza

### Resumen
Esta investigación se centró en el estudio e implementación de 3 métodos de interpolación de señales
bidimensionales: Nearest Neighbour, Bilineal y Bicúbica. Mediante estos técnicas numéricas se busca
estimar los valores internos no existentes en un inicio luego de redimensionar una señal (representada como una matriz en el código).

### Dependencias
Las versiones de las librerías listadas a continuación son referenciales, puede que el códgio corra con versiones anteriores, probar antes de actualizar

* python 3.*
* numpy 1.14.5
* matplotlib 2.2.2

### Instrucciones
Para ver el resultado inmediato del proyecto navegar dentro de la carpeta del mismo y hacer
```python
python3 main.py
```

Si se desea jugar con los valores de la matriz usada o las escalas de redimensionamientos, modificar solor el archivo _main.py_, los otros archivos son las librerias de calculo numérico y ploteo

### Referencias
* W.H. Press, S.A. Teukolsky, W.T. Vetterling, W.P. Flannery, Numerical Recipes in C: The Art of Scientific Computing (1992) pg.123-127.

* W.Burger,M.Burge,Digital Image Processing:An Algo-
rithmic introduction using Java (2008) pg.392.

### Imágenes
![alt text](https://i.imgur.com/Co0QmHm.png "Interpolación por NN")
![alt text](https://i.imgur.com/JRQtqvI.png "Interpolación Bilineal")
![alt text](https://i.imgur.com/zN2EBzK.png "Interpolación Bicúbica")