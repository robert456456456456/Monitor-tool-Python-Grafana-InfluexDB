#!/usr/bin/python
import linux_metrics as lm
import os

def apend_file(file_path,string):
    with open(file_path, 'a') as file:
        file.write(string+"\n")



def costructor_api_inlflux_insert_data(db_name,app_name,value,land,file):
        #print land.split('\n')[0]
        #print value   
        cmd = '''curl -i -XPOST 'http://localhost:8086/write?db=statsdemo' --data-binary "%s,app=%s,land=%s value=%s"''' % (db_name, app_name, land.split('\n')[0], value)
        #print cmd
        apend_file(file, cmd)


def constructor_api_get_data(data,db_name,landscape):
    file_ = landscape.split('\n')[0]+ '_data.sh'
    if file_:
        try:
            os.remove(file_)
        except:
            print 'file not exist'


    for i in data:
            app_name = i[0]
            value = i[1]
            #print landscape
            costructor_api_inlflux_insert_data(db_name, app_name, str(value), landscape, file_)

def server_name():
    file = open("/etc/hostname", "r")
    landscape= file.read()
    return landscape



def main():
    data=[]
    # cpu
    #print 'procs running: %d' % lm.cpu_stat.procs_running()
    cpu_pcts = lm.cpu_stat.cpu_percents(sample_duration=1)
    c= str('cpu utilization: %.2f%%' % (100 - cpu_pcts['idle'])).split(':')[1].split('%')[0].split(' ')[1]
    #print c
    data.append(['proc',str(lm.cpu_stat.procs_running())])
    data.append(['cpu',c])
    # disk
    b= str('disk busy: %s%%' % lm.disk_stat.disk_busy('xvda', sample_duration=1)).split(':')[1].split('%')[0].split(' ')[1]
    data.append(['disk_busy',str(b)])
    r, w = lm.disk_stat.disk_reads_writes('xvda1')
    usah= lm.disk_usage('/dev/xvda1')
    #print 'disk usage: %s' % usah[4]
    data.append(['disk_usage',str(usah[4].split('%')[0])])
    #print 'disk reads: %s' % r
    data.append(['disk_reads',str(r)])
    #print 'disk writes: %s' % w
    data.append(['disk_writes',str(w)])

    # memory
    used, total, _, _, _, _ = lm.mem_stat.mem_stats()
    #print 'mem used: %s' % used
    data.append(['mem_used',str(used)])
    #print 'mem total: %s' % total
    data.append(['mem_total',str(total)])
    # network
    rx_bits, tx_bits = lm.net_stat.rx_tx_bits('eth0')
    #print 'net bits received: %s' % rx_bits
    data.append(['net_bits_received',str(rx_bits)])
    #print 'net bits sent: %s' % tx_bits
    data.append(['net_bits_sent',str(tx_bits)])
    constructor_api_get_data(data,'all_metrics',str(server_name()))



if __name__ == '__main__':
    main()
    file_=str(server_name()).split('\n')[0]+ '_data.sh'
    os.system(file_)


