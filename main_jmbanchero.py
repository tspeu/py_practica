# from ValidatorsClass import *
from AutorClass import *
from LibroClass import *
from ValidatorsClass import *
import pickle

# todo
"""
El módulo principal contendrá la función main que hará uso de los métodos
de la clase Libro y autor, tendrá un menú para trabajar con Libros y autores
creando listas, con las opciones de crear/modificar y eliminar tanto libros
como autores.
"""

# todo
"""
Creación de ficheros para cargar los datos al programa tanto los libros como
los autores, para ello se contemplarán esta opción en el menú así como se
deberá actualizar los ficheros cuando se agreguen elementos o se actualicen
en el programa.
"""

# contantes
_MSM = "Escojer una opción:\n"
__LIBROS__NAME = "libros"
__LIBRO__NAME = "libro"
__AUTORES__NAME = "autores"
__AUTOR__NAME = "autor"
__INDICE_NAME = "Indique el índice correcto: "
__MENU__DATA = f"Desea cargar datos desde un fichero externo.\n{_MSM}[S-s]\nOtra tecla para no cargar los datos\n"
__MENU_NAME = f"{_MSM}[1]:Mostrar Libros\n[2]:Crear Libro\n[3]:Modificar Libro\n[4]:Eliminar Libro\n" \
              f"[5]:Mostrar Autores\n[6]:Crear Autor\n[7]:Modificar Autor\n[8]:Eliminar Autor\n" \
              f"[9]:Grabar Datos en ficheros y Salir\n[x] SALIR\n"
__ISBN_NAME = "introducir el ISBN: "
__TITULO_NAME = "introducir el Título del libro: "
__ID_AUTOR_NAME = "introducir el ID_AUTOR: "
__NAME_AUTOR_NAME = f"introducir el Nombre del {__AUTOR__NAME}: "
__APELLIDOS_AUTOR_NAME = f"introducir el/los apellido/s del {__AUTOR__NAME}: "
__FECHA_AUTOR_NAME = f"introducir el año de nacimiento del {__AUTOR__NAME}: "
__MMS_ERROR = "No se han encontrado "
__MODIFICAR_LIBROS_NAME = f"Escojer un libro para modificar. {__INDICE_NAME}"
__MODIFICAR_AUTOR_NAME = f"Escojer un autor para modificar. {__INDICE_NAME}"
__ESCOGER_AUTOR_NAME = f"Escojer un autor. {__INDICE_NAME}"
__BORRAR_LIBROS_NAME = f"Escojer un libro para eliminar. {__INDICE_NAME}"
__BORRAR_AUTOR_NAME = f"Escojer un autor para eliminar. {__INDICE_NAME}"
__ID_AUTOR_DEFAULT = 1
__NAME_AUTOR_DEFAULT = "ANÓNIMO"
__APELLIDO_AUTOR_DEFAULT = "DESCONOCIDO"
__FECHA_AUTOR_DEFAULT = "1900"
# constantes


"""
:arg string, string, string
:return class Libro
"""
def crear_libro(isbn, titulo, id_autor):
    return Libro(isbn, titulo, id_autor)


"""
:arg List() _autores, string clase
pide los datos del isbn. llama al validador de ISBN por medio del metodo input_isbn,
titulo, y si existen autores, se muestra la lista de autores y se escoge uno
el id_autor se pasa al libro. sino el id_autor será 1
:return List() string, string.title(), string
"""
def datos_libros(_autores, clase):
    isbn = input_isbn(__ISBN_NAME)
    titulo = input_valor(__TITULO_NAME)
    if len(_autores) > 0:
        mostrar_lista(_autores, clase)
        _index = input_indice(__ESCOGER_AUTOR_NAME, len(_autores))
        _a = _autores[int(_index)]
        id_autor = _a.get_id_autor()
    else:
        id_autor = "1"  # input_valor(__ID_AUTOR_NAME)
    return [isbn, titulo.title(), str(id_autor)]


"""
:param string _id 
pide los datos del isbn, se llama al validador ISBN,
titulo , y se pasa el mismo id_autor.
En esta versión no es posible modificar el id del autor.
"""
def datos_libros_modificar(_id):
    isbn = input_isbn(__ISBN_NAME)
    titulo = input_valor(__TITULO_NAME)
    return [isbn, titulo.title(), str(_id)]


"""
:arg string, string, string. 
:return class Autor
"""
def crear_autor(nombre, apellido, id_a, fecha):
    return Autor(nombre, apellido, id_a, fecha)


