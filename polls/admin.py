from django.contrib import admin
from .models import Question,Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Statement',{'fields':['question_text']}),
                 ('Date information', {'fields':['pub_date'],'classes':['collapse']})
    ]

    inlines = [ChoiceInline]#Choice 모델 클래스 같이 보기

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)