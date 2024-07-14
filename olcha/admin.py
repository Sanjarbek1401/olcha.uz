from django.contrib import admin

from .models import Category,Group


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug':('category_name',)}

@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'slug']
    prepopulated_fields = {'slug':('group_name',)}
