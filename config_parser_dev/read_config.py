import configparser

config = configparser.ConfigParser()
config.sections()
config.read('example.ini')
print(config['DEFAULT']['compressionlevel'])