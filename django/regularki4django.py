"""Regular expression for django url patterns."""

url(r'^$',...)  Empty string(Home page)  Matches: http://127.0.0.1/


url(r'^stores/',...)  Any trailing characters  Matches: http://127.0.0.1/stores/  http://127.0.0.1/stores/long+string+anything+12345


url(r'^about/contact/$',...)  Exact, no trailing characters  Matches: http://127.0.0.1/about/contact  Doesn`t match: http://127.0.0.1/about


url(r'^stores/\d+/'...)  Numbers  Matches: http://127.0.0.1/stores/2/  http://127.0.0.1/stores/34/  Doesn`t match: http://127.0.0.1/drinks/324/


url(r'^drinks/\D+/',...) Non-digits  Matches: http://127.0.0.1/drinks/mocha/  Doesn`t match: http://127.0.0.1/drinks/324/


url(r'^drinks/mocha|espresso/',...)  Word options, any trailing characters  Matches: http://127.0.0.1/drinks/mocha/  http://127.0.0.1/drinks/mochaccino/  http://127.0.0.1/drinks/espresso/  Doesn`t match: http://127.0.0.1/drinks/soda/


url(r'^drinks/mosha$|espresso/$',...)  Word options exact, no trailing characters  Matches: http://127.0.0.1/drinks/mocha/  Doesn`t match: http://127.0.0.1/drinks/mochaccino/  Matches: http://127.0.0.1/drinks/espresso/  Doesn`t match: http://127.0.0.1/drinks/espressomacchiato/


url(r'^stores/\w+/',...)  Word characters (Any letter lower or uppercase,
number, or underscore)  Matches: http://127.0.0.1/stores/sandiego/  http://127.0.0.1/stores/LA/  http://127.0.0.1/stores/1/  Doesn`t match: http://127.0.0.1/san-diego/


url(r'^stores/[\w]+/',...)  Word characters or dash  Matches: http://127.0.0.1/san-diego/


url(r'^state/[A-Z]{2}/',...)  Two uppercase letters  Matches: http://127.0.0.1/CA/  Doesn`t match: http://127.0.0.1/Ca/


