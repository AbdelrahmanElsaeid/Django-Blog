from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['author','title']
    list_filter = ['tags']
    search_fields = ['title','content']


admin.site.register(Post,PostAdmin)




