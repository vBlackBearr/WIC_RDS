import mysql.connector

config = {
    'user': 'admin',
    'password': '12345678',
    'host': 'database-wic.crvlwakzi7le.us-east-1.rds.amazonaws.com',
    'database': 'database_wic'
}

conexion = mysql.connector.connect(**config)
cursor = conexion.cursor()

