# Prueba-Arkon

## Pasos para arrancar el proyecto
1. Crear un entorno virtual con python
> Yo utilizo el virtualvenv que trae python https://docs.python.org/es/3/library/venv.html
```
python3 -m venv myvenv
```
![Screenshot from 2023-01-31 07-18-28](https://user-images.githubusercontent.com/53199747/215771441-b91b2c59-0bcb-4d44-af94-87a46172a5ae.png)

2. Activar el entorno virtual.
![Screenshot from 2023-01-31 07-20-41](https://user-images.githubusercontent.com/53199747/215771698-2d760c64-545d-47be-bdce-aa9a78d20cbd.png)
> Recuerda ejecutar todo en el virtualenv. Si no ves un prefijo `(myvenv)` en tu consola tienes que activar tu virtualenv.
Basta con escribir `myvenv\Scripts\activate` en Windows o `source myvenv/bin/activate` en Mac OS / Linux.

3. Instalar las dependencias del proyecto
```
pip install -r requirements.txt
```
![Screenshot from 2023-01-31 07-22-36](https://user-images.githubusercontent.com/53199747/215772106-0eaec0c4-aadc-42ea-923f-2c631e578728.png)


4. Crear los contenederos de pgadmin4 y postgres
```
docker-compose up
```
![Screenshot from 2023-01-31 07-23-55](https://user-images.githubusercontent.com/53199747/215772417-d84fa999-79e4-4e29-baf9-c3fe93b8ea8c.png)


5. Registrar un servidor de postgres con pgadmin4
  - Logearnos en pgadmin4 
    1. Abrimos un navegador y vamos a localhost
    ![Screenshot from 2023-01-31 06-48-09](https://user-images.githubusercontent.com/53199747/215764288-752c210d-fc21-43cc-9998-952071d03102.png)
    2. Va aparecernos un formulario de correo ponemos:
    ```
    admin@admin.com
    ```
    - Contraseña
    ```
    admin
    ```
  - Registrar un nuevo servidor
    1. Dentro del panel de pgadmin4 en la parte izquierda vamos a registrar un nuevo servidor, dando click derecho a **Servers** > **Register** > **Server**
    ![Screenshot from 2023-01-31 06-55-45](https://user-images.githubusercontent.com/53199747/215766030-2a1d070c-8a31-46a5-b453-ec9fb070ef88.png)


    2. Al dar click en server nos saldra un modal
    ![Screenshot from 2023-01-31 07-00-51](https://user-images.githubusercontent.com/53199747/215766788-396c43d3-4ccd-4022-806c-7efef9301fed.png)
    > En **name** podemos poner cualquier nombre
		>
    > Después nos dirigimos en el mismo modal a **Connection**
     ![Screenshot from 2023-01-31 07-04-32](https://user-images.githubusercontent.com/53199747/215767757-c37f1923-2bf3-4686-b5eb-1577e1a98b5e.png)
    > En **Host name** ponemos postgres y guardamos dando click en **save**
    
6. Ejecutar las migraciones de tablas del proyecto 
```
python3 manage.py migrate
```
7. Correr el servidor
```
python3 manage.py runserver
```

8. Correr los test unitarios
```
python3 manage.py test
```

## Probrar el proyecto.
> Para probar el proyecto en todo momento debe de estar corriendo el servidor y los contenedores de docker y pgadmin4
1. Se puede probar ejecutando los test unitarios con
```
python3 manage.py test
```

2. Utilizando postman o la interfaz que nos da django rest_framework
> Nos podemos dirigir a `http://localhost:8000/swagger/` Nos mostrara una
documentación de la API
![Screenshot from 2023-01-31 07-40-10](https://user-images.githubusercontent.com/53199747/215776264-af7540e0-f4ae-414b-87c1-f836d1e5f544.png)
- Postman
  > Postman es una plataforma de API para que los desarrolladores diseñen, construyan, prueben e iteren sus API https://www.postman.com/downloads/
  1. Abrir postman

  2. Hacer peticiones
	> Para hacer una petición tenemos que pegar el url y seleccionar el método
	![image](https://user-images.githubusercontent.com/53199747/215781081-18920e4e-a67e-4699-aac4-3972f429898c.png)
	
	- Una vez hecho lo anterior. En el caso de que la petición requiera datos, debemos pasarselos
	https://abi.gitbook.io/net-core/4.-creando-tu-primer-servicio/4.4-probando-tus-servicios-con-postman
	

- Interfaz de django_rest_framework
  > Para utilizarla solamenete debemos dirigirnos a la ruta
  >
  > Ejemplo: Si queremos crear un evento nos dirigimos a http://localhost:8000/api/v1/events/
  ![image](https://user-images.githubusercontent.com/53199747/215778118-03e5c2e2-37e2-4675-ab99-620b1bb41bfc.png)
  > Ahí nos mostrara un formulario con los datos a llenar.


## Diagrama de la Base de Datos
> Cree 2 tablas. La tabla eventos y tabla tickets.
>
> Como maneje los boletos. Lo conecte con la tabla eventos haciendo una
 relacion de uno a muchos
![Untitled(1)](https://user-images.githubusercontent.com/53199747/215773468-7f871532-ab63-4269-a33f-c55a0c2624d0.png)

