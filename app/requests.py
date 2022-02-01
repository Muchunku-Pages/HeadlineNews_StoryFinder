import urllib.request,json
from .models import Article, Category, Source , Headlines

# Getting api key
api_key = None
# Getting source url
source_url= None
# Getting source url
category_url= None

def configure_request(app):
    global api_key, source_url, category_url
    api_key = app.config['NEWS_API_KEY']
    source_url= app.config['NEWS_API_SOURCE_URL']
    category_url=app.config['CATEGORY_API_URL']


def get_source():
    '''
    Retrieve the stringified json response to url request
    '''
    get_source_url= source_url.format(api_key)
    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_result = None

        if get_source_response['sources']:
            source_result_list = get_source_response['sources']
            source_result = process_result(source_result_list)

    return source_result

def process_results(source_list):
    '''
    Process and transform result data into a list of objects
    Args:
        source_list: dictionary containing source item objects
    Returns:
        source_results: Returned list of source  item  object instances
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)

    return source_results

def article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.load(article_source_data)#

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_result = process_article_result(article_source_list)


    return article_source_result

def process_article_result(news):
    '''
    Process the json articles files from the api key
    '''
    article_source_result = []
    for article in news:
        author = article.get('author')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get ('title')

        if url:
            article_object = Article(author,description,time,image,url,title)
            article_source_result.append(article_objects)

    return article_source_result

def get_category(category_name):
    '''
    Obtain the category data from the retrieved stringified json category results
    '''
    get_category_url = category_url.format(category_name,api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        get_category_result = None

        if get_category_response['articles']:
            get_category_list = get_category_response['articles']
            get_category_result = process_article_result(get_category_list)

    return get_category_result

def get_headline():
    '''
    Obtain the headline data from the retrieved stringified json headline results
    '''
    get_headline_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headline_url) as url:
        get_headline_data = url.read()
        get_headline_response = json.loads(get_headline_data)

        get_headline_results = None

        if get_headline_response['articles']:
            get_headline_list = get_headline_response['articles']
            get_headline_result = process_article_result(get_headline_list)

    return get_headline_result