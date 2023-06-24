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

## Ejemplo practico: 

Para llamar a los métodos de nuestras clases de test podemos usar la estructura: 

- given(pre-condición/dado) + when(cuando) + then(entonces): 

- Clases a testear: 

```py
class CalculadoraEstatica:
    # Puedo acceder a sus métodos sin instanciarla
    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b

    @staticmethod
    def division(a, b):
        return a / b
    

class Calculadora:
    # Tiene constructor dado que para acceder a sus métodos debo instanciarla
    def __init__(self):
        pass

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def division(self, a, b):
        return a / b
```

- Clases de testeo con unittest y coverage para ver y analizar cobertura: 


```py
from unittest import TestCase
from calculadoras import CalculadoraEstatica, Calculadora


class CalculadoraEstaticaTest(TestCase):

    def test_metodo_suma_deberia_retornar_la_suma_de_dos_numeros(self):
        # Given
        numero1 = 5
        numero2 = 10

        # When
        resultado = CalculadoraEstatica.suma(numero1, numero2)

        # Then
        self.assertEqual(resultado, 15)

    def test_metodo_resta_deberia_retornar_la_resta_de_dos_numeros(self):
        # Given
        numero1 = 10
        numero2 = 5

        # When
        resultado = CalculadoraEstatica.resta(numero1, numero2)

        # Then
        self.assertEqual(resultado, 5)

    def test_metodo_division_deberia_retornar_el_cociente_de_dos_numeros(self):
        # Given
        numero1 = 10
        numero2 = 2

        # When
        resultado = CalculadoraEstatica.division(numero1, numero2)

        # Then
        self.assertEqual(resultado, 5)
    
    def test_metodo_division_deberia_generar_un_error_si_el_divisor_es_cero(self):
        # Given
        numero1 = 10
        numero2 = 0

        # When & Then
        with self.assertRaises(ZeroDivisionError):
            CalculadoraEstatica.division(numero1, numero2)


class CalculadoraTest(TestCase):

    def test_metodo_suma_deberia_retornar_la_suma_de_dos_numeros(self):
        # Given
        mi_clase = Calculadora()
        numero1 = 5
        numero2 = 10

        # When
        resultado = mi_clase.suma(numero1, numero2)

        # Then
        self.assertEqual(resultado, 15)

    def test_metodo_resta_deberia_retornar_la_resta_de_dos_numeros(self):
        # Given
        mi_clase = Calculadora()
        numero1 = 10
        numero2 = 5

        # When
        resultado = mi_clase.resta(numero1, numero2)

        # Then
        self.assertEqual(resultado, 5)

    def test_metodo_division_deberia_retornar_el_cociente_de_dos_numeros(self):
        # Given
        mi_clase = Calculadora()
        numero1 = 10
        numero2 = 2

        # When
        resultado = mi_clase.division(numero1, numero2)

        # Then
        self.assertEqual(resultado, 5)
    
    def test_metodo_division_deberia_generar_un_error_si_el_divisor_es_cero(self):
        # Given
        mi_clase = Calculadora()
        numero1 = 10
        numero2 = 0

        # When & Then
        with self.assertRaises(ZeroDivisionError):
            mi_clase.division(numero1, numero2)
```

Para simplemente ejecutar los testeos usando unittest debo ubicarme en el directorio donde tengo el archivo de testing y ejecutar el comando: 

```bash
python3 -m unittest nombre_del_archivo.py
```

Si quiero ejecutar los tests usando el modulo de coverage entonces debo: 

1. Instalar coverage en mi venv: 

```bash
pip install coverage
```

2. Asegurarme de que mi archivo de test comience con "test_" y termine con ".py"

3. Ejecutar en consola: 

```bash
coverage run -m unittest discover
```
Ejecuta todos los test que tenga la sintaxis señalada arriba

```bash
coverage report
```
Imprime por consola el reporte de cobertura

```bash
13:13:59 👽 with 🤖 mgobea 🐶 in ~/develop/clean_code via clean_code …
➜ coverage report
Name                   Stmts   Miss  Cover
------------------------------------------
calculadoras.py           19      0   100%
test_calculadoras.py      48      0   100%
------------------------------------------
TOTAL                     67      0   100%
```

```bash
coverage html
```
Genera un directorio y dentro del mismo un archivo index.html donde podremos ver en una web el mismo reporte de cobertura que antes veiamos por consola. 

<img src="./images/coverage_report_html.png">

----------------------------

## Code Smells (Código que huele mal)

**¿Que son los code smells?**

1. Son síntomas de que el código no es todo lo limpio que debería. Algo "huele mal en el código".
2. 7 Tipos de code smells:
   1. En los comentarios
   2. En el entorno de desarrollo
   3. En las funciones
   4. Code smells generales
   5. Code smells en Java (aunque muchos se peuden aplicar a otros lenguajes)
   6. En los nombres
   7. En los tests.

------------------------------

