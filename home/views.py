from django.shortcuts import render

def index(request):
    return render(request, "home/index.html", {})

def memorama_view(request):
    return render(request, 'Memo/memorama.html',{})


def Web_view(request):
    return render(request, 'static/Web/index.html',{})

def challenges_view(request):
    return render(request, 'home/challenges.html',{})

def resources_view(request):
    return render(request, 'home/resources.html',{})

def solutions_view(request):
    return render(request, 'home/solutions.html',{})

def takeaction_view(request):
    return render(request, 'home/take-action.html',{})

#css
def stilo_view(request):
    return render(request, 'static/style/baseStyle.css',{})
def stilos_view(request):
    return render(request, 'static/stiles/layout.css',{})

