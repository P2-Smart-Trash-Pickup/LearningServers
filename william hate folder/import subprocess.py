import subprocess
import time
import statistics
import os

def pingb(hostname,iterations=31):
    latency = []
    lost_latency = 0
    hejmartin = 0
    print(f"pinging {hostname} {iterations} times\n")

    for _ in range(iterations):
        result = subprocess.run(['ping',hostname],capture_output=True,text=True)
        output = result.stdout

        if "time=" in output:
            rttms = output.split("time=")[1].split("ms")[0]
            hejmartin = hejmartin + int(rttms)
            print(f"rtt = {rttms}ms")
    print(f"average time {hejmartin/iterations}ms")
pingb("pornhub.com",10)