"""io about."""

#1 io.StringIO()

import io

# write to buffer
output = io.StringIO()
output.write('This goes into the buffer.')
print('And so does this.', file=output)

# Output that written
print(output.getvalue())
output.close()  # emptyed memory buffer

# Init of write buffer
input = io.StringIO('inital value for read buffer')

# Read from buffer
print(input.read())

'''RESULTS:
This goes into the buffer.And so does this.

inital value for read buffer
'''

#2 for raw data use io.BytesIO()

import io

# Write to buffer
output = io.BytesIO()
output.write('This goes into the buffer. '.encode('utf-8'))
output.write('ÁÇÈ'.encode('utf-8'))

# get written value
print(output.getvalue())
output.close()  # empty memory buffer

# Init buffer for write
input = io.BytesIO(b'Initial value for read buffer')

# Read from buffer
print(input.read())

'''RESULTS:
b'This goes into the buffer. \xc3\x81\xc3\x87\xc3\x88'
b'Initial value for read buffer'
'''

#3 io.TextIOWrapper()

import io

# write on the buffer
output = io.BytesIO()
wrapper = io.TextIOWrapper(
        output,
        encoding= 'utf-8',
        write_through=True,
)
wrapper.write('This goes into the buffer.')
wrapper.write('ÁÇĒ')

# get from the buffer
print(output.getvalue())

output.close()  # empty buffer memory

# Init buffer for write
input = io.BytesIO(
        b'Initial value for read buffer with unicode characters' +
        'ÁÇĒ'.encode('utf-8')
)
wrapper = io.TextIOWrapper(input, encoding='utf-8')

# Read from the buffer
print(wrapper.read())

'''RESULTS:
b'This goes into the buffer.\xc3\x81\xc3\x87\xc4\x92'
Initial value for read buffer with unicode charactersÁÇĒ
'''
