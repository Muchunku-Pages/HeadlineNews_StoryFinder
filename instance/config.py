#NEWS_API_KEY = 'd5cb1c4606844f8b91883d48a41ffbe0'

import os

class Config:
    '''
     Configuration Parent class
      Args:
        Config: The parent configuration class with General configuration settings
    '''
    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    # CAT_API_URL='https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    CAT_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'




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