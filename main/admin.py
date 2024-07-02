from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Course, CoursePage

#@admin.register(Course)
class CourseAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

#@admin.register(CoursePage)
class CoursePageAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'course', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(CoursePage,CoursePageAdmin)
admin.site.register(Course,CourseAdmin)
