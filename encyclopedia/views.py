from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import Markdown
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

markdowner = Markdown()

# entry page view 
def entry_page(request, title):
   # If an entry is requested that does not exist, 
   # the user should be presented with an error page 
   # indicating that their requested page was not found.

   #1. check the entry exist or not.
   entry = util.get_entry(title)
   if entry == None:
       return render(request, "encyclopedia/error.html", { 
           "title": "something went wrong",
           "message": f"{title} not found!"
       })
   else:
       return render(request, "encyclopedia/entryPage.html", {
           "title": title,
           "content":markdowner.convert(util.get_entry(title))
       })
       
   