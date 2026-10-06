cd C:\\Users\\Emi\\Pictures\\mi\_app\\backend

py -m pip install fastapi uvicorn mysql-connector-python (solamente 1 vez, es cuando lo instalas XD) (Instalación de dependencias)



\--------------



Arrancar FastAPI: framework web moderno y de alto rendimiento para construir APIs (Interfaces de Programación de Aplicaciones) con Python

py -m uvicorn main:app --reload



Queda funcionando en: http://127.0.0.1:8000



Para detener el proceso: Ctrl + C







\-----------------------------------------------------



***Frontend***



**Ubicación :** cd C:\\Users\\Emi\\Pictures\\mi\_app\\frontend



**Arrancar el servidor del frontend:** py -m http.server 5500



**Queda funcionando en:** http://127.0.0.1:5500



**Para detenerlo:** Ctrl + C









\---------------------------------







MySQL : Lo hicimos desde MySQL Workbench



**Para consultar usuarios:**



USE mi\_app;



SELECT \* FROM usuarios;



**Para crear la base inicialmente usamos base.sql**



CREATE DATABASE mi\_app



USE mi\_app;



CREATE TABLE usuarios (

&#x09;id INT AUTO\_INCREMENT PRIMARY KEY,

&#x09;nombre VARCHAT(100) NOT NULL,

&#x09;email VARCHAR(150) NOT NULL

);

