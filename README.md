# Principios de Clean Code o buenas prácticas en coding

## Nombres significativos

### ¿Que nombramos al programar?

1. Variables, funciones y argumentos
2. Clases, paquetes.
3. Ficheros y directorios.
4. Ficheros de despliegue

### Principios para nombrar: 

1. Los nombres deben revelar intención.
2. Evitar la desinformación. Ej: no llamar lista a algo que en realidad es un map o una tupla, clases con nombres largos y muy parecidos pero con diferencias en el centro
3. Usá nombres pronunciables. Los nombres deben ser fáciles de buscar. Es mucho mejor elegir un nombre muy largo a uno que no deja claro su significado. 
4. Añade contexto que aporte significado. Ejemplos: variables firstName, lastName, street, houseNumber, city, state y zipcode hacen sentido estando juntas, pero si las vemos separadas dificilmente sepamos a que hacen referencia. Entonces podríamos agregarle por ejemplo el prefijo **addr** a los atributos para darles contexto. Ej: addr_first_name

### Nombres de las clases

1. Los nombres de las clases deben ser un nombre o conjunto de nombres, no deberían ser verbos
2. Los nombres de los métodos deberían ser verbos, indicando una acción
3. No llamar a una clase CreateEmployee ni a un método EmployeeName(), debería ser Employee el nombre de la clase y get_employee_name el nombre de su método. 

----------------------------------------------------------

## Caracteristicas de las buenas funciones

1. Son pequeñas. De ser posible... muy pequeñas
2. Hacen **UNA** sola cosa.
3. Nivel de abstracción único. Ejemplo de la clase Person que mezcla metodos propios de la clase coche con los que si le corresponden
4. Reciben pocos argumentos. Se deben evitar las funciones con mas de 3 argumentos. Un gran numero de argumentos suele indicar una mala encapsulación. Ejemplo una función "create_user" que recibe 5 argumentos: username, password, firstname, lastname y address podría recibir **solo 1 argumento** (user_form_data: UserFormData) si encapsulamos los 5 atributos anteriores en una clase antes de enviarlos a la función. 
5. No tienen efectos secundarios.
6. Devuelven excepciones en lugar de codigos de error. Es una buena práctica que nuestras funciones devuelvan excepciones programadas en lugar de "logs" informando un error en caso de que algo falle. Dado que de devolver excepciones podríamos manejar el resultado de las mismas con bloque try - catch ó try - except (para los pythonicos como yo)

----------------------------------------------------------

## Comentarios

1. El código limpio o buen código se debe leer perfectamente, sin ningún comentario o casi ningún comentario (Regla de oro del Clean Code)
2. Añadir comentarios solo cuando sea estrictamente necesario. 
3. Son muy complicados de mantener. El código cambia muy rápido, y los comentarios quedan desactualizados rápidamente. 
4. Si el digo tiene muchos comentarios, puede ser dos razones:
   1. El codigo no se entiende --> Refactorización.
   2. Los comentarios son obvios --> Eliminar comentarios. 
5. Nunca dejes comentado código que ya no se está utilizando. ¡Para algo tenemos el software de control de versiones como Git!

### Casos de buenos comentarios

1. Comentar las expresiones regulares con ejemplos del formato permitido por un REGEX.
2. Los Javadocs, docstrings en Python o la documentación inteligente y dinámica de frameworks como FastApi de Python son otro ejemplo claro de buenos y **útiles** comentarios. 
3. Comentarios para marcar TODO´s. Pero no cualquier TODO sino aquel TODO sobre el cual necesitamos el avance de otro equipo para poder avanzar con el mismo (dependencias)

--------------------------------------------------------

## Formato del código

1. Un buen formato facilita la lectura del código. 
2. Recomenadaciones:
   1. Configurar el IDE para que aplique el formato automáticamente al guardar los cambios
   2. Todo el equipo de trabajo debe escribir bajo las mismas reglas
   3. Seguir el styleguide de Google que está disponible para varios lenguajes. Por ejemplo en Java está en: https://google.github.io/styleguide/javaguide.html


