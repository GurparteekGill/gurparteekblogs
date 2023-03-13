

# Register your models here.

from django.contrib import admin

# Register your models here.
from .models import Post,PostextraImages

# Register your models here.
admin.site.register(PostextraImages)
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)

