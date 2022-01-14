from django.contrib import admin
from polls.models import Poll, Question, Choice
import nested_admin
    
class ChoiceInline(nested_admin.NestedStackedInline):
    model = Choice
    extra = 1

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]
    
class PollAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]
    readonly_fields = ['date_start']


admin.site.register(Poll, PollAdmin)
