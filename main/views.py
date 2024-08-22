from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Course, CoursePage

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_index.html', {'courses': courses})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    courses = Course.objects.all()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'all_courses': courses,
        'current_course': course,
    })

def course_page_detail(request, course_slug, page_slug):
    course = get_object_or_404(Course, slug=course_slug)
    page = get_object_or_404(CoursePage, course=course, slug=page_slug)
    courses = Course.objects.all()
    pages = list(course.pages.all())
    page_index = pages.index(page)

    return render(request, 'courses/course_page_detail.html', {
        'course': course,
        'page': page,
        'all_courses': courses,
        'current_course': course,
	'prev_page': pages[page_index - 1] if page_index > 0 else None,
        'next_page': pages[page_index + 1] if page_index < len(pages) - 1 else None,

    })


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def policy(request):
    return render(request, 'policy.html')

def terms(request):
    return render(request, 'terms.html')

def contact(request):
    return render(request, 'contact.html')