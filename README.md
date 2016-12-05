Python script for a static blog 
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
* Pygments (Only if you need source code syntax highlighting)

You can install the required libraries with pip (or easy_install):

    pip install jinja2 markdown pygments

Yeah, that's it!

Configuration
--------------

I decided to use no more than a single `Python` file, so the configuration is done in the same script file (at the beginning).

The configuration is as follow:

* **LOCALE**: Locale for use on dates formats and other backend stuff related to localization in `Python`.
       
         LOCALE = 'es_DO.UTF-8'

* **DEFAULT_LANG**: Default language for articles, goes on meta tag in the website. You can change the language for specific blog post (as stated later in this document).
       
         DEFAULT_LANG = 'es'  

* **DATE_FORMAT**: Date format to use in the articles date.
     
        DATE_FORMAT = '%Y-%m-%d'

* **TAGS**: General tags for the website, goes in the meta tag.
       
         TAGS = ['Programación', 'Linux']

* **BLOG_NAME**: Name of the blog, this is used for the title on <head></head> and the website header (with my template of course, one can use it as wants it).
        
        BLOG_NAME = 'My Awesome blog name' 

* **AUTHOR**: Name of the blog's author, when templates rendered it goes on meta tag.
 
        AUTHOR = 'Juan Perez'

* **BLOG_DESCRIPTION**: Blog description, it goes on meta tag.
        
        BLOG_DESCRIPTION = 'Apuntes y notas de un newbie.'

* **INDEX_FILE**: The template file to render for generate de index file (using `Jinja2`).
        
        INDEX_FILE = "index.html"

* **THEME_DIR**: The directoty container for `TEMPLATES_DIR` and `STYLES_DIR` directories.

        THEME_DIR = 'theme/'

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

* **SOURCE_FILE_EXT**: Extension of `Markdown` files
       
         SOURCE_FILE_EXT = 'md' 

* **OUTPUT_FILE_EXT**: Extension of html files.

        OUTPUT_FILE_EXT = 'html'
        
* **COPY_SOURCE_FILES_TO_OUTPUT**: Indicate if should copy sources files (markdown files) from `SOURCE_DIR` to output directory `HTML_DIR`.

        COPY_SOURCE_FILES_TO_OUTPUT = True

How to create a new entry
-------------------------

Very simple, just create your file with an extension as `SOURCE_FILE_EXT` in the directory `SOURCE_DIR` 
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
        
* **author**: Author of the article, if not specified the configuration variable `AUTHOR` will be used. It's optional.

**Note**: All annotations are obligatory, except `slug`, `lang` and `author` as stated above.

A blog post example:

    title: Back to present II!
    tags: insane, sci-fi, parody
    date: 2016-01-25
    slug: back-again
    lang: en
    author: The Doctor
    
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed 
    eiusmod tempor incidunt ut labore et dolore magna aliqua. 
    
    Ut enim ad minim veniam, quis nostrud exercitation ullamco 
    laboris nisi ut aliquid ex ea commodi consequat. Quis aute 
    iure reprehenderit in voluptate velit esse cillum dolore 
    eu fugiat nulla pariatur. 
    
    Excepteur sint obcaecat cupiditat non proident, sunt in culpa 
    qui officia deserunt mollit anim id est laborum.

Generate website
----------------

For this, just run the script as follow:

    python nitido.py
    
Peace out!

