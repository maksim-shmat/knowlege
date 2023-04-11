""" .env for django about."""

#1 (virtual env) PS > echo 'DATABASE_URL=sqlite:///db.sqlite3' > .env
#??? for windows?

#2 settings.py

...
import dotenv

BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
)
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
SECRET_KEY = os.getenv('SECRET_KEY')

#3 .env

...
SECRET_KEY = my_randomly_generated_key
