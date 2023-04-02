## Github:

**GitHub es una plataforma web para alojar y gestionar proyectos de software utilizando el sistema de control de versiones Git. GitHub permite a los desarrolladores trabajar en equipo, compartir su código y colaborar en proyectos de software de manera efectiva.**

**El proceso básico de trabajo en GitHub es el siguiente:**

1. **Crear una cuenta de usuario en GitHub.**

2. **Crear un nuevo repositorio de Git en GitHub.**

3. **Clonar el repositorio en una máquina local.**

4. **Añadir, editar o eliminar archivos en la copia local del repositorio.**

5. **Hacer un commit de los cambios en la rama local.**

6. **Hacer un push de la rama local al repositorio remoto en GitHub.**

7. **Crear una pull request para solicitar que los cambios se integren en la rama principal del repositorio.**

8. **Revisar y discutir los cambios con otros colaboradores.**

9. **Fusionar la pull request en la rama principal del repositorio si los cambios son aceptados.**

**Además de alojar y gestionar proyectos de software, GitHub también ofrece una serie de herramientas y servicios adicionales, como seguimiento de problemas, solicitudes de funciones, integración continua y despliegue automático.**

### Comandos básicos:

```bash
git add .: Agrega todos los cambios realizados en el directorio actual para ser incluidos en el próximo commit.
git commit -m “comentario”: Crea un nuevo commit con los cambios agregados con git add y con el comentario proporcionado.
git push <nombre del origen remoto> <nombre de rama remota>: Sube los cambios al repositorio remoto.
```

### Comandos para trabajar con ramas:

```bash
git status: Muestra el estado actual del repositorio, incluyendo la rama actual.
git checkout <nombre de la rama>: Cambia a la rama especificada.
git checkout -b <nombre de la rama>: Crea una nueva rama y cambia a ella.
git branch <nombre de la rama>: Crea una nueva rama.
git branch --list: Lista todas las ramas en el repositorio local.
git branch -d <nombre de la rama>: Borra la rama especificada.
git pull: Actualiza la rama actual con los cambios del repositorio remoto.
git merge <nombre de la rama>: Fusiona la rama especificada con la rama actual.
```

### Comando para deshacer cambios:

```bash
git revert <código del commit>: Crea un nuevo commit que deshace los cambios realizados en el commit especificado.
```

Comandos para guardar cambios temporalmente:

```bash
git stash save "nombre del stash": Guarda temporalmente los cambios que aún no se han confirmado.
git stash list: Muestra la lista de todos los stashes guardados.
git checkout <nombre de la rama>: Cambia a otra rama.
git stash apply: Aplica los cambios guardados en el último stash.
```

### Documento recomendado 📓

[Cheatsheet](https://training.github.com/downloads/es_ES/github-git-cheat-sheet.pdf)
