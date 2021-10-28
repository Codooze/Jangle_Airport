import pymysql


def obtener_conexion():
    return pymysql.connect(host='Jeison.mysql.pythonanywhere-services.com',  # probar con su usuario de sistema o localhost
                                user='Jeison',  # probar con root
                                password='admin*****',
                                db='Jeison$default')
