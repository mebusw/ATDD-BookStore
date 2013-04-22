from django.contrib import admin
from book.models import Book, Comment, Author, Bill, UserProfile
'''
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question']
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    
#admin.site.register(Poll)
admin.site.register(Poll, PollAdmin)
'''
'''class MembershipInline(admin.TabularInline):
    model = Book.authors.through

class AuthorAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]
    exclude = ('authors',)
'''
    
class AuthorAdmin(admin.ModelAdmin):
    model = Author
        
class CommentInline(admin.TabularInline):
    model = Comment

class BookAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    
class BillAdmin(admin.ModelAdmin):
    model = Bill
    
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
