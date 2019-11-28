from django.contrib import admin

from .models import Survey, SurveyResponse, User


admin.site.register(Survey)
admin.site.register(SurveyResponse)
admin.site.register(User)
