from django.conf.urls import url

from . import views
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>[0-9]+)/details/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/details/(?P<answers_id>[0-9]+)/editcomment/$', views.editcomment, name='editcomment'),
    # url(r'^(?P<question_id>[0-9]+)/details/(?P<answers_id>[0-9]+)/deleteComment/$', views.deleteComment, name='deleteComment'),

    url(r'result/$', views.result_image, name= 'result_image'),
    # url(r'^post/$', views.post, name='upload'),

    url(r'classification_svm/$', views.classification_svm, name= 'classification_svm'),

    url(r'register_acc/$', views.register_acc, name= 'register_acc')
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #url(r'^deleteComment/(?P<answers_id>[0-9]+)/$', views.deleteComment, name="deleteComment"),
]
