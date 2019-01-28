from django.contrib import admin
from .models import Category,Listing

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    #prepopulated_fields = {'slug': ('name',)}

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category',)
    #prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Listing, ListingAdmin)
