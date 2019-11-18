#!/usr/bin/python
#-*-coding:utf-8-*-
import subprocess
def ck(subj):
    value = subprocess.Popen('cat %s'% subj, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return value.stdout.read().strip()
def vck(subj):
    value = subprocess.Popen(subj, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return value.stdout.read().strip()
subj = {
        'ipforward':'/proc/sys/net/ipv4/ip_forward',
        'syncookies':'/proc/sys/net/ipv4/tcp_syncookies',
        'syn_recv_no':'/proc/sys/net/ipv4/tcp_max_syn_backlog',
        'socketlistenbacklog':'/proc/sys/net/core/somaxconn',
        'swap':'/proc/sys/vm/swappiness'
        }

cmdsubj = {

}

print(subj['syn_recv_no'])