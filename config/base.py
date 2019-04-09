
DEBUG = True



# database configuration

MYSQL_HOST="localhost"
MYSQL_PORT=3306
MYSQL_USERNAME="root"
MYSQL_PASSWORD="root"
MYSQL_DATABASE="test_database"

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".format(
        username=MYSQL_USERNAME, password=MYSQL_PASSWORD,
        host=MYSQL_HOST, port=MYSQL_PORT, db=MYSQL_DATABASE
    )
