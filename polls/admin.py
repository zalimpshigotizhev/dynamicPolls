from django.contrib import admin
from polls.models import Question, Poll, Choice, UserResponse


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    fk_name = 'question'


class QuestionInline(admin.TabularInline):
    model = Question
    fields = ['question_text']
    max_num = 1
    extra = 1


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    inlines = [ChoiceInline]
    actions = ['delete_activity_selected']
    fieldsets = [
        (None, {"fields": ["question_text"], },),
        ('Статистика', {'fields': ['numbering'],}),
        ('Информация по дататайму', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'numbering', 'respondents_count')

    def delete_activity_selected(self, request, queryset):
        """ Для удалеия статистических данных """
        for question in queryset:
            for choice in question.choices.all():
                choice.votes = 0
                choice.save()

            question.respondents_count = 0
            question.save()


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    pass
