from django.contrib import admin
from .models import Post,Question,Post_Question, Category

admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Post_Question)
admin.site.register(Category)