"""
pide los datos de la clase Autor,
nombre, apellido, el id_autor se genera automaticamente,
fecha se llama al validador del año
:return List[string, string, int, string]
"""
def datos_autor():
    nombre = input_valor(__NAME_AUTOR_NAME)
    apellido = input_valor(__APELLIDOS_AUTOR_NAME)
    # id_a = input_valor(__ID_AUTOR_NAME)
    id_a = crear_id_ramdom()
    fecha = input_fecha(__FECHA_AUTOR_NAME)
    return [nombre.title(), apellido.title(), id_a, fecha]


"""
:param list() _list lista , string clase, se pasa el nombre de la clase
 si existe se muestra cada item
"""
def mostrar_lista(_lista, clase):
    _cont = 0
    if _lista:
        for elem in _lista:
            print(f"[{_cont}] {elem.__str__()}")
            _cont += 1
    else:
        print(f"{__MMS_ERROR} {clase}")


"""
:param list[] _list1, string clase, List[] list2
 si existe se muestra cada item
 se muestra los elemntos de la list1, libros
 se recorre la list1, autores y se busca el id_autor si coincide
 se muestra  nombre y el apellido del autor.
"""
def mostrar_libros_autores(_lista, clase, _list2):
    _cont = 0
    _msm = ""
    if _lista:
        for elem in _lista:
            if len(_list2) > 0:
                _a_id = elem.get_id_autor()
                _autor = find(_list2, _a_id, "get_id_autor()")
                # _list2[_in].__str__()
                _msm = _autor.autor_nombre()
            print(f"[{_cont}] {elem.__str__()}, autor:{_msm}")
            _cont += 1
    else:
        print(f"{__MMS_ERROR} {clase}")


"""
:param list[] _list, string _id, string _value
recorre la lista y si encuentra el valor de _id en la 
propiedad valor(id_autor) 
:return el elemnto encontrado
"""
def find(_list, _id, _value):
    for x in _list:
        if x.get_id_autor() == int(_id):
            return x


"""
:param lista() _lista si existe la lista
:param  str modificar_name el nombre de la lista a modificar
se llama a input_indice() si el indice es correcto
se llama a modificar_vehiculo() pasando la clase por parametro
:return  _diccionario{ item: index:}
"""
def modificar_lista(_lista, modificar_name):
    if _lista:
        opt = input_indice(modificar_name, len(_lista))
        if opt:
            _i = int(opt)
            # print(type(_lista[_i]).__name__)
            _ele = modificar_item(type(_lista[_i]).__name__, _lista[_i].get_id_autor())
            __dic = {"item": _ele, "index": _i}
            return __dic


"""
:param string clase, acepta la clase 
se llama a los metodos de tomar datos de cada clase
:return  un objeto del tipo clase datos validados
"""
def modificar_item(clase, _id):
    if clase == "Libro":
        __l = datos_libros_modificar(_id)
        print(f"{clase} modificada!")
        print("el id del autor no puede modificarse")
        return crear_libro(__l[0], __l[1], __l[2])
    if clase == "Autor":
        __a = datos_autor()
        print(f"{clase} modificada!")
        return crear_autor(__a[0], __a[1], _id, __a[3])


"""
:param list() _list acepta la lista
si la lista tiene items se llama a input_indice() con el mensaje del input y la longitud de la lista
si el indicé es correcto se borra el item de la lista en el indice
"""
def borrar_lista(_lista, borrar_name, clase):
    mostrar_lista(_lista, clase)
    if len(_lista) > 0:
        opt = input_indice(borrar_name, len(_lista))
        if opt:
            _i = int(opt)
            _lista.pop(_i)
            print(f"{clase} se ha eliminado correctamente!")


"""
:param _i int. indice que se quiere mostrar
:param _list list[], lista con los datos
:return elemto de la lista en la posución _i
"""
def mostrar_por_index(_i, _list):
    return _list[_i]


"""
:param _list list[], lista con los datos
:param name_fichero string, nombre del fichero que va a guardar
"""
def grabar_datos(_list, name_fichero):
    #  todo validar
    _n = f"{name_fichero}.pckl"
    __f = open(_n, "wb")
    pickle.dump(_list, __f)
    __f.close()


"""
:param = name string . es el nombre del fichero que se va a cargar
:return _list list[]. con los datos del fichero
"""
def cargar_datos(_name):
    _n = f"{_name}.pckl"
    if validated_file_exist(_n):
        _f = open(_n, "rb")
        _lista = pickle.load(_f)
        print(f"Datos cargados correctamente. fichero: {_n}")
        for _l in _lista:
            print(_l.__str__())
        _f.close()
        return _lista
    else:
        print(f"El fichero {_n} no existe!")
        return False


