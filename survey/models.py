from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Survey(models.Model):
    name = models.CharField(max_length=120)
    available_places = models.PositiveIntegerField()
    user = models.ForeignKey('User', related_name='surveys', on_delete=models.CASCADE)

    @property
    def remaining_places(self):
        return self.available_places - SurveyResponse.objects.filter(survey_id=self.pk).count()

    def __str__(self):
        return self.name


class SurveyResponse(models.Model):
    survey = models.ForeignKey('Survey', related_name='survey_responses', on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name='survey_responses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}".format(self.survey, self.user.name, self.created_at)
        
