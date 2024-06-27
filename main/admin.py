from django.contrib import admin
from .models import Course, CoursePage

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(CoursePage)
class CoursePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'slug')
    prepopulated_fields = {'slug': ('title',)}
