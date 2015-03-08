#!/usr/bin/env python

from os import listdir
from os.path import isfile, join, basename
import sys
import jinja2
import markdown

# The template file to render, compatible with Jinja2
TEMPLATE_FILE = "/home/lex/code/python/blog-engine/template/template.jinja2"

# The directory of the source files in format markdown
SOURCE_DIR="/home/lex/code/python/blog-engine/source/"

# The output file where store the generated files
HTML_DIR="/home/lex/code/python/blog-engine/html/"

# Initialize jinja2 objects
templateLoader = jinja2.FileSystemLoader(searchpath="/")
templateEnv = jinja2.Environment( loader=templateLoader )
template = templateEnv.get_template( TEMPLATE_FILE )

def convert_to_markdown(text):
    ''' Parse markdown formatted text into html '''
    html = markdown.markdown(text)
    return html

def generate_article(date, title, content, tags, file_name):
    ''' Generate article output file, render from jinja2 to html '''
    templateVars = { "title" : title,
        "content" : content,
        "date" : date, 
        "tags" : tags
        }
    outputText = template.render( templateVars )
    f = open(join(HTML_DIR, file_name), 'w')
    f.write(outputText)
    print("File name %s successfully proccessed by Jinja2!" % (basename(f.name)))
    f.close()

if __name__ == "__main__":
    sources = [ f for f in listdir(SOURCE_DIR) if isfile(join(SOURCE_DIR, f)) and f[-2:] == "md"]
    print("Found %d files to be processed!" % (len(sources)))
    for entry in sources:
        file = open(join(SOURCE_DIR, entry), 'r')
        header = True
        content = date = title = ''
        tags = []
        for line in file:
            values = line.split(':')
            if header and len(values) == 2:
                if values[0].strip() == 'title':
                    title = values[1]
                elif values[0].strip() == 'tags':
                    tags = values[0].split(',')
                elif values[0].strip() == 'date':
                    date = values[1]
            else:
                if header: header = False
                content = content + line
        if len(title) < 2:
            print("Tag title is required in header file!")
            print("File name: " + file.name)
            print("Exiting now!")
            sys.exit(-1)
        elif len(tags) == 0:
            print("Tag tags is required in header file, you must provide at least one tag to the article!")
            print("File name: " + file.name)
            sys.exit(-1)
        elif len(date) < 2:
            print("Tab date is required in header file!")
            print("File name: " + file.name)
            sys.exit(-1)
        else:
            content = convert_to_markdown(content)
            generate_article(date, title, content, tags, basename(file.name)[:-2] + "html") 
        file.close()

    print("All file proccessed successfully!")

# vim: tabstop=8  expandtab  shiftwidth=4  softtabstop=4