## Code smell en los comentarios: 

**C1: Información inapropiada**

Todo lo que esté mejor en otro sistema (ej. Sistema de control de cambios - Git) debe ser eliminado del codigo. 

Ejemplo mas clasico ó 1: Código sin uso en la actualidad que lo dejamos "por las dudas". Es una mala práctica dado que si llegamos a necesitarlo podemos volver a encontrarlo en la historia de nuestro proyecto de Git u otro sistema de versionado. 

Ejemplo 2: Dejar comentado los datos del autor del código y la fecha de creación... Esto es información que ya queda registrada en nuestro sistema de versionado.

```py
# @author Mariano Gobea
# Create Date: 24.06.2023 13:45 hs
class Comments:
   pass
```

Ejemplo 3: TODO´s con los pendientes. También es una mala práctica. Los pendientes deben ser registrados en un sistema de registro de tareas pendientes como por ejemplo "Monday" o "Notion" no en el código en sí. 

Ejemplo 4: Comentarios obsoletos, supongamos que tenemos una una variable que almacena una fecha y en principio era de tipo string pero luego la cambiamos a Datetime. Si el comentario sigue señalando que es de tipo String entonces se trata de un comentario obsoleto: 

```java
private Date lastLoginDate; // Last Login date as String (DD-MM-YYYY HH:MM)
```
Ejemplo 5: Comentarios redundantes. Es decir, comentarios que dan información que es muy clara con solo leer el código si es que el mismo fue bien nombrado. 

Ejemplo 6: Comentarios mal redactados. No hay que cometer faltas de ortografía en los comentarios, debemos asegurarnos de que se entienda lo que queremos decir con los mismos.

-------------------------

## Code smells asociados al entorno de desarrollo. 

Mas concretamente son code smells asociados a la etapa de compilación del software y de la ejecución de tests. 

E1: La compilación requiere mas de un paso: 
Debes ser capaz de hecer un checkout del código fuente con un comando y compilarlo con otro. 

Aplicado a Python tiene que ver con las dependencias de un proyecto. Es importante detallar las mismas (archivo requirements.txt) así como un código simple que nos permita tenerlas y no estar instalando una por una. En python ese comando es: 

```bash
pip install -r requirements.txt
```
Por supuesto que este comando solo va a funcionar en los casos donde contemos en el proyecto donde estamos trabajando con un archivo requirements.txt. De allí la importancia de generarlo y mantenerlo actualizado al mismo cuando somos nosotros los que iniciamos un proyecto o agregamos dependencias al mismo que inicialmente no existian. 

E2: Los tests requieren mas de un paso

Los tests se deben ejecutar con único comando que sea simple, rápido y obvio. Caso contrario corremos el riesgo de ejecutar los tests habitualmente por "pereza". Debemos ejecutar los tests cada día decenas, o incluso cientos de veces para evitar cometer errores en el código que luego nos cueste mucho tiempo encontrar. 

Ejemplo en python para ejecutar un archivo de test contamos con el comando: 

```bash
python3 -m unittest nombre_del_archivo.py
```

--------------------------------

## Code smells asociados a las funciones

F1: Demasiados argumentos

Lo mejor es que una función no reciba argumentos, seguido por uno, dos y tres argumentos. Se deben evitar las funciones con > 3 argumentos. 

Es una buena práctica, que ya mencionamos mas arriba encapsular argumentos dentro de una clase cuando la misma recibe mas de 3 argumentos. Otra opción es dividir la función en dos o mas funciones para reducir así la cantidad de argumentos recibidos. Dado que seguramente si una función recibe mas de tres argumentos su scope sea superior a la máxima que reza que una función debe hacer una única cosa. 

F2: Argumentos de salida

Una función no debe realizar tareas de salida a consola, por ejemplo, no debe imprimir. En su lugar debe retornar los valores que que queremos sacar de la misma para que la impresión se realice desde el codigo principal.

Otro ejemplo del mismo error es envíar un argumento con puntero (& para enviarla y * para recibirla. Al igual que los punteros en Golang), es decir, del entorno global del programa, dado que queremos modificarlo dentro de la función en lugar de retornar un valor de la función y luego guardarlo en una variable que invoque a nuestra función.

F3: Pasar flags (variables booleanas) como argumento

¿Por que es un error? Porque un flag suele indicar que una función hace mas de una cosa, es decir, va a hacer algo si el flag es true y otra cosa si el flag es false. Y como ya repetimos muchas veces esto es un error dado que una función debe hacer una única cosa. Si tenes la necesidad de hacer dos cosas distintas entonces debemos generar dos funciones distintas en lugar de una función que reciba un booleano. 

F4: Funciones Muertas

Son aquellas funciones que no se llaman nunca. Las mismas se deben eliminar. Si las necesitamos en el futuro siempre podemos ir a buscarlas a GIT. 

--------------------------------

## Code smells generales - Parte 1: 

























