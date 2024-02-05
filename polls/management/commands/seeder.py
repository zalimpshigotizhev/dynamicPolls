import csv
import os
import pprint as pp
import time
from django.core.management.base import BaseCommand
from polls.models import Poll, Question, Choice


def get_data(url):
    with open(url, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        data = list(reader)
        return data


def questions_in_csv():
    with open('polls/management/commands/questions.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        questions = Question.objects.all()
        writer.writerow(['id', 'question_text', 'pub_date', 'respondents_count'])
        for question in questions:
            writer.writerow([question.id, question.question_text, question.pub_date, question.respondents_count])


def choices_in_csv():
    with open('polls/management/commands/choices.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        questions = Choice.objects.all()
        writer.writerow(['id', 'choice_text', 'votes', 'question_id', 'next_question_id'])
        for question in questions:
            writer.writerow([question.id, question.choice_text, question.votes, question.question_id, question.next_question_id])


def seed_quests():
    questions = get_data('polls/management/commands/movies_quests.csv')
    for question in questions:
        new_question = Question(question_text=question['question_text'], id=question['id'])
        new_question.save()


def seed_choices():
    choices = get_data('polls/management/commands/movies_choices.csv')
    for choice in choices:
        new_choice = Choice(choice_text=choice['choice_text'], question_id=choice['question_id'], next_question_id=choice['next_question_id'])
        new_choice.save()


def seed_polls():
    poll = Poll.objects.create(name="Фильмы", question=Question.objects.filter(id=1)[0])
    poll.save()
    
def seed_all():
    seed_quests()
    seed_choices()
    seed_polls()
    print("Готово. Данные загружены в базу.")


class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **options):
        # Здесь поместите вашу логику сидера

        # current_directory = os.getcwd()
        seed_all()
