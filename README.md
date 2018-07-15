# Trabajos

El presente repositorio agrupará los trabajos de investigación desarrollados por los miembros de ACECOM.

## Formato

Toda publicación de investigación en este repositorio seguirá las siguientes etapas:

* Si el miembro que desea publicar su investigación no tiene acceso como editor al repositorio, deberá solicitarlo al siguiente correo: acecom@uni.edu.pe. El asunto del correo deberá ser __solic. de publicación github__. En respuesta a este correo se le proporcionará un número **id** para que publique su trabajo.
* Una vez con el **id** el miembro debe crear un **fork** del presente repositorio, esto copiará una versión del presente repo. en su cuenta, llamado _https://github.com/[NOMBRE_DE_USUARIO]/Trabajos_, **único lugar** donde se procederá a incluir su proyecto como sigue:
	* Deberá crear una carpeta con la estructura [id]-[Nombre del proyecto]. Por ejemplo, si su proyecto se llama **implementación de cimulazion de fluiiidos** y la id proporcionada en el correo es **037**, la carpeta deberá llamarse **037-Implementación_de_simulación_de_fluidos** respetando la ortografía adecuada, el cero explícito de la id, las palabras separadas por underscore ('\_') y el guión entre la id y el nombre con mayúscula al principio
	* A continuación deberá hacer dos cosas: Soltar la carpeta del proyecto dentro de la creada hace un instante y generar un readme en markdown

La estructura de su proyecto entonces quedaría así:

```
/---------------------------------------------------
/ En https://github.com/[NOMBRE_DE_USUARIO]/Trabajos
/---------------------------------------------------

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
## Fecha: AÑO/MES/DIA

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

* Finalmente, una vez se incluyó todo el contenido de su proyecto a publicar de manera adecuada deberá solicitar el merge. Si todo está en orden uno de nuestros miembros administradores aceptará su proyecto y quedará archivado en este repositorio

### Nota:

* El **README.md** debe llamarse tal cual para que github lo presente formateado correctamente
* Puede usar [este](https://help.github.com/articles/fork-a-repo/) enlace para informarse de como forkear un repo; note que el proceso es tan simple como darle click a fork, añadir los cambios ya sea en el mismo github o desde su propia pc con git, commitear los cambios y solicitar el merge.
