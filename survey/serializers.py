from rest_framework import serializers

from .models import Survey, SurveyResponse, User


class SurveySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    available_places = serializers.IntegerField()
    user_id = serializers.CharField(source='user.id')

    def create(self, validated_data):
        #Solely for the purposes of the sample test where users may not be set up in advance
        try:
            user = User.objects.get(id=validated_data["user"]["id"])
        except User.DoesNotExist:
            user = User.objects.create(id=validated_data["user"]["id"])   

        validated_data['user_id'] = int(validated_data["user"]["id"])
        validated_data.pop("user", None)
        return Survey.objects.create(**validated_data)


class SurveyResponseSerializer(serializers.Serializer):
    user_id = serializers.CharField(source='user.id')
    survey_id = serializers.CharField(source='survey.id')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    def create(self, validated_data):
        try:
            survey = Survey.objects.get(id=validated_data["survey"]["id"])
            if survey.remaining_places <= 0:
                raise serializers.ValidationError('Sorry this survey has no more availability')
            else:
                validated_data['user_id'] = int(validated_data["user"]["id"])
                validated_data.pop("user", None)
                validated_data['survey_id'] = int(validated_data["survey"]["id"])
                validated_data.pop("survey", None)
                return SurveyResponse.objects.create(**validated_data)
        except Survey.DoesNotExist:
            raise serializers.ValidationError('This is not a valid survey, please try again')

            