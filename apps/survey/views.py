from django.shortcuts import render, redirect

def index(request):
    return render(request, "survey/index.html")

def getData(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        request.session['counter'] += 1
        return redirect('/result')

def displayResult(request):
    name = request.session['name']
    location = request.session['location']
    language = request.session['language']
    comments = request.session['comments']
    dictionary = {
        'name': name,
        'location': location,
        'language': language,
        'comments': comments,
    }
    return render(request, "survey/results.html", dictionary)

def goBack(request):
    return redirect('/')

# Create your views here.
