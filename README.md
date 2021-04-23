# PLEASE READ!
Beginner project with Python.
This is a selenium bot to earn points on the page [youlikehits.com](http://youlikehits.com/)

## How does the page work?
This page is to promote your social networks and websites for free. You have to add your profiles and then through a points system gain followers and interactions. By following other people you earn points that you exchange for followers for your own account.

## What do you need?
- An account at [youlikehits.com](http://youlikehits.com)
- A dummy twitter account to earn automatic points
- Download the webdriver, in this case I use google chrome. You can download it [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). **(place the webdriver in the same directory where the youlikehits_bot.py file is)**

## How does the bot work?
You enter your credentials in the terminal: youlikehits username, youlikehits password, twitter username, twitter password **(remember that it is a dummy twitter account, do not use your main account).**
The bot will run 3 times by default, this value can be changed directly in the youlikehits_bot.py file.

1. The driver starts and enters the main page and log in.
2. Open the twitter followers exchange page and log in.
3. Follow the user and return to the main page.
4. Confirm the user followed and close the page.
5. The bot starts again depending on how many times it is placed by default.

In the file **requirements.txt** are the modules used.

# POR FAVOR LEER!
Proyecto principiante con Python.
Este es un bot de selenium para ganar puntos en la pagina [youlikehits.com](https://www.youlikehits.com/)

## ¿Cómo funciona la pagina?
Esta pagina es para promocionar tus redes sociales y sitios web gratis. Tienes que agregar tus perfiles y luego mediante un sistema de puntos ganar seguidores e interacciones. Al seguir a otras personas ganas puntos que luego intercambias por seguidores para tu propia cuenta.

## ¿Qué necesitas?
- Una cuenta en youlikehits.com
- Una cuenta de twitter ficticia para ganar los puntos automaticos
- Descargar el webdriver, en este caso se uso el de google chrome. Puedes descargarlo [aqui](https://sites.google.com/a/chromium.org/chromedriver/downloads). **(Coloca el webdriver en la misma carpeta donde esta el archivo youlikehits_bot.py)**

## ¿Qué hace el bot?
Ingresas en la terminal tus credenciales: usuario de youlikehits, contraseña de youlikehits, usuario de twitter y contraseña de twitter **(recuerda que es una cuenta ficticia de twitter, no uses tu cuenta principal)**.
El bot correra 3 veces de manera predeterminada, este valor puede cambiarse directo en el archivo youlikehits_bot.py
1. Arranca el driver y entra a la pagina youlikehits.com y se loguea
2. Abre la pagina de intercambio de seguidores en twitter y se loguea
3. Sigue al usuario y vuelve a la pagina principal
4. Confirma el usuario seguido y cierra la pagina
5. Inicia nuevamente el bot dependiendo cuantas veces se coloque de manera predeterminada

En el archivo **requirements.txt** se encuentran los modulos utilizados.
