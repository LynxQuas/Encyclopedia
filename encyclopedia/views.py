from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import Markdown
from . import util
import random

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

# New page
def newpage(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        if not title or not content:
            return render(request, "encyclopedia/error.html", {
                    "title": "something went wrong",
                    "message": "Input is empty"
            })
        existing_entry = util.get_entry(title)
        if existing_entry:
            return render(request, "encyclopedia/error.html", {
                    "title": "something went wrong",
                    "message": "Page Already Exist."
            })
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/entryPage.html", {
                "title": title,
                "content":markdowner.convert(util.get_entry(title))
       })
    else:
         return render(request, "encyclopedia/newpage.html")


# RANDOM PAGE
def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return render(request, "encyclopedia/entryPage.html", { 
        "title": random_entry,
        "content": markdowner.convert(util.get_entry(random_entry))
    })
    
# Edit Page 
def edit(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = util.get_entry(title)

        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content" : content
        })

# save the edited page.
def save(request):
    title = request.POST.get("title")
    content = request.POST.get("content", "")
    util.save_entry(title, content)
    return render(request, "encyclopedia/entryPage.html", {
        "title": title,
        "content": markdowner.convert(content)
    })

         


    

   

            
        
        