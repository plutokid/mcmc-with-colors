from django.conf.urls import patterns, url

from colortask import views


urlpatterns = patterns('',
	url(r'^instructions/$',views.instructions, name='instructions'),
	url(r'^instructions-mturk/$',views.instructions_mturk),
    url(r'^stage/$',views.stage, name='stage'),
    url(r'^conclusion/$',views.conclusion, name='conclusion'),
    url(r'^proposal/$',views.proposal, name='proposal'),
    url(r'^saveQuestionData/$',views.saveQuestionData, name='saveQuestionData'),
    # url(r'^saveParticipantData/$',views.saveParticipantData, name='saveParticipantData'),
)