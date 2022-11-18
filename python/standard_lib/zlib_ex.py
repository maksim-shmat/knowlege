"""zlib about."""

#1 zlib memory

import zlib
import binascii

original_data = b'This is the original text.'
print('Original    :', len(original_data), original_data)

compressed = zlib.compress(original_data)
print('Compressed  :', len(compressed),
        binascii.hexlify(compressed))

decompressed = zlib.decompress(compressed)
print('Decompressed:', len(decompressed), decompressed)

'''RESULTS:
Original    : 26 b'This is the original text.'
Compressed  : 32 b'789c0bc9c82c5600a2928c5485fca2ccf4ccbcc41c8592d48a123d007f2f097e'
Decompressed: 26 b'This is the original text.'
'''

#2 zlib lengths for example

import zlib

original_data1 = b'This is the original text.'

template = '{:>15} {:>15}'
print(template.format('len(data)', 'len(compressed)'))
print(template.format('-' * 15, '-' * 15))

for i in range(5):
    data = original_data * i
    compressed = zlib.compress(data)
    highlight = '*' if len(data) < len(compressed) else ''
    print(template.format(len(data), len(compressed)), highlight)

'''RERULTS:
      len(data) len(compressed)
--------------- ---------------
              0               8 *
             26              32 *
             52              35 
             78              35 
            104              36 
'''

#3 zlib compresslevel

import zlib

input_data = b'Some repeated text.\n' * 1024
template = '{:>5} {:>5}'

print(template.format('Level', 'Size'))
print(template.format('-----', '----'))

for i in range(0, 10):
    data = zlib.compress(input_data, i)
    print(template.format(i, len(data)))

'''RESULTS:
Level  Size
-----  ----
    0 20491
    1   172
    2   172
    3   172
    4    98
    5    98
    6    98
    7    98
    8    98
    9    98
'''

#4 zlib incremental, if momory low put data to compress()

import zlib
import binascii

compressor = zlib.compressobj(1)

with open('lorem.txt', 'rb') as input:
    while True:
        block = input.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print('Compressed: {}'.format(
                binascii.hexlify(compressed)))
        else:
            print('buffering...')
    remaining = compressor.flush()
    print('Flushed: {}'.format(binascii.hexlify(remaining)))

#5 zlib mixed compressed data with free data for decompressobj()

import zlib

lorem = open('lorem.txt', 'rb').read()
compressed = zlib.compress(lorem)
combined = compressed + lorem

decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combined)

decompressed_matches = decompressed == lorem
print('Decompressed matches lorem:', decompressed_matches)

unused_matches = decompressor.unused_data == lorem
print('Unused data matches lorem :', unused_matches)

'''RESULTS:
Decompressed matches lorem: True
Unused data matches lorem : True
'''

#6 zlib check sum, not safe criptographic, just count control sum only.

import zlib

data = open('lorem.txt', 'rb').read()

cksum = zlib.adler32(data)
print('Adler32: {:12d}'.format(cksum))
print('       : {:12d}'.format(zlib.adler32(data, cksum)))

cksum = zlib.crc32(data)
print('CRC-32 : {:12d}'.format(cksum))
print('       : {:12d}'.format(zlib.crc32(data, cksum)))

'''RESULTS:
Adler32:   2778140539
       :   4211023605
CRC-32 :    229580248
       :   3621037226
'''

#7 zlib server, !not safe for andrusha

import zlib
import logging
import socketserver
import binascii

BLOCK_SIZE = 64


class ZlibRequestHandler(socketserver.BaseRequestHandler):

    logger = logging.getLogger('Server')

    def handle(self):
        compressor = zlib.compressobj(1)

        # Check file
        filename = self.request.recv(1024).decode('utf-8')
        self.logger.debug('client asked for: %r', filename)

        # zip chunk and send
        with open(filename, 'rb') as input:
            while True:
                block = input.read(BLOCK_SIZE)
                if not block:
                    break
                self.logger.debug('RAW %r', block)
                compressed = compressor.compress(block)
                if compressed:
                    self.logger.debug(
                            'SENDING %R',
                            binascii.hexlify(compressed))
                    self.request.send(compressed)
                else:
                    self.logger.debug('BUFFERING')

        # send compressed data
        remaining = compressor.flush()
        while remaining:
            to_send = remaining[:BLOCK_SIZE]
            remaining = remaining[BLOCK_SIZE:]
            self.logger.debug('FLUSHING %r',
                              binascii.hexlify(to_send))
            self.request.send(to_send)
        return

if __name__ == '__main__':
    import socket
    import threading
    from io import BytesIO

    logging.basicConfig(
            level=logging.DEBUG,
            format='%(name)s: %(message)s',
    )
    logger = logging.getLogger('Client')

    # Set server for different thread
    address = ('localhost', 0)  # core check port
    server = socketserver.TCPServer(address, ZlibRequestHandler)
    ip, port = server.server_address  # What port is it?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    # Connect to server as client
    logger.info('Contacting server on %s:%s', ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Ask file
    requested_file = 'lorem.txt'
    logger.debug('sending filename: %r', requested_file)
    len_sent = s.send(requested_file.encode('utf-8'))

    # Get answer
    buffer = BytesIO()
    decompressor = zlib.decompressobj()
    while True:
        response = s.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('READ %r', binascii.hexlify(response))

        # Include not used data to send line
        to_decompress = decompressor.unconsumed_tail + response
        while to_decompress:
            decompressed = decompressor.decompress(to_decompress)
            if decompressed:
                logger.debug('DECOPRESSED %r', decompressed)
                buffer.write(decompressed)
                # Find data how not use cause buffer full
                to_decompress = decompressor.unconsumed_tail
            else:
                logger.debug('BUFFERING')
                to_decompress = None
        

        # Handling data from decompressor's buffer
        remainder = decompressor.flush()
        if remainder:
            logger.debug('FLUSHED %r', remainder)
            buffer.write(remainder)

        full_response = buffer.getvalue()
        lorem = open('lorem.txt', 'rb').read()
        logger.debug('response matches file contents: %s',
                     full_response == lorem)

        # Free resources
        s.close()
        server.socket.close()
