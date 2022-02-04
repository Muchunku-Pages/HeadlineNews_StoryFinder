import os

class Config:
    '''
    Configuration Parent class
    Args:
        Config: The parent configuration class with General configuration settings
    '''


    NEWS_API_KEY = '5f0592b7382649419c1d6083116ac3a5'
    SECRET_KEY = '1234567'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    CATEGORY_API_URL = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'  # Getting api key


class ProdConfig(Config):
    '''
    Configuration Production Child class
    Args:
        Config: A child configuration class with Production configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Configuration Development Child class

    Args:
         Config: A child configuration class with Development configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}