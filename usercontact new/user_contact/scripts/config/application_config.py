import configparser

config = configparser.ConfigParser()
config.read('user_contact/conf/settings.conf')

# POSTGRESQL_CONFIG = config['postgresql']


config.read('user_contact/conf/settings.conf')

MONGODB_URI = config.get('mongodb', 'uri')
DATABASE_NAME = config.get('mongodb', 'database_name')
