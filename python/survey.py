"""File for tests_ex.py, testing classes."""

class AnonymousSurvey():
    """Assemble anonimous ansvers to questions."""

    def __init__(self, question):
        """Save question and ready to save ansswers."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Return question."""
        print(self.question)

    def store_response(self, new_response):
        """Save one answer to question."""
        self.responses.append(new_response)

    def show_results(self):
        """Return answers."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
