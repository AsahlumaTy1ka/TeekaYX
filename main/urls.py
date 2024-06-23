from django.urls import path
from . import views
from django.contrib import admin


admin.site.site_title = "TeekaYX | Admin"
admin.site.site_header = "TeekaYX | Administration"
admin.site.index_title = "Site administration"

urlpatterns = [
    path('courses/python/introduction/', views.pythonintro, name='pythonintro'),
    path('courses/python/getting_started/', views.pythonstart, name='pythonstart'),
    path('courses/python/python_syntax/', views.pythonsyntax, name='pythonsyntax'),
    path('courses/python/python_comments/', views.pythoncomments, name='pythoncomments'),
    path('courses/python/python_variables/', views.pythonvariables, name='pythonvariables'),
    path('courses/python/python_datatypes/', views.pythondatatypes, name='pythondatatypes'),
    path('courses/python/python_numbers/', views.pythonnumbers, name='pythonnumbers'),
    path('courses/python/python_casting/', views.pythoncasting, name='pythoncasting'),
    path('courses/python/python_strings/', views.pythonstrings, name='pythonstrings'),
    path('courses/python/python_booleans/', views.pythonbooleans, name='pythonbooleans'),
    path('courses/python/python_operators/', views.pythonoperators, name='pythonoperators'),
    path('courses/python/python_lists/', views.pythonlists, name='pythonlists'),
    path('courses/python/python_tuples/', views.pythontuples, name='pythontuples'),
    path('courses/python/python_sets/', views.pythonsets, name='pythonsets'),
    path('courses/python/python_dictionaries/', views.pythondictionaries, name='pythondictionaries'),
    path('courses/python/python_ifelse/', views.pythonifelse, name='pythonifelse'),
    path('courses/python/python_whileloop/', views.pythonwhileloop, name='pythonwhileloop'),
    path('courses/python/python_forloop/', views.pythonforloop, name='pythonforloop'),
    path('courses/python/python_functions/', views.pythonfunctions, name='pythonfunctions'),
    path('courses/python/python_lambda/', views.pythonlambda, name='pythonlambda'),
    path('courses/python/python_arrays/', views.pythonarrays, name='pythonarrays'),
    path('courses/python/python_classes/', views.pythonclasses, name='pythonclasses'),
    path('courses/python/python_inheritance/', views.pythoninheritance, name='pythoninheritance'),
    path('courses/python/python_iterators/', views.pythoniterators, name='pythoniterators'),
    path('courses/python/python_polymorphism/', views.pythonpolymorphism, name='pythonpolymorphism'),
    path('courses/python/python_scope/', views.pythonscope, name='pythonscope'),
    path('courses/python/python_modules/', views.pythonmodules, name='pythonmodules'),
    path('courses/python/python_dates/', views.pythondates, name='pythondates'),
    path('courses/python/python_math/', views.pythonmath, name='pythonmath'),
    path('courses/python/python_json/', views.pythonjson, name='pythonjson'),
    path('courses/python/python_regex/', views.pythonregex, name='pythonregex'),
    path('courses/python/python_pip/', views.pythonpip, name='pythonpip'),
    path('courses/python/python_tryexcept/', views.pythontryexcept, name='pythontryexcept'),
    path('courses/python/python_userinput/', views.pythonuserinput, name='pythonuserinput'),
    path('courses/python/python_stringformatting/', views.pythonstringformatting, name='pythonstringformatting'),
    path('courses/python/python_filehandling/', views.pythonfilehandling, name='pythonfilehandling'),
    path('courses/python/python_fileopen/', views.pythonfileopen, name='pythonfileopen'),
    path('courses/python/python_filewritecreate/', views.pythonfilewritecreate, name='pythonfilewritecreate'),
    path('courses/python/python_filedel/', views.pythonfiledel, name='pythonfiledel'),
    path('courses/python/', views.coursespy,name='coursespy'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),


]
