class Config:
    SECRET_KEY='B!weNAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root' 
    MYSQL_PASSWORD = 'thomas2009'
    MYSQL_DB = 'flask_login'


config = {
    'development': DevelopmentConfig
}