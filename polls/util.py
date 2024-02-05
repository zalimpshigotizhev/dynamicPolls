import pprint as pp
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.db import connection


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0]for col in desc], row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    desc = cursor.description
    return dict(zip([col[0]for col in desc], cursor.fetchone()))


def add_session_passed_question(request, question_id):
    session = request.session

    if session.get('passed_questions', []):
        session['passed_questions'].append(question_id)
    else:
        session['passed_questions'] = [question_id]
    session.save()


def check_poll_passed(request, poll_id):
    session = request.session
    if session.get('passed_questions', []):
        return True
    return False


def poll_add_count_passes(request, poll_id):
    cursor = connection.cursor()
    cursor.execute(
        f"""UPDATE polls_poll 
        SET count_passes = count_passes + 1
        WHERE id = {poll_id}"""
    )


def percentage_ratio(number, all):
    if all == 0:
        return 0
    return round((number / all) * 100, 2)


def choices_percentage_ratio(question, all_votes):
    for choice in question['choices']:
        choice['percentage'] = percentage_ratio(choice['votes'], all_votes)


def delete_session_passed_questions(request):
    if 'passed_questions' in request.session:
        del request.session['passed_questions']


def select_all_polls():
    cursor = connection.cursor()
    cursor.execute("""SELECT *
                   FROM polls_poll""")
    return dictfetchall(cursor)


def select_poll_by_id(id, columns='*'):
    cursor = connection.cursor()
    cursor.execute(f"""SELECT {columns}
                   FROM polls_poll
                   WHERE id = {id}""")
    return dictfetchone(cursor)


def select_question_by_id(id, columns='*'):
    cursor = connection.cursor()
    cursor.execute(f"""SELECT {columns}
                   FROM polls_question
                   WHERE id = {id}""")
    return dictfetchone(cursor)


def select_questions_by_ids(ids, columns='*'):
    ids = ','.join([str(id) for id in ids])
    cursor = connection.cursor()
    cursor.execute(f"""SELECT {columns}
                   FROM polls_question
                   WHERE id IN ({ids})""")
    return dictfetchall(cursor)


def select_choices_by_question_id(id, columns='*'):
    cursor = connection.cursor()
    cursor.execute(f"""SELECT {columns}
                   FROM polls_choice
                   WHERE question_id = {id}""")
    return dictfetchall(cursor)


def select_choice_by_id(id, columns='*'):
    cursor = connection.cursor()
    cursor.execute(f"""SELECT {columns}
                   FROM polls_choice
                   WHERE id = {id}""")
    return dictfetchone(cursor)


def update_respond_count(id):
    cursor = connection.cursor()
    cursor.execute(f"""UPDATE polls_question
                   SET respondents_count = respondents_count + 1
                   WHERE id = {id}""")


def update_vote_count(id):
    cursor = connection.cursor()
    cursor.execute(f"""UPDATE polls_choice
                   SET votes = votes + 1
                   WHERE id = {id}""")


def create_user_response(user, poll_id, question_id, choice_id):
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO polls_userresponse
                   (user, poll_id, question_id, choice_id)
                   VALUES ('{user}', {poll_id}, {question_id}, {choice_id})""")


def get_user_count_passes(request, poll_id):
    cursor = connection.cursor()
    cursor.execute(f"""SELECT COUNT(*)
                   FROM polls_userresponse
                   WHERE poll_id = {poll_id}""")
    return dictfetchone(cursor)


def select_respondents_count_by_question_id(id):
    cursor = connection.cursor()
    cursor.execute(f"""SELECT COUNT(*)
                   FROM polls_userresponse
                   WHERE question_id = {id}""")
    return dictfetchone(cursor)['COUNT(*)']


def sorted_questions(poll_id):
    cursor = connection.cursor()
    cursor.execute(f"""SELECT question_id, COUNT(*) AS counts
                   FROM polls_userresponse
                   WHERE poll_id = {poll_id}
                   GROUP BY question_id
                   ORDER BY counts DESC""")
    questions = dictfetchall(cursor)
    ids = [item['question_id'] for item in questions]
    counts = [item['counts'] for item in questions]

    dict_result = {}
    curr_number = 1
    for quest in counts:
        if quest not in dict_result:
            dict_result[quest] = curr_number
            curr_number += 1

    numbered_lst = [dict_result[num] for num in counts]
    data = tuple(zip(ids, numbered_lst))

    for item in data:
        cursor.execute(f"""
            UPDATE polls_question
            SET numbering = {item[1]}
            WHERE id = {item[0]}
        """)
    print(data)
    return questions

