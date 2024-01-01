from django.shortcuts import render, redirect
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Path: encyclopedia/views.py

def entry(request, title):
    entry_content = util.get_entry(title)
    if entry_content is None:
        return render(request, "encyclopedia/error.html", {
            "error_message": f"The requested page '{title}' was not found."
        })
    else:
        html_content = markdown2.markdown(entry_content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": html_content
        })


def search(request):  # new search view
    query = request.GET.get('q', '')
    entries = util.list_entries()
    if query in entries:
        return redirect('entry', title=query)
    else:
        results = [entry for entry in entries if query.lower() in entry.lower()]
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "results": results
        })

def new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        entries = util.list_entries()
        if title in entries:
            return render(request, "encyclopedia/error.html", {
                "error_message": f"The page '{title}' already exists."
            })
        else:
            util.save_entry(title, content)
            return redirect('entry', title=title)
    else:
        return render(request, "encyclopedia/new.html")

def edit(request, title):
    if request.method == "POST":
        content = request.POST.get('content')
        util.save_entry(title, content)
        return redirect('entry', title=title)
    else:
        entry_content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "entry": entry_content
        })

def random(request):
    import random
    entries = util.list_entries()
    title = random.choice(entries)
    return redirect('entry', title=title)