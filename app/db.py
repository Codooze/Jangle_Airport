import pymysql


def obtener_conexion():
    return pymysql.connect(host='Jeison',  # probar con su usuario de sistema o localhost
                                user='root',  # probar con root
                                password='admin*****',
                                db='Jeison$default')
