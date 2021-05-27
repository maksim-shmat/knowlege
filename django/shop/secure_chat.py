"""netcat not safe."""

apt install socat
$ socat TCP4-LISTEN:1234 STDOUT

### in termux
socat STDIN TCP4:1234:127.0.0.1:1234
