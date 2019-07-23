#!/usr/bin/env python


from prometheus_client import start_http_server, Summary, Counter, Gauge
import random
from time import time, sleep
import os


if len(sys.argv) < 1:
        print "need one arg pid process "
        print "use cmd python %s <pid>" % __file__
        sys.exit()


def getValue(pid):
	cmd = 'ps -heo %%cpu,%%mem -q %d' % pid
        cpu_mem_metric = os.popen(cmd).read()

        raw = cpu_mem_metric.rstrip().split(' ')

        (cpu,mem) = list(filter(lambda x: x != '', raw))
        return ( cpu, mem )


kafka_cpu = Gauge('cpu_kafka', 'The gauge cpu usage')
kafka_mem = Gauge('mem_kafka', 'The gauge memory usage')


if __name__ == "__main__":
    start_http_server(8181)
    while True:
    	(cpu,mem) = getValue(sys.argv[1])
    	kafka_cpu.set( cpu )
    	kafka_mem.set( mem )
    	sleep(1)
