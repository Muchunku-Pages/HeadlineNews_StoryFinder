from flask import render_template
from . import home


@home.route('/')
def (home):
  '''
  Returns the home page landing page and its data content
  '''
 
  return render_template('home.html')

@home.route('/article')
def article():

    '''
    Returns the article page containing the various article details and data
    '''
   
   
    return render_template('article.html')

@home.route('/category/')
def category(category_name):
    '''
     Returns the category.html page and its content
    '''
    category = get_category(category_name)
    title = get_category(f'{category_name}')
    category_name = category

    return render_template('categories.html')