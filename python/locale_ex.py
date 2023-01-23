"""locale about."""

# locale env
# for: $ export LANG=; export LC_CTYPE=; python3 locale_ex.py
# for: $ LANG=en_US LC_CTYPE=en_US LC_ALL=en_US python3 locale_ex.py
# for: $ Lang=be_BE LC_CTYPE=be_BE LC_ALL=be_BE python3 locale_ex.py #?

import locale
import os
import pprint

'''
# Default values how will be created in users environment
locale.setlocale(locale.LC_ALL, '')

print('Environment settings:')
for env_name in ['LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE']:
    print('  {} = {}'.format(
        env_name, os.environ.get(env_name, ''))
    )

print('\nLocale from environment:', locale.getlocale())

template = """
Numeric formatting:

    Decimal point        : "{decimal_point}"
    Grouping positions   : {grouping}
    Thousands separator  : "{thousands_sep}"

Monetary formatting:

    International currency symbol    : "{int_curr_symbol!r}"
    Local currency symbol            : {currency_symbol!r}
    Symbol precedes positive value   : {p_cs_precedes}
    Symbol precedes negative value   : {n_cs_precedes}
    Decimal point                    : "{mon_decimal_point}"
    Digits in fractional values      : {frac_digits}
    Digits in fractional values,
                     international   : {int_frac_digits}
    Grouping positions               : {mon_grouping}
    Thousands separator              : "{mon_thousands_sep}"
    Positive sign                    : "{positive_sign}"
    Positive sign position           : {p_sign_posn}
    Negative sign                    : "{negative_sign}"
    Negative sign position           : {n_sign_posn}

"""

sign_positions = {
        0: 'Surrounded by parentheses',
        1: 'Before value and symbol',
        2: 'After value and symbol',
        3: 'Before value',
        4: 'After value',
        locale.CHAR_MAX: 'Unspecified',
}

info = {}
info.update(locale.localeconv())
info['p_sign_posn'] = sign_positions[info['p_sign_posn']]
info['n_sign_posn'] = sign_positions[info['n_sign_posn']]

print(template.format(**info))

RESULTS:
Environment settings:
  LC_ALL = 
  LC_CTYPE = 
  LANG = en_GB.UTF-8
  LANGUAGE = en_GB:en

Locale from environment: ('en_GB', 'UTF-8')

Numeric formatting:

    Decimal point        : "."
    Grouping positions   : [3, 3, 0]
    Thousands separator  : ","

Monetary formatting:

    International currency symbol    : "'GBP '"
    Local currency symbol            : '£'
    Symbol precedes positive value   : 1
    Symbol precedes negative value   : 1
    Decimal point                    : "."
    Digits in fractional values      : 2
    Digits in fractional values,
                     international   : 2
    Grouping positions               : [3, 3, 0]
    Thousands separator              : ","
    Positive sign                    : ""
    Positive sign position           : Before value and symbol
    Negative sign                    : "-"
    Negative sign position           : Before value and symbol
'''

#2 locale currency
