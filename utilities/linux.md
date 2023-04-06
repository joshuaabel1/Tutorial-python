## Comandos basicos de linux 🐧

### Navegación y manipulación de directorios 📁

```bash
$ ls # lista el contenido del directorio actual
```

![ls](https://i.imgur.com/cMWvDll.png)

```bash
$ pwd # muestra la ruta del directorio actual
```

![pwd](https://i.imgur.com/p2BFhgZ.png)

```bash
$ cd <directorio>: cambia al directorio deseado
```

![cd](https://i.imgur.com/bgFK9Yo.png)

```bash
$ cp <archivo> <ruta> # copia archivos
```

![cp](https://i.imgur.com/NP3LWMq.png)

```bash
$ cp -r <carpeta> <ruta> # copia archivos y carpetas recursivamente
```

![cp](https://i.imgur.com/N5P9mln.png)

```bash
$ rm <archivo> # elimina archivos
```

![rm](https://i.imgur.com/oAvoBXh.png)

```bash
$ rm -rf # elimina archivos y carpetas de forma recursiva y forzadamente
```

![rm-rf](https://i.imgur.com/80MyHgT.png)

```bash
$ mv # mueve o renombra archivos o directorios
```

![mv](https://i.imgur.com/rYQfUeg.png)

```bash
$ mkdir# crea un nuevo directorio
```

![mkdir](https://i.imgur.com/sWmTPA2.png)

### Gestión de archivos y permisos 📂

```bash
$ touch <nombre-del-archivo> # crea un nuevo archivo vacío
$ chmod <permisos> <archivo> # cambia los permisos de los archivos
$ shred # sobrescribe un archivo para ocultar su contenido
```

### Gestión de procesos y recursos del sistema 🖥️

```bash
$ htop # muestra información sobre los procesos y los recursos del sistema
$ ps # informa sobre el estado de los procesos del shell
$ kill # termina los programas
```

### Gestión de paquetes 📦

Como manejadores de paquetes posiblemente empecemos utilizando `apt` que es parte de las distribuciones basadas en debian, como ubuntu, mint, etc. Pero en el caso de las distribuciones basadas en red hat, como fedora, centos, etc. utilizaremos `yum`.

```bash
$ apt update # actualiza la lista de paquetes disponibles
$ apt upgrade # actualiza los paquetes instalados
$ apt install <paquete> # instala un paquete
$ apt remove <paquete> # elimina un paquete
$ apt autoremove # elimina los paquetes que ya no son necesarios
$ apt search <paquete> # busca un paquete
$ apt show <paquete> # muestra información sobre un paquete
```

### Interacción con el sistema 🖥️

```bash
$ sudo <comando> # ejecuta el siguiente comando como superusuario
$ sudo !! # ejecuta el último comando como superusuario
$ shutdown <tiempo-en-milisegundos> # apaga la máquina
$ exit # sale de la sesión actual del shell
$ passwd # cambia la contraseña del usuario
$ history # muestra una lista de comandos utilizados
$ which <programa> # devuelve la ruta binaria completa de un programa
$ uname -a # muestra información sobre el sistema operativo
```

### Comunicación y conectividad 📡

```bash
$ ping <url> # comprueba la conectividad con un host
$ wget <url> # descarga archivos desde la web
```

### Edición de texto 📝

Estos editores de texto vienen instalados por defecto y son muy útiles para editar archivos de configuración.

```bash
$ vi <archivo> # abre el archivo en el editor de texto vim
$ nano <archivo> # abre el archivo en el editor de texto nano
```

### Visualización de archivos y datos 📊

```bash
$ cat <archivo> # muestra el contenido de un archivo
$ less # inspecciona los archivos de forma interactiva
$ tail # muestra las últimas líneas de un archivo
$ head # muestra las primeras líneas de un archivo
$ grep # imprime las líneas que coinciden con los patrones
$ wc # cuenta las palabras de un archivo
$ find # busca archivos que siguen un patrón
```

### Ayuda y documentación 📚

```bash
$ man <comando> # muestra la documentación de un comando
$ whatis <comando> # muestra una descripción corta de un comando
$ neofetch # (necesario instalarse) muestra información sobre el sistema operativo y el hardware
$ whoami # muestra el nombre de usuario actual.
```

### Documentación adicional 📔

**En ingles** [devhints](https://devhints.io/)
**Tambien en ingles** [quickref](https://quickref.me)
