## Credenciales 
```
USER: i.martinpena

CORREO: i.martinpena@usp.ceu.es

CONTRASEÑA: 105462
```

## Resumen comandos de GIT
```
- Inicialización de repositorios: git init
- Clonación de repositorios existentes: git clone
- Revisión de cambios: git status
- Preparación de archivos para confirmación: git add
- Confirmación de cambios: git commit -am "comentarios"
- Publicación de cambios en repositorios remotos: git push
- Actualización de la copia local: git pull
- Gestión de ramas: git branch, git checkout
```

## Configuración GIT
Configuración usuario:
```
git config --global user.name "i.martinpena"
git config --global user.email i.martinpena@usp.ceu.es
```

Inicializa un nuevo repositorio de Git en el directorio actual:
```
git init
```
Clona un repositorio existente desde una URL: git clone [url]
```
git clone https://github.com/ejemplo/repo.git
```

Muestra el estado del repositorio, incluidos los cambios no rastreados o en espera:
```
git status
```

Agrega un archivo al área de preparación (staging area) para el próximo commit: git add [archivo]
```
git add ejemplo.txt
git add *
```

Realiza un commit de los cambios preparados con un mensaje: 
```
git commit -m "Añade ejemplo.txt al proyecto"
```

Envía los commits al repositorio remoto: git push [remote] [rama]
```
git push origin master
```

Actualiza el repositorio local con los cambios del repositorio remoto: git pull [remote] [rama]
```
git pull origin master
```

Crea una nueva rama: git branch [nombre-rama]
```
git branch nueva-rama
```

Cambia a otra rama: git checkout [nombre-rama]
```
git checkout nueva-rama
```
