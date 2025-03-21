@echo off
:: Establecer la variable de entorno FLASK_APP
set FLASK_APP=.\src\main.py

:: Activar el entorno virtual
call C:\Users\adair\.virtualenvs\backend-KEA-lZw9\Scripts\activate

:: Ejecutar Flask
flask run -h 0.0.0.0

