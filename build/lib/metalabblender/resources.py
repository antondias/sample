import os
import psutil;
import tensorflow as tf
from tensorflow.python.client import device_lib

def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
  		return str(bytes) + units[0] if bytes < 1024 else human_size(bytes>>10, units[1:])

def print_resources():
    mem = psutil.virtual_memory().total
    free_mem = psutil.virtual_memory().available
    hdd = psutil.disk_usage('/content/')

    print(f"CPU Count: {os.cpu_count()}")
    print(f"Memory: {human_size(mem)}")
    print(f"Free Memory: {human_size(free_mem)}")
    print(f"HD Total: {human_size(hdd.total)}")
    print(f"HD Used: {human_size(hdd.used)}")
    print(f"HD Free: {human_size(hdd.free)}")

    devices = device_lib.list_local_devices()
    for d in devices:
        t = d.device_type
        name = d.physical_device_desc
        l = [item.split(':',1) for item in name.split(", ")]
        name_attr = dict([x for x in l if len(x)==2])
        dev = name_attr.get('name', 'Unnamed device')
        print(f" {d.name} || {dev} || {t} || {human_size(d.memory_limit)}")       