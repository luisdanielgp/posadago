# "PosadasGo" un proyecto de b17devf 

Este es un proyecto creado el día Viernes 1 de Diciembre para el segundo hackaton-cito de Dev.f batch 17. Este reto consistia en realizar tres plataformas: un chatbot, una plataforma web y una aplicacion de django con el fin de solucionar el problema de la realizacion de una posada.

### Equipo

* Alex - Cinta Blanca
* Karla - Cinta Roja
* Jorje - Cinta Roja
* Luis - Cinta Negra Backend
* Jade - Cinta Negra Backend
* Jesus - Cinta Negra Frontend

## Requerimientos

Los requerimientos son tener instalado [Python](https://www.python.org/downloads/) y [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/) en el servidor, asi como [PostgreSQL](https://www.postgresql.org/) de manera global.

Como primer paso, el proyecto necesita correr dentro del entorno virtual de Virtualenv con todo lo que requerimos, procederemos a crearlo mediante las siguientes lineas de comandos:

```
$ virtualenv venv -p python3
```

```
$ source venv/bin/activate
```

```
(venv)$ pip install django requests djangorestframework psycopg2
```

### Para correrlo con una base de datos de PostgreSQL:

Con las anteriores lineas de comando tendremos configurado nuestro entorno virtual "venv" para poder correr el proyecto, a demás de eso, necesitamos tambien crear un superusuario y una base de datos en PostgreSQL mediante pgAdmin v4 (obviaremos la creacion de un usuario superuser y una base de datos asignada a dicho usuario). Posteriormente configuraremos en el archivo ./settings.py dentro del proyecto los parametros para la conexion a la base de datos.


**Extracto de la linea 78 de ./settings.py**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'NOMBREDELABASEDEDATOS',
        'USER': 'NOMBREDELSUPERUSUARIO',
        'PASSWORD': 'CONTRASEÑADELSUPERUSUARIO',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
```
La aplicacion de Django tiene un endpoint que recibe un json del chatbot (la informacion como el nombre del usuario, lo que va a llevar a la posada y si confirma que va a la posada) y que a demas hace una peticion post. Este endpoint tambien sera consumido por la plataforma web a traves de una peticion get.
