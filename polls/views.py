from django.shortcuts import redirect, render
from django.db import connection
from polls import util


def index(request):
    # util.sorted_questions(1)
    util.delete_session_passed_questions(request)

    polls = util.select_all_polls()
    context = {
        'polls': polls
    }

    return render(request, 'polls/index.html', context)


def question_detail(request, poll_id, question_id):
    poll_actual = util.select_poll_by_id(poll_id, 'name')
    quest_actual = util.select_question_by_id(question_id, 'question_text, id')
    choices = util.select_choices_by_question_id(quest_actual['id'], 'choice_text, id, next_question_id')

    context = {
        'poll_id': poll_id,
        'question_id': question_id,
        'nav': poll_actual['name'],
        'quest': quest_actual,
        'choices': choices
    }
    return render(request, 'polls/question_detail.html', context)


def vote(request, poll_id, question_id):
    util.sorted_questions(poll_id)

    if util.check_poll_passed(request, poll_id) is False:
        util.poll_add_count_passes(request, poll_id)

    # session = create_or_get_session(request)
    util.add_session_passed_question(request, question_id)

    select_choice = request.POST.get('vote')    
    choice = util.select_choice_by_id(select_choice, 'id, next_question_id, votes')
    util.update_vote_count(choice['id'])

    next_quest = choice['next_question_id']

    util.create_user_response("Anonymous", poll_id, question_id, select_choice)

    if next_quest is None:
        return redirect('polls:results', poll_id)
    util.update_respond_count(question_id)
    return redirect('polls:detail', poll_id, next_quest)


def results(request, poll_id):
    poll = util.select_poll_by_id(poll_id, 'name, count_passes')

    passed_questions = request.session.get('passed_questions')
    if passed_questions is None:
        return redirect('polls:index')
    questions = util.select_questions_by_ids(passed_questions, '*')

    quest_and_choices = []
    all_votes = 0

    # Тут мы добавляем в вопрос его варианты, число проголосовавших и проценты
    # каждого варианта
    
    for question in questions:
        question['respondents_count'] = util.select_respondents_count_by_question_id(question['id'])
        question['choices'] = util.select_choices_by_question_id(question['id'])
        all_votes += sum(choice['votes'] for choice in question['choices'])
        question['all_votes'] = all_votes
        util.choices_percentage_ratio(question, all_votes)
        question['percentage'] = util.percentage_ratio(all_votes, poll['count_passes'])
        all_votes = 0
        quest_and_choices.append(question)


    context = {
        'poll': poll,
        'nav': 'Результаты опроса',
        'questions': quest_and_choices,
        'count_passes': poll['count_passes'],
    }

    return render(request, 'polls/results.html', context)
