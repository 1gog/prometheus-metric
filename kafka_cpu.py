#!/usr/bin/env python


from prometheus_client import start_http_server, Summary, Counter, Gauge
# import time
import random
from time import time, sleep

import subprocess
subprocess.run(["ls", "-l"])


# example for Summary
#REQUEST_TIME = Summary('cpu_kafka', 'Time spent processing request')


# example for Counter
#c = Counter('kafka_cpu', 'Kafka Cpu usage')
# example for Gauges

g = Gauge('g_cpu_kafka','The gauge cpu usage')


#@REQUEST_TIME.time()
#def process_request(t):
#    """A dummy function that takes some time."""
#    time.sleep(t)

#def cpu_count():
#    return c.inc(random.random())

@g.track_inprogress()
def gauge_kafka_cpu():
    #g1 = Gauge('g_cpu_kafka','The gauge cpu usage')
    g.set(random.randrange(1,100,1))

start_http_server(8181)
while True:
    #g1 = Gauge('g_cpu_kafka','The gauge cpu usage')
    #g1.set(random.randrange(1,100,1))
    gauge_kafka_cpu()
    sleep(1)



#if __name__ == "__main__":
#    start_http_server(8181)
#    while True:
#       #process_request(1)
#       gauge_kafka_cpu()
