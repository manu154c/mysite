from django.contrib import admin

from .models import Blog, Author, Entry

#class ChoiceInline(admin.StackedInline):
#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 3

class EntryAdmin(admin.ModelAdmin):
    """
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    """
    
    fieldsets = [
        ('Title',               {'fields': ['headline']}),
        #('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Content', {'fields': ['body_text']}),
    ]
    #inlines = [ChoiceInline]
    
    #list_display = ('question_text', 'pub_date', 'was_published_recently')
    #list_filter = ['pub_date']
    #search_fields = ['question_text']

#admin.site.register(Question, QuestionAdmin)
admin.site.register(Entry, EntryAdmin)
