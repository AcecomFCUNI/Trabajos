# Trabajos

El presente repositorio agrupará los trabajos de investigación desarrollados por los miembros de ACECOM.

## Formato

Toda publicación de investigación en este repositorio seguirá las siguientes etapas:

* Si el miembro que desea publicar su investigación no tiene acceso como editor al repositorio, deberá solicitarlo al siguiente correo: acecom@uni.edu.pe. El asunto del correo deberá ser "solic. de publicación github" (sin las comillas). En este correo se le proporcionará un número **id** para que publique su trabajo.
* Una vez en github (en este mismo repositorio) deberá crear una carpeta con la estructura [id]-[Nombre del proyecto]. Por ejemplo, si su proyecto se llama **implementación de cimulazion de fluiiidos** y la id proporcionada en el correo es **037**, la carpeta deberá llamarse **037-Implementación de simulación de fluidos** respetando la ortografía adecuada, el cero explícito de la id y el guión entre la id y el nombre con mayúscula al principio
* A continuación deberá hacer dos cosas: Soltar la carpeta del proyecto dentro de la creada hace un instante y generar un readme en markdown

La estructura de su proyecto entonces quedaría así:

```
/
|--- 037-Implementación de simulación de fluidos (carpeta obligatoria)
		|--- implementación de cimulazion de fluiiidos (carpeta de proyecto)
			|--- main.py
			|--- fluidos.py
			|--- otra_carpeta
				|--- mas_cosas.txt
			|--- config.txt
			|--- etcétera.txt
		|--- README.md (archivo markdown obligatorio)
```

El archivo README.md debe tener los siguientes apartados:

```markdown
# Título del proyecto
## @autor: Su_nombre_completo_aquí

### Resumen
Breve descripción del proyecto investigado

### Dependencias
Lista de paquetes, programas, lenguajes y herramientas utilizadas  y necesarias para replicar el proyecto de manera local
ej:

* python 3.5
* numpy 5.8.2
* matplotlib 5.5.2

### Instrucciones
Instrucciones de uso para que, una vez con las dependencias instaladas, se pueda ejecutar el programa
ej:

* Ingresar al terminal
* Hacer python3 main.py

### Referencias
Enlaces a libros, papers, videos y páginas externas usadas en la elaboración del proyecto

### Imágenes
Imágenes de los procesos y/o resultados del proyecto que ilustren y llamen la atención
```

### Nota:

* El **README.md** debe llamarse tal cual para que github lo presente formateado correctamente
* Si usted no se siente en la confianza de utilizar git o github para publicar su proyecto, contacte el mismo correo adjuntando su REAME.md y proyecto comprimido en .zip .rar o similar
