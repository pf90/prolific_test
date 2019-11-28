from django.urls import path

from .views import SurveyView, SurveyResponseView 


app_name = "surveys"


urlpatterns = [
    path('surveys/', SurveyView.as_view()),
    path('survey_responses/', SurveyResponseView.as_view()),
]