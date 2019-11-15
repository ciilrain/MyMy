#!/usr/bin/python
#-*-coding:utf-8-*-
import subprocess
def ck(subj):
    value = subprocess.Popen('cat %s'% subj, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return value.stdout.read().strip()
def vck(subj):
    value = subprocess.Popen(subj, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return value.stdout.read().strip()

proc = '/proc/sys/'
subj = '/proc/sys/net/ipv4/ip_forward'
subj2 = 'vm/swapness'

str1 = proc+subj2
print(str1)
