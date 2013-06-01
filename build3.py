## -*- coding: utf-8 -*-
#!/usr/bin/python3

from mako.lookup import Template,TemplateLookup
from sh import cp,rm,pwd,mv,uglifyjs,cat,glob,cssoptimizer
import markdown
import logging
import os,sys

#Settings
WEBSITE_TITLE = "Ubuntu Faq"
DEFAULT_TAGS = "ubuntu"
SOURCE = "notes.txt"
logging.root.setLevel(logging.DEBUG)
LINKS_ON_PAGE = 20
PAGE_PATTERN = "From%dto%d"
VERSION = 0.2

if (len(sys.argv)>1):
  BASE_URL = sys.argv[1]
else:
  BASE_URL = "file://"+str(pwd()).replace("\n","")+"/_site/"

#Code
def materialize_template(template_name,fname,env):
  os.chdir("_templates")

  env['base_url']=BASE_URL
  env['website_title']=WEBSITE_TITLE
  env['default_tags']=DEFAULT_TAGS
  env['current_url']=BASE_URL+fname+".html"
  env['version']=VERSION
  
  mylookup = TemplateLookup(directories=['.'],input_encoding='utf-8', output_encoding='utf-8', encoding_errors='replace')
  result = Template(filename=template_name+".mako",
    lookup=mylookup,
    default_filters=['decode.utf8']).render(**env) 

  os.chdir("..")
  f = open("_site/"+fname+".html",'w')  
  f.write(result) 
  f.close()

def valid_fname(fname):
  return fname.replace("/","-").replace(".","-").replace("\n","")

def link(title,fname):
  link={}
  link["title"]=title
  link["href"]=BASE_URL+fname+".html"
  return link

def bake_note(title, tags, content):
  env={
    "title": title,
    "tags": tags,
    "content": markdown.markdown(content)
  }

  materialize_template("note",valid_fname(title),env)

def bake_toc(headers):
  chunks=[headers[x:x+LINKS_ON_PAGE] for x in range(0, len(headers), LINKS_ON_PAGE)]

  pages=[]
  n=0
  for chunk in chunks:
    pages.append(link("%d-%d" % (n+1,n+len(chunk)),PAGE_PATTERN % (n,n+LINKS_ON_PAGE)))
    n+=LINKS_ON_PAGE

  n=0
  for chunk in chunks:
    links=[]
    for header in chunk:
      links.append(link(header,valid_fname(header)))

    env={
      "title": "Заметки %d-%d" % (n+1,n+len(chunk)),
      "links": links,
      "pages": pages,
      "start": str(n+1)
    }

    materialize_template("all",PAGE_PATTERN % (n,n+LINKS_ON_PAGE),env)
    n+=LINKS_ON_PAGE


def materialize_notes(source):
  raw=open(source, 'r', encoding='utf-8').readlines()
  
  post_buffer=""
  tags=""
  previous_line=""
  previous_title=""
  headers=[]
  i=0
  l=0

  for line in raw:
    l+=1

    #add additional line before code for markdown parser
    if line[0:4]=="    " and previous_line[1:4]!="   " and previous_line[0]!="#":
      line = "\n" + line

    if line[0:2]=="##" and line[2]!="#":
      if l!=1:
        i+=1
        bake_note(previous_title,tags,post_buffer)
        if i==1:
          bake_note("index",tags,post_buffer)
        post_buffer=""
        tags=""

      previous_title=line[2:]
      headers.append(line[2:])

    elif l==len(raw):
      post_buffer+=line
      bake_note(previous_title,tags,post_buffer)

    elif line[0:4]=="!tag":
      tags=line[6:].replace("\n","")

    else:
      post_buffer+=line
      previous_line=line

  bake_toc(headers)



def main():
  logging.debug('start')

  #clear output directory
  rm("-Rf",glob("_site/*"))
  #copy static contant
  cp("-a",glob("_web/*"),"_site/")
  mv("_site/dot_htaccess","_site/.htaccess")
  #copy optimized css
  cssoptimizer(cat(glob("_css/*")),"-i","_site/style.css")
  #copy optimized js
  uglifyjs(cat(glob("_js/*")),"-o","_site/scripts.js")

  #generate content
  materialize_notes(SOURCE)
  materialize_template("Y_Search","Y_Search",{"title":"Поиск"})

  logging.debug('end.') 
  logging.info('To start copy following url into your browser: \n%sindex.html' % BASE_URL)

if __name__ == "__main__":
    main() 
