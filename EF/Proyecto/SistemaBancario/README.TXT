##Contenido
0. Integrantes
1. Módulos
2. Librerías y herramientas implementadas
3. Base de datos
4. Framework
5. Comandos utilizados

0. Integrantes
---------------------------------------------------------------
Evelyn Carolina Jorge       20-0084
Marimel Nicole Suarez       20-0085
Nahomy Gómez                20-0079

1. Módulos
---------------------------------------------------------------
Nuestro sistema de gestión bancaria está compuesto por 5 módulos
principales, los cuales son:

    I. Usuario (Sign Up, Log In y "Mi Cuenta")
    II. GUI de Interacción (Página principal, "Acerca de Nosotros" y sección de ayuda)
    III. Transacciones (Realizar un depósito e historial de transacciones)
    IV. Notificaciones Emergentes (Cuenta existente, cédula o contraseña incorrecta, 
    actualización de información y cuenta eliminada)
    V. Administrador (CRUD)


2. Librerías y herramientas implementadas
---------------------------------------------------------------
Para la elaboración de las funciones, conexión a la base de datos
y diseño de la interfaz del administrador, se utilizaron las siguientes
librerías y/o herramientas:

    I. mysqlclient
    II. Jazzmin
    III. virtualenv
    IV. Herramientas o librerías propias de Django


3. Base de datos
---------------------------------------------------------------
La base de datos utilizada fue MySQL y se implementó la librería
"mysqlclient" para permitir al usuario acceder al servidor y realizar
las acciones requeridas.


4. Framework
---------------------------------------------------------------
El Framework utilizado fue Django con la versión 4.1

5. Comandos utilizados
---------------------------------------------------------------
Algunos de los comandos utilizados fueron:

pip install virtualenv
virtualenv init --python=python
cd .../init/Scripts activate
django-admin startproject SistemaBancario
django-admin startapp users
django-admin startapp cuentas
django-admin startapp bancario
pip install mysqlclient
mysql -u root -p
create database SistemaBancario;
python manage.py makemigrations
python manage.py migrate
python manage.py runserver