from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.text import slugify

class Course(models.Model):
    title = models.CharField(max_length=200)
    list_description = models.TextField(default='Default list description') 
    description = models.TextField(default='desc')
    banner_image = models.ImageField(upload_to='course_banners/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class CoursePage(models.Model):
    course = models.ForeignKey(Course, related_name='pages', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    def get_content_as_markdown(self):
        return markdownify(self.content)

    def get_absolute_url(self):
        return f"/courses/{self.course.slug}/{self.slug}/"
