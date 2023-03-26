## Github:


__GitHub es una plataforma web para alojar y gestionar proyectos de software utilizando el sistema de control de versiones Git. GitHub permite a los desarrolladores trabajar en equipo, compartir su código y colaborar en proyectos de software de manera efectiva.__

__El proceso básico de trabajo en GitHub es el siguiente:__

1) __Crear una cuenta de usuario en GitHub.__

2) __Crear un nuevo repositorio de Git en GitHub.__

3) __Clonar el repositorio en una máquina local.__

4) __Añadir, editar o eliminar archivos en la copia local del repositorio.__

5) __Hacer un commit de los cambios en la rama local.__

6) __Hacer un push de la rama local al repositorio remoto en GitHub.__

7) __Crear una pull request para solicitar que los cambios se integren en la rama principal del repositorio.__

8) __Revisar y discutir los cambios con otros colaboradores.__

9) __Fusionar la pull request en la rama principal del repositorio si los cambios son aceptados.__

__Además de alojar y gestionar proyectos de software, GitHub también ofrece una serie de herramientas y servicios adicionales, como seguimiento de problemas, solicitudes de funciones, integración continua y despliegue automático.__

Comandos básicos:
``` bash
git add .: Agrega todos los cambios realizados en el directorio actual para ser incluidos en el próximo commit.
git commit -m “comentario”: Crea un nuevo commit con los cambios agregados con git add y con el comentario proporcionado.
git push: Sube los cambios al repositorio remoto.
```
Comandos para trabajar con ramas:
``` bash
git status: Muestra el estado actual del repositorio, incluyendo la rama actual.
git checkout <nombre de la rama>: Cambia a la rama especificada.
git checkout -b <nombre de la rama>: Crea una nueva rama y cambia a ella.
git branch <nombre de la rama>: Crea una nueva rama.
git branch --list: Lista todas las ramas en el repositorio local.
git branch -d <nombre de la rama>: Borra la rama especificada.
git pull: Actualiza la rama actual con los cambios del repositorio remoto.
git merge <nombre de la rama>: Fusiona la rama especificada con la rama actual.
```
Comando para deshacer cambios:
``` bash
git revert <código del commit>: Crea un nuevo commit que deshace los cambios realizados en el commit especificado.
```
Comandos para guardar cambios temporalmente:
``` bash
git stash save "nombre del stash": Guarda temporalmente los cambios que aún no se han confirmado.
git stash list: Muestra la lista de todos los stashes guardados.
git checkout <nombre de la rama>: Cambia a otra rama.
git stash apply: Aplica los cambios guardados en el último stash.
```