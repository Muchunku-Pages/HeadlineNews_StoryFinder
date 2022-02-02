from flask import render_template,request,redirect,url_for
from . import home
from ..request import get_source,article_source,get_category,get_headline


@home.route('/')
def home():


  '''
  Returns the home page landing page and its data content
  '''
 
  source= get_source()
  headline = get_headline()
  return render_template('home.html',source=source, headline = headline)

@home.route('/article')
def article():
  
  '''
  Returns the article page containing the various article details and data
  '''
   
   
  article = article_source(id)
  return render_template('article.html',article= article,id=id )

@home.route('/category/<category_name>')
def category(category_name):
  
    '''
    Return the category.html page and its content
    '''
   

    category = get_category(category_name)
    title = get_category(f'{category_name}')
    category = category

    return render_template('category.html',title = title, category = category)