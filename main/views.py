from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def courses(request):
    return render(request, 'courses/index.html')


def coursespy(request):
    return render(request, 'courses/python/index.html')

def pythonintro(request):
    h1 = "Python Introduction"
    prev = reverse('coursespy')
    next = reverse('pythonstart')
    return render(request, 'courses/python/introduction.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonstart(request):
    h1 = "Getting Started with Python"
    prev = reverse('pythonintro')
    next = reverse('pythonsyntax')
    return render(request, 'courses/python/starting.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonsyntax(request):
    h1 = "Python Syntax"
    prev = reverse('pythonstart')
    next = reverse('pythoncomments')
    return render(request, 'courses/python/syntax.html', {'h1': h1, 'prev': prev, 'next': next})

def pythoncomments(request):
    h1 = "Python Comments"
    prev = reverse('pythonsyntax')
    next = reverse('pythonvariables')
    return render(request, 'courses/python/comments.html', {'h1': h1, 'prev': prev, 'next': next})


def pythonvariables(request):
    h1 = "Python Variables"
    prev = reverse('pythoncomments')
    next = reverse('pythondatatypes')
    return render(request, 'courses/python/variables.html', {'h1': h1, 'prev': prev, 'next': next})


def pythondatatypes(request):
    h1 = "Python Data Types"
    prev = reverse('pythonvariables')
    next = reverse('pythonnumbers')
    return render(request, 'courses/python/datatypes.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonnumbers(request):
    h1 = "Python Numbers"
    prev = reverse('pythondatatypes')
    next = reverse('pythoncasting')
    return render(request, 'courses/python/numbers.html', {'h1': h1, 'prev': prev, 'next': next})

def pythoncasting(request):
    h1 = "Python Casting"
    prev = reverse('pythonnumbers')
    next = reverse('pythonstrings')
    return render(request, 'courses/python/casting.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonstrings(request):
    h1 = "Python Strings"
    prev = reverse('pythoncasting')
    next = reverse('pythonbooleans')
    return render(request, 'courses/python/strings.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonbooleans(request):
    h1 = "Python Booleans"
    prev = reverse('pythonstrings')
    next = reverse('pythonoperators')
    return render(request, 'courses/python/booleans.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonoperators(request):
    h1 = "Python Operators"
    prev = reverse('pythonbooleans')
    next = reverse('pythonlists')
    return render(request, 'courses/python/operators.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonlists(request):
    h1 = "Python Lists"
    prev = reverse('pythonoperators')
    next = reverse('pythontuples')
    return render(request, 'courses/python/lists.html', {'h1': h1, 'prev': prev, 'next': next})

def pythontuples(request):
    h1 = "Python tuples"
    prev = reverse('pythonlists')
    next = reverse('pythonsets')
    return render(request, 'courses/python/tuples.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonsets(request):
    h1 = "Python Sets"
    prev = reverse('pythontuples')
    next = reverse('pythondictionaries')
    return render(request, 'courses/python/sets.html', {'h1': h1, 'prev': prev, 'next': next})

def pythondictionaries(request):
    h1 = "Python Dictionaries"
    prev = reverse('pythonsets')
    next = reverse('pythonifelse')
    return render(request, 'courses/python/dictionaries.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonifelse(request):
    h1 = "Python If...Else"
    prev = reverse('pythondictionaries')
    next = reverse('pythonwhileloop')
    return render(request, 'courses/python/ifelse.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonwhileloop(request):
    h1 = "Python While Loop"
    prev = reverse('pythonifelse')
    next = reverse('pythonforloop')
    return render(request, 'courses/python/whileloop.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonforloop(request):
    h1 = "Python For Loop"
    prev = reverse('pythonwhileloop')
    next = reverse('pythonfunctions')
    return render(request, 'courses/python/forloop.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonfunctions(request):
    h1 = "Python Functions"
    prev = reverse('pythonforloop')
    next = reverse('pythonlambda')
    return render(request, 'courses/python/functions.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonlambda(request):
    h1 = "Python Lambda"
    prev = reverse('pythonfunctions')
    next = reverse('pythonarrays')
    return render(request, 'courses/python/lambda.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonarrays(request):
    h1 = "Python Arrays"
    prev = reverse('pythonlambda')
    next = reverse('pythonclasses')
    return render(request, 'courses/python/arrays.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonclasses(request):
    h1 = "Python Classes and Objects"
    prev = reverse('pythonarrays')
    next = reverse('pythoninheritance')
    return render(request, 'courses/python/classes.html', {'h1': h1, 'prev': prev, 'next': next})

def pythoninheritance(request):
    h1 = "Python Inheritance"
    prev = reverse('pythonclasses')
    next = reverse('pythoniterators')
    return render(request, 'courses/python/inheritance.html', {'h1': h1, 'prev': prev, 'next': next})

def pythoniterators(request):
    h1 = "Python Iterators"
    prev = reverse('pythoninheritance')
    next = reverse('pythonpolymorphism')
    return render(request, 'courses/python/iterators.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonpolymorphism(request):
    h1 = "Python Polymorphism"
    prev = reverse('pythoniterators')
    next = reverse('pythonscope')
    return render(request, 'courses/python/polymorphism.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonscope(request):
    h1 = "Python Scope"
    prev = reverse('pythonpolymorphism')
    next = reverse('pythonmodules')
    return render(request, 'courses/python/scope.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonmodules(request):
    h1 = "Python Modules"
    prev = reverse('pythonscope')
    next = reverse('pythondates')
    return render(request, 'courses/python/modules.html', {'h1': h1, 'prev': prev, 'next': next})

def pythondates(request):
    h1 = "Python Dates"
    prev = reverse('pythonmodules')
    next = reverse('pythonmath')
    return render(request, 'courses/python/dates.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonmath(request):
    h1 = "Python Math"
    prev = reverse('pythondates')
    next = reverse('pythonjson')
    return render(request, 'courses/python/math.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonjson(request):
    h1 = "Python JSON"
    prev = reverse('pythonmath')
    next = reverse('pythonregex')
    return render(request, 'courses/python/json.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonregex(request):
    h1 = "Python Regex"
    prev = reverse('pythonjson')
    next = reverse('pythonpip')
    return render(request, 'courses/python/regex.html', {'h1': h1, 'prev': prev, 'next': next})


def pythonpip(request):
    h1 = "Python PIP"
    prev = reverse('pythonregex')
    next = reverse('pythontryexcept')
    return render(request, 'courses/python/pip.html', {'h1': h1, 'prev': prev, 'next': next})

def pythontryexcept(request):
    h1 = "Python Try...Except"
    prev = reverse('pythonpip')
    next = reverse('pythonuserinput')
    return render(request, 'courses/python/tryexcept.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonuserinput(request):
    h1 = "Python User Input"
    prev = reverse('pythontryexcept')
    next = reverse('pythonstringformatting')
    return render(request, 'courses/python/userinput.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonstringformatting(request):
    h1 = "Python String Formatting"
    prev = reverse('pythonuserinput')
    next = reverse('pythonfilehandling')
    return render(request, 'courses/python/stringformating.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonfilehandling(request):
    h1 = "Python File Handling"
    prev = reverse('pythonstringformatting')
    next = reverse('pythonfileopen')
    return render(request, 'courses/python/filehandling.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonfileopen(request):
    h1 = "Python File Open"
    prev = reverse('pythonfilehandling')
    next = reverse('pythonfilewritecreate')
    return render(request, 'courses/python/fileopen.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonfilewritecreate(request):
    h1 = "Python File Write and Create"
    prev = reverse('pythonfileopen')
    next = reverse('pythonfiledel')
    return render(request, 'courses/python/filewritecreate.html', {'h1': h1, 'prev': prev, 'next': next})

def pythonfiledel(request):
    h1 = "Python File Delete"
    prev = reverse('pythonfilewritecreate')
    next = ''
    clas = 'disabled'
    return render(request, 'courses/python/filedel.html', {'h1': h1, 'prev': prev, 'next': next, 'clas': clas})

'''
JAVASCRIPT
IS 
THE 
KING
OF
THE 
WEB


'''
