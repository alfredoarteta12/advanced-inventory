# advanced-inventory
Historia de Usuario
Como dueño de un pequeño negocio,
quiero gestionar mi inventario de forma digital y guardarlo en archivos externos,
para no perder la información al cerrar el programa, analizar el rendimiento de mis ventas y compartir mis datos fácilmente.

Criterios de Aceptación (Checklist)

  Guardado persistente: Toda la información de los productos se debe almacenar en un archivo CSV para no perder los datos al cerrar el programa.
  Carga automática: Al iniciar el sistema, la lista de inventario debe actualizarse con los datos guardados previamente.
  control total (CRUD): El sistema debe permitir registrar, consultar, editar y dar de baja productos de forma sencilla.
  Resumen de negocio: El programa debe calcular automáticamente el valor total del inventario y mostrar estadísticas básicas de las existencias.
  alidación de datos: Si se ingresa un dato incorrecto (como texto en un campo de precio) o el archivo no se encuentra, el programa debe mostrar un mensaje de aviso y permitir continuar con la operación.

  Tareas de Desarrollo

  [ ] Estructurar los datos del inventario: Crear la base usando listas y diccionarios para que cada producto tenga su nombre, cantidad y precio bien organizados.
  [ ] Crear el menú de operaciones (CRUD): Programar las funciones que permitan al usuario agregar, ver, editar y borrar productos de la lista actual.
  [ ] Configurar la persistencia en CSV: Desarrollar la lógica para que el programa escriba los datos en un archivo externo y los lea automáticamente al iniciar la sesión.
  [ ] Implementar el motor de estadísticas: Crear una función que recorra el inventario y calcule datos clave, como el valor total de la mercancía.
  [ ] Añadir el sistema de alertas y validación: Configurar mensajes de aviso que informen al usuario si intenta ingresar datos no válidos o si el archivo de inventario no se encuentra disponible
<img width="3337" height="2871" alt="advance inventory drawio (1)" src="https://github.com/user-attachments/assets/ffc3f4c4-31a9-4d84-9b15-507c9c695687" />
