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

# Search
def search(request):
    if request.method == "POST":
        # get the input.
        title = request.POST.get("q", "")
        entries = util.list_entries()
        # if the input is empty.
        if not title: 
            return render(request, "encyclopedia/error.html", {
                    "title": "something went wrong",
                    "message": "Input is empty"
            })
        # sub string matches.
        substring_match = [entry for entry in entries if title.lower() in entry.lower()]
        if substring_match:
            return render(request, "encyclopedia/search.html", {
            "result": substring_match
        })
        # if page is not exist.
        else:
            return render(request, "encyclopedia/error.html", {
                    "title": "something went wrong",
                    "message": "Page does not exist."
            })

            
        
        