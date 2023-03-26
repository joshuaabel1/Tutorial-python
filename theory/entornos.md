## Entornos virtuales:

__Un entorno virtual en Python es un ambiente aislado que permite la instalación y uso de paquetes y versiones específicas de Python sin interferir con otras instalaciones de Python y sus paquetes.__

__Los entornos virtuales son útiles para proyectos en los que se requiere utilizar diferentes versiones de paquetes o para evitar conflictos entre versiones de paquetes en diferentes proyectos.__

__Para crear un entorno virtual en Python, se utiliza la herramienta venv (disponible en Python 3.x) que viene incluida con la instalación de Python. El comando venv crea una carpeta que contiene todo lo necesario para el entorno virtual, incluyendo una copia del intérprete de Python y los paquetes necesarios.__

__Aquí te muestro los pasos para crear y utilizar un entorno virtual en Python:__


1) __Abre una terminal o línea de comandos y navega a la carpeta donde deseas crear el entorno virtual.__
2) __Crea el entorno virtual utilizando el siguiente comando.__
``` bash
python -m venv nombre_del_entorno_virtual
```
__Donde nombre_del_entorno_virtual es el nombre que deseas asignar al entorno virtual.__

3) __Activa el entorno virtual con el siguiente comando:__

- En Windows:
``` bash
  nombre_del_entorno_virtual\Scripts\activate.bat
```


- En Linux/Mac:
  ``` bash
  source nombre_del_entorno_virtual/bin/activate
  ```

1) __Una vez activado el entorno virtual, cualquier paquete que se instale utilizando pip se instalará solo en ese entorno virtual, y no interferirá con otros entornos virtuales o instalaciones de Python.__
2) __Para desactivar el entorno virtual, simplemente utiliza el comando deactivate.__

__En resumen, los entornos virtuales en Python son ambientes aislados que permiten la instalación y uso de paquetes y versiones específicas de Python sin interferir con otras instalaciones de Python y sus paquetes. Se crean utilizando la herramienta venv y se activan y desactivan utilizando comandos específicos en la línea de comandos.__

__En Python existen varias herramientas para administrar paquetes y dependencias de proyectos:__

### Administradoras de paquetes python:

1) __pip: Es el administrador de paquetes estándar para Python. Se utiliza para instalar y desinstalar paquetes, y también para actualizarlos. Pip permite la instalación de paquetes desde repositorios públicos o privados y también permite la instalación de paquetes desde archivos de distribución.__

2) __conda: Es un administrador de paquetes y entornos virtuales que se enfoca en el análisis de datos, la ciencia y el aprendizaje automático. Conda permite la creación de entornos virtuales con paquetes específicos y la instalación de paquetes desde diferentes fuentes.__

3) __PyPI: Es el repositorio oficial de paquetes de Python. Se puede acceder a través de la herramienta pip para instalar paquetes directamente desde el repositorio. PyPI es un repositorio público, por lo que cualquier persona puede publicar un paquete.__

4) __Anaconda: Es una distribución de Python que incluye un conjunto de paquetes comunes utilizados en el análisis de datos, la ciencia y el aprendizaje automático. Además de los paquetes, Anaconda también incluye la herramienta conda para la gestión de paquetes y entornos virtuales.__

5) __pipenv: Es una herramienta de administración de dependencias que combina pip y virtualenv. Pipenv se utiliza para crear y administrar entornos virtuales y para manejar las dependencias del proyecto. Pipenv también gestiona la seguridad de las dependencias y asegura que las versiones de los paquetes sean compatibles.__