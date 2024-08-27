from django.contrib import admin
from .models import Author, Quote

# Register your models here.

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'birthday')
#     search_fields = ('name',)

# class QuoteAdmin(admin.ModelAdmin):
#     list_display = ('text', 'author')
#     search_fields = ('text', 'author__name')
#     list_filter = ('author',)

# Не забути додати адмін класи в register у випадку їх активації)

admin.site.register(Author)
admin.site.register(Quote)
