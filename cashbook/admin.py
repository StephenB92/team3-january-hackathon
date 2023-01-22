from django.contrib import admin
from .models import Cashbook


@admin.register(Cashbook)
class CashbookAdmin(admin.ModelAdmin):
    """ Settings for the admin  panel """

    prepopulated_fields = {'slug': ('book_title',)}
    list_filter = ('status', 'created_on')
    list_display = ('status', 'created_on', 'slug', 'book_title')
    search_fields = ('book_title', 'book_category')


# Register your models here.
