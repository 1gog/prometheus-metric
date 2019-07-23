#!/usr/bin/env python 



import os

def getValue():
        cpu_mem_metric = os.popen('ps -heo %cpu,%mem -p 1').read()

        raw = cpu_mem_metric.rstrip().split(' ')

        (cpu,mem) = list(filter(lambda x: x != '', raw))
        print("cpu = %s" % cpu )
        print("mem = %s" % mem )
        return ( cpu, mem )


(cpu, mem ) = getValue()
