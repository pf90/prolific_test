<h2>Overview</h2>

The Surveys API stores data about surveys and responses to surveys.
Users can create and list surveys using the API. Each survey has a name and a number of available places.
Users can also create responses to surveys. Each survey response is recorded with a timestamp.
Each survey response counts towards the available places for a survey. Survey responses should only be created if there are still available places on the survey. For example if I try to create a 31st response to a survey with 30 places, I should receive an error.

<h4>Specification</h4>
A study record should have the following fields:
<li> ID </li>
<li> survey name </li>
<li> available places </li> 
<li> user_id </li>
A study response record should have the following fields:
<li> ID </li>
<li> user_id </li>
<li> created_at </li> 
<li> survey_id </li>
The API should include the following endpoints:
<li> List all surveys </li>
<li> Create a new survey </li>
<li> Create a new survey response </li>
<h5> Additional requirements: </h5>
Users should not be able to submit a survey response if there are no more available places on a study

<h2>Installing</h2>

    virtualenv prolific_test
    source prolific-test/bin/activate
    git clone https://github.com:pf90/prolific_test.git
    cd prolific_test/
    python manage.py migrate
    python manage.py runserver
    
