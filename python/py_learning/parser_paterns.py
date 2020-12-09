import re

matchobj = re.match('Hello(.*)World', text2)
print(matchobj)

pattobj = re.compile('Hello(.*)World')
matchobj = pattobj.match(text1)
matchobj.group(1)

patt = '[ \t]*Hello[\t]+(.*)[Ww]orld'
line = ' Hello spamworld'
mobj = re.match(patt, line)
mobj.group(1)

patt = b'[ \t]*Hello[ \t]+(.*)[Ww]orld'
line = b' Hello spawnworld'
re.match(patt, line).group(1)

re.match(patt, ' Hello spawnworld')

re.match('[ \t]*Hello[ \t]+ (.*)[Ww]orld', line)

#--------
re.split('--', 'aaa--bbb--ccc')
re.sub('--', '...', 'aaa--bbb--ccc')

re.split('--|==', 'aaa--bbb==ccc')

re.split('[-=]', 'aaa-bbb=ccc')

re.split('(--)|(==)', 'aaa--bbb==ccc')

re.split('(?:--)|(?:==)', 'aaa--bbb==ccc')

#-------
re.match('(.*)/(.*)/(.*)', 'spam/ham/eggs').groups()

re.match('<(.*)>/<(.*)>/(.*)>', '<spam>/<ham>/<eggs>').groups()

re.match('/s*<(.*)>/?<(.*)>/?<(.*)>', ' <spam>/<ham><eggs>').groups()

re.match('Hello\s*([a-z]*)\s+(.*?)\s*!', 'Hellopattern world !').groups()

re.findall('<(.*?)>', '<spam>/<ham>/<eggs>')

re.findall('<(.*?)>', '<spam> / <ham><eggs>')

re.findall('<(.*?)>/?<(.*?)>',
        'todays menu: <spam>/<ham>...<eggs><s>').groups()

re.findall('<(.*?)>.*<(.*?)>', '<spam> \n <ham>\n<eggs>')

re.findall('(?s)<(.*?)>.*<(.*?)>', '<spam> \n <ham>\n<eggs>')

re.findall('(?s)<(.*?)>.*?<(.*?)>', '<spam> \n <ham>\n<eggs>')

re.search('(?P<part1>\w*)/(?P<part2>\w*)', '...aaa/bbb/ccc]').groups()

re.search('(?P<part1>\w*)/(?P<part2>\w*)', '...aaa/bbb/ccc]').groupdict()

re.search('(?P<part1>\w*)/(?P<part2>\w*)', '...aaa/bbb/ccc]').groups(2)

re.search('(?P<part1>\w*)/(?P<part2>\w*)',
        '...aaa/bbb/ccc]').group('part2')

re.findall('(?P<part1>\w*)/(?P<part2>\w*)', '...aaa/bbb/ccc/ddd]')