### Formato Vertical - Densidad

Es el numero de lineas que hay en un bloque de código en concreto. 

Por ejemplo a la hora de definir una clase nos conviene dejar espacios en blanco entre el primer método y los atributos así como entre método y método para reducir la densidad del código. 

### Formato Vertical - Orden

Ejemplo, si tenemos una función c, una b y un a que llama a la b y c dentro es preferible declarar primero la función a con la llamada a b y c y debajo de a las funciones b y c en ese orden. Al reves no se vería de forma limpia. 

### Formato Verticual - Distancia

Agrupar conceptos relacionados y separar conceptos diferentes. Por ejemplo, dentro de una función podemos dejar juntos, sin espacios las distintas variables que vamos a usar, luego de ellas un if, un nuevo espacio y el return. 

## Formato Horizontal - Densidad

Consiste que no dejar el código muy compacto para facilitar la lectura. Por ejemplo dejar lugares en blanco entre los signos y las letras y/o numeros contribuye a una densidad horizontal equilibrada. 

## Formato Horizontal - Indentación

La identación es clave pero con Python ese problema no lo tendremos nunca dado que la identación estructura los bloques de codigo sin necesidad de usar llaves como en otros lenguajes (java, javascript, etc)

---------------------------------------------------

## Gestión de errores

1. El codigo debe ser limpio, pero también robusto.
2. La gestión de errores puede ensuciar mucho el código, por lo que hay que prestarle especial atención. 
3. Devolver excepciones en lugar de códigos de error
4. Usar excepciones unchecked
5. No devoler ni pasar null. Si pasamos null quien lo recibe está obligado a verificar que hayamos devuelto algo distinto de null para continuar. Caso contrarío podriamos generar una NullPointerExcepction que podría generar errores en el código por no tratarlo correctamente. 

### ¿Que son las **unchecked exceptions**?

1. Se trata de excepciones que heredan de la clase RuntimeExcepción. Es decir, son excepciones que ocurren en tiempo de ejecución y no en tiempo de compilación. Ejemplo: la NullPointerException de Java
2. Se pueden tratar con try-catch (o try-except en Python) pero no es estrictamente necesario. 
3. Las excepciones checked, son las excepciones normales, heradan de Excepción. **Si no las tratas el programa no compila.**
4. Recomendado **usar checked Excepctions si se trata de una librería crítica**, que sea de obligado cumplimiento tratar las excepciones. 

-----------------------------------------------------

## Test Unitarios

### Tener test que pueben tus funciones y clases es fundamental para:

1. La refactorización del código. 
2. Estar seguros a la hora de realizar modificaciones sobre el código. Si tenemos un alto coverage de Testing (>90%) esto nos ofrece mucha seguridad a la hora de iterar el codigo. Lo modificamos y si sigue pasando los test unitarios entonces es correcto el codigo que implementamos. 

Para hacer testing se recomienda usar las librerías que casi todos los lenguajes de programación tienen con este objetivo. Algunas de las mas conocidas son: JUnit, unittest, jasmine, etc. 

**Test Driver Development (TDD):** Filosofía de desarrollo de Software muy conocida orientada integralmente al desarrollo de Test Unitarios. Desarrollo guiado por test. 
Antes de crear codigo para una nueva funcionalidad, **lo primero que debo escribir es el test de esa funcionalidad.**, En segundo lugar **implementamos la funcionalidad que queriamos desarrollar** desde el inicio teniendo en consideración que debe pasar el test que ya fue escrito. En tercer lugar, mejorar el código que acabamos de desarrollar, **limpiando el codigo, refactorizando, etc, estando seguros de que no vamos a romper** nada dado que en la medida en que generamos cambios vamos testeando los mismos.  

Esta filosofía es muy buena en la teoria pero en la práctica es muy complicada de implementar por lo que muy poca gente lo sigue al 100%. Al implementar primero los tests, tu código será mas facil de probar. 

-------------------------------------------------------










