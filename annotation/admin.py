from django.contrib import admin
from .models import Article,Annotation,Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Annotation)
admin.site.register(Comment)