from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

# Register your models here.

admin.site.register(Genre)
admin.site.register(Language)

# Define the admin class
class BookInline(admin.TabularInline):
   model = Book
   extra = 0
   can_delete = False
   fields =  ('title', 'summary', 'genre', 'isbn' )
   # list_display = ('title', 'summary', 'display_genre', 'isbn' )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
   model = BookInstance
   extra = 0

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'language', 'status', 'due_back')
    list_filter = ('status', 'due_back', 'language')
    # exclude = ['id']
    # fields = ['book', ('language','imprint'), ('status', 'due_back')]

    fieldsets = (
           (None, {
                'fields': ('book', ('language','imprint'))
           }),
           ('Availability', {
               'fields': (('status', 'due_back'),'borrower')
           }),
    )
