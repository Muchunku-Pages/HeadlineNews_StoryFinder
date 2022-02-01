class Headline:
    '''
    Define the class from which the objects of the headline category of a news source are instantiated
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title


class Article:
    '''
    Define the class from which the objects of the news article of a news source are instantiated
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title  

class Category:
    '''
    Define the class from which the objects of the news category of a news source are instantiated
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title

class Source:
    '''
    Define the class from which the objects of news Source are instantiated
    '''
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
