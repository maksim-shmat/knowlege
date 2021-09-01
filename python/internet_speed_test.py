"""Speed test of internet."""

# pip3 install speedtest-cli

import speedtest

st = speedtest.Speedtest()

download_speed = st.download()
print(download speed / (2 ** 20))
print()

upload_speed = st.upload()
print(upload_speed / (2 ** 20))
