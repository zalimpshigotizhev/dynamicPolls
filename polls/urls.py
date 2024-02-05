from django.urls import path
from .views import index, question_detail, vote, results


app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('polls/<int:poll_id>/<int:question_id>/', question_detail, name='detail'),
    path('polls/<int:poll_id>/<int:question_id>/vote/', vote, name='vote'),
    path('polls/<int:poll_id>/results/', results, name='results'),
]
