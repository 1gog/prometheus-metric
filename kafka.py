#!/usr/bin/env python


from prometheus_client import start_http_server, Summary, Counter, Gauge
import random
from time import time, sleep
import os,sys

ServicePort=8181


def preup():
    if len(sys.argv) <= 1:
        print "Need one arg service name"
        print "use cmd "
        print "default port number 8181"
        print "        python %s <kafka> <port>" % __file__
        sys.exit()


def startServer():
    try:
	if len(sys.argv) == 3:
	    port = sys.argv[2]
	else:
	    port = 8181
	start_http_server(int(port))
    except Exception as e:
	print("ERROR: %s" % e)
	sys.exit()

def getPid():
	cmd = "systemctl show -p MainPID %s.service | awk -F= '{print $2}'" % sys.argv[1]
	pid = (os.popen(cmd).read()).rstrip()
	if int(pid) == 0:
	    print("pid of system process not found of process is clouse")
	    sys.exit()
	else:
	    return int(pid)

def getValue(pid):
	cmd = 'ps -heo %%cpu,%%mem -q %d' % pid
        cpu_mem_metric = os.popen(cmd).read()

        raw = cpu_mem_metric.rstrip().split(' ')

        (cpu,mem) = list(filter(lambda x: x != '', raw))
        return ( cpu, mem )


kafka_cpu = Gauge('cpu_kafka', 'The gauge cpu usage')
kafka_mem = Gauge('mem_kafka', 'The gauge memory usage')


if __name__ == "__main__":
    preup()
    startServer()
    while True:
    	(cpu,mem) = getValue(getPid())
    	kafka_cpu.set( cpu )
    	kafka_mem.set( mem )
    	sleep(1)
