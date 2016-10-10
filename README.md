A simple Python script to generate and maintain a static blog 
=============================================================

This is just a simple `Python` script to maintain my blog, it's pretty
minimal. Articles are written in [Markdown](https://en.wikipedia.org/wiki/Markdown) format in 
plain text.

For creating the `HTML` templates [Jinja2](http://jinja.pocoo.org/) is used.

Requirements
-------------

* Python 2
* Jinja2
* Markdown

Yeah, that's it!

Configuration
--------------

I decided to use no more than a single `Python` file, so the configuration is done in the same script file (at the beginning).
The configuration is as follow:

* **LOCALE**: Locale for use on dates formats and other backend stuff related to localization in `Python`.
       
         LOCALE = 'es_DO.UTF-8'

* **DEFAULT_LANG**: Default language for articles, goes on meta tag in the website. You can change the language for specific blog post (as stated later in this document).
       
         DEFAULT_LANG = 'es'  

* **TAGS**: General tags for the website, goes in the meta tag.
       
         TAGS = ['Programación', 'Linux']

* **BLOG_NAME**: Name of the blog, this is used for the title on <head></head> and the website header (with my template of course, one can use it as wants it).
        
        BLOG_NAME = 'My Awesome blog name' 

* **DATE_FORMAT**: Date format to use in the articles date.
     
        DATE_FORMAT = '%Y-%m-%d'

* **INDEX_FILE**: The template file to render for generate de index file (using `Jinja2`).
        
        INDEX_FILE = "index.html"

* **ARTICLE_FILE**: Template file to render for generate the article/post (using `Jinja2`).
        
        ARTICLE_FILE = 'article.html' 

* **TEMPLATES_DIR**: Templates directory of `Jinja2` files.
        
        TEMPLATES_DIR = 'templates' 

* **STATIC_PAGES**: List of static html pages, wich will not be proccessed with `Markdown`.
        
        STATIC_PAGES = ['about.html']

* **SOURCE_DIR**: The directory of the plain text files in format `Markdown` to generate the posts
        
        SOURCE_DIR = 'source/' 

* **IMAGES_DIR**: Directory name of blog images.
        
        IMAGES_DIR = 'images/'

* **STYLES_DIR**: Directory name of css styles file
        
        STYLES_DIR = 'css/' 

* **HTML_DIR**: The output directory where the generated files will be put.
        
        HTML_DIR = 'html/'

* **EXT**: Extension of `Markdown` files
       
         EXT = 'md' 

How to create a new entry
-------------------------

Veyr simple, just create your file with a extension as `EXT` in the directory `SOURCE_DIR` 
that you set up in the script and use `Markdown` format as you wish. There are some annotations that you must put in the beginning 
of the article/post file in plain text. These are the next:

* **title**: The title of the blog post.

        title: First new blog post!

* **tags**: List of tags of the blog post.
 
        tags: unix, python, markdown

* **date**: Date of the blog post, it should have the same format as stated in the configuration variable `DATE_FORMAT`.
 
        date: 2016-10-10

* **slug**: Just in case you want a name for the post file different than the psot title. It's optional.
 
        slug: first-post

* **lang**: Language of the article/post, if not specified the configuration variable `DEFAULT_LANG` will be used. It's optional. 

        lang: en

**Note**: All annotations are obligatory, except `slug`.

Generate website
----------------

For this, just run the script as follow:

    python nitido.py
    
**Note**: For testing purposes (or as starting point project) you could just clone the entire repository and run the command above, it will generate a blog with
the predefined setting and some test articles. Otherwise, you just need the `Python` script and customize as you want.
    
Peace out!
