"""Install fuzzywuzzy for search in a bot work."""

from fuzzywuzzy import fuzz, process

# diff two strings and get result in percents
fuzz.ratio("Let's do a simple test", "Let us do a simple test")

### diff words not see in a case or one by one

fuzz.token_sort_ratio('Hello our world', 'world our lovely Hello')

### targeting great same word, limit - how many return

choices = ["Data Visualisation", "Data Visualization",
           "Customised Behaviours", "Customized  Behaviors"]
process.extract("data.visualisation", choices, limit=2)

######
