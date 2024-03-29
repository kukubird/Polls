from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question'] #adds a search box at the top of the cahnge list

admin.site.register(Poll, PollAdmin)
#admin.site.register(Page)
