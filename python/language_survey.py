"""File for survey.py which for tests_ex.py. Testing classes."""

from survey import AnonymousSurvey

# make a question 
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show question and save it
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Return results.
print('\nThank you to everyone who paricipated in the survey!')
my_survey.show_results()
