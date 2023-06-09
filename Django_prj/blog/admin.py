from django.contrib import admin
from .models import Post, Tag
from .models import Category

admin.site.register(Post)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
# Register your models here.