from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [(None, {'fields': ['question_text']}), ('Date information', {'fields': ['publish_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]
    #list_display = ('question_text', 'publish_date') 
    list_display = ('question_text', 'publish_date', 'was_published_recently') 
    list_filter = ['publish_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# Register your models here.
