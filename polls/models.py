from django.db import models
from django.utils import timezone


class Question(models.Model):

    question_text = models.CharField(
        verbose_name="Текст вопроса",
        max_length=200
    )

    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        default=timezone.now
    )

    respondents_count = models.IntegerField(
        verbose_name='Количество ответивших',
        default=0
    )

    numbering = models.IntegerField(
        verbose_name="Нумерация",
        default=0
    )

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="Вариант ответа",
        related_name="choices"
    )

    choice_text = models.CharField(
        verbose_name="Текст варианта ответа",
        max_length=200
    )

    next_question = models.ForeignKey(
        Question,
        on_delete=models.SET_NULL,
        verbose_name="Следующий вопрос",
        null=True,
        blank=True,
        related_name="next_choices"
    )

    votes = models.IntegerField(
        verbose_name="Количество голосов",
        default=0
    )

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'


class Poll(models.Model):
    name = models.CharField(
        verbose_name="Название опроса",
        max_length=200
    )

    question = models.ForeignKey(
        verbose_name="Если вариант отвечает на вопрос",
        to=Question,
        on_delete=models.CASCADE
    )

    count_passes = models.IntegerField(
        verbose_name="Количество проходов",
        default=0,
    )

    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        default=timezone.now
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class UserResponse(models.Model):
    user = models.CharField(
        verbose_name="Пользователь, ответивший на опрос",
        default="Anonymous",
        max_length=200,
        null=True,
        blank=True
    )

    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        verbose_name="Опрос, на который отвечал пользователь"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="Вопрос, на который был дан ответ"
    )

    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        verbose_name="Выбранный вариант ответа"
    )

    def __str__(self):
        return f"Ответ пользователя {self.user} на вопрос: {self.question.question_text}"

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'

