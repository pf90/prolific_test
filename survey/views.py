from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Survey, SurveyResponse
from .serializers import SurveySerializer, SurveyResponseSerializer


class SurveyView(APIView):
    def get(self, request):
        surveys = Survey.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return Response({"surveys": serializer.data})

    def post(self, request):
        survey = request.data.get('survey')

        serializer = SurveySerializer(data=survey)
        if serializer.is_valid(raise_exception=True):
            survey_saved = serializer.save()
        return Response({"success": "Survey '{}' created successfully".format(survey_saved.name)})


class SurveyResponseView(APIView):
    def get(self, request):
        survey_responses = SurveyResponse.objects.all()
        serializer = SurveyResponseSerializer(survey_responses, many=True)
        return Response({"survey_responses": serializer.data})

    def post(self, request):
        survey_response = request.data.get('survey_response')

        serializer = SurveyResponseSerializer(data=survey_response)
        if serializer.is_valid(raise_exception=True):
            survey_response_saved = serializer.save()
        return Response({"success": "Survey response '{}' created successfully".format(survey_response_saved.id)})