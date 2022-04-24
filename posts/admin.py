from django.contrib import admin
from .models import Post,Category
# Register your models here.
admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  

admin.site.register(Post, PostAdmin)