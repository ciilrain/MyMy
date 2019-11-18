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
        'maxsocketlisten':'/proc/sys/net/core/somaxconn',
        'swap':'/proc/sys/vm/swappiness'
        }

cmdsubj = {

}

syn_recv_no = int(ck(subj['syn_recv_no']))
maxconn = int(ck(subj['maxsocketlisten']))
swap = int(ck(subj['swap']))
syncookies = int(ck(subj['syncookies']))
ipforward = int(ck(subj['ipforward']))


if maxconn<1000:
    print('Limit socket listen too low!')
else:
    print('Limit socket listen configured OK!')

if syn_recv_no<1000:
    print('SYN_RECV queue too low!')
else:
    print('SYN_RECV queue configured OK!')

if swap>10:
    print('swappiness rate too high!')
else:
    print('swappiness rate is OK!')

if syncookies>0:
    print('DO NOT use syncookies on highly loaded servers!')
else:
    print('syncookies closed')

if ipforward>0:
    print('')
else:
    print('')