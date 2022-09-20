"""Time about."""

#1 time get clock info

import textwrap
import time

available_clocks = [
        ('clock', time.clock),
        ('monotonic', time.monotonick),
        ('perf_counter', time.perf_counter),
        ('process_time', time.process_time),
        ('time', time.time),
]

for clock_name, func in available_clocks:
    print(textwrap.dedent('''\
            {name}:
            adjustable    : {info.ajustable}
            imlementation : {info.implementation}
            monotonic     : {info.monotonic}
            resolution    : {info.resolution}
            current       : {current}
            ''').format(
                name=clock_name,
                info=time.get_clock_info(clock_name),
                current=func())\
            )