"""
muesta el menu para cargar datos externos
:return lista1 con datos de fichero libros
:return lista2 con datos de fichero autores
"""
def menu_datos(_lista1, _lista2):
    print(".......cargando datos")
    _lista1 = cargar_datos(__LIBROS__NAME)
    _lista2 = cargar_datos(__AUTORES__NAME)
    return [_lista1, _lista2]


"""
menu principal del programa
"""
def menu_principal():
    __libros = []
    __autores = []
    if validated_file_exist(f"{__LIBROS__NAME}.pckl"):
        _cont = True
        while _cont:
            _opt = input(__MENU__DATA)
            if _opt == "S" or _opt == "s":
                __l = menu_datos(__libros, __autores)
                __libros = __l[0]
                __autores = __l[1]
                _cont = False
            else:
                print("No se han cargado los datos desde ficheros externos")
                _cont = False
    continuar = True
    while continuar:
        opcion = input(__MENU_NAME)
        if opcion == "1":
            print(f"mostrar {__LIBROS__NAME}!")
            # mostrar_lista(__libros, __LIBROS__NAME)
            mostrar_libros_autores(__libros, __LIBROS__NAME, __autores)
        elif opcion == "2":
            print(f"crear {__LIBROS__NAME}!!")
            if len(__autores) > 0:
                _l = datos_libros(__autores, __AUTORES__NAME)
                __libros.append(crear_libro(_l[0], _l[1], _l[2]))
            else:
                print("Primero debe crear un autor. Escoger opción [6]")
        elif opcion == "3":
            print(f"modificar {__LIBROS__NAME}!!")
            mostrar_lista(__libros, __LIBROS__NAME)
            if len(__libros) > 0:
                _dic_libros = modificar_lista(__libros, __MODIFICAR_LIBROS_NAME)
                print(_dic_libros.get("item"))
                __libros[_dic_libros.get("index")] = _dic_libros.get("item")
        elif opcion == "4":
            print(f"borrar {__LIBROS__NAME}!")
            borrar_lista(__libros, __BORRAR_LIBROS_NAME, __LIBROS__NAME)
        elif opcion == "5":
            print(f"mostrar {__AUTORES__NAME}!")
            mostrar_lista(__autores, __AUTORES__NAME)
        elif opcion == "6":
            _a = datos_autor()
            __autores.append(crear_autor(_a[0], _a[1], _a[2], _a[3]))
        elif opcion == "7":
            print(f"modificar {__AUTOR__NAME}!")
            mostrar_lista(__autores, __AUTORES__NAME)
            if len(__autores) > 0:
                _dic_aut = modificar_lista(__autores, __MODIFICAR_AUTOR_NAME)
                print(_dic_aut.get("item"))
                __autores[_dic_aut.get("index")] = _dic_aut.get("item")
        elif opcion == "8":
            print(f"Eliminar {__AUTOR__NAME}!")
            borrar_lista(__autores, __BORRAR_AUTOR_NAME, __AUTOR__NAME)
            pass
        elif opcion == "9":
            if __autores or __libros:
                print("....guadando datos en ficheros externos")
                grabar_datos(__libros, __LIBROS__NAME)
                grabar_datos(__autores, __AUTORES__NAME)
                print("Saliendo del programa!")
            else:
                print("No hay datos que grabar en los ficheros externos!")
            continuar = False
        else:
            if opcion == "X" or opcion == "x":
                print("Saliendo del programa!")
                continuar = False
            else:
                print("LA OPCIÓN NO ES VÁLIDA!")


#  TEST
# validated_year("100")

# Driver Code
# isbns = [
#     "0811821846",
#     "978-0811821841",
#     "1616550414",
#     "978-1616550417",
#     "0553418025",
#     "978-0553418026",
# ]

# print(is_valid_isbn13('9783161484100'))
# print(is_valid_isbn13('9783161484100'))
# print(is_valid_isbn13('0811821846'))
# print(is_valid_isbn10('0811821846'))
# print(is_valid_isbn10('1616550414'))
# print(is_valid_isbn10('0553418025'))
# print(is_odd(12))
# print('is_odd(12)')
# print(is_odd(10))

# validar_fecha("123")
# validar_fecha("120")
# validar_fecha("10")
# validar_fecha("560")
# validar_fecha("1224")
# validar_fecha("1")
