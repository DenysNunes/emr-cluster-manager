from config import settings
from bs4 import BeautifulSoup

import requests
import logging
import functools as fn
import pickle

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_metastore() -> list[dict]:
    yarn_data_url = "http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop-task-config.html"
    cores_data_url = "http://aws.amazon.com/pt/ec2/instance-types/"

    # Crawling YARN Instance Data
    logger.info("Crawling YARN data from AWS source ({})".format(yarn_data_url))

    page = requests.get(yarn_data_url, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')

    divs = soup.find_all('div', class_='table-container')
    tables = [t.find_all('table')[0] for t in divs]
    raw_instances = {}

    for table in tables:
        instance = table.find_all(class_="table-header")[0].text.strip()
        instance_data = {}

        if len(table.find_all('th')) == 4:
            for row in range(0, len(table.find_all('td')), 3):
                instance_data[table.find_all('td')[row].text] = table.find_all('td')[row + 1].text
        else:
            for row in range(0, len(table.find_all('td')), 2):
                instance_data[table.find_all('td')[row].text] = table.find_all('td')[row + 1].text
        
        raw_instances[instance] = instance_data

    # Crawling CORE Data

    logger.info("Crawling CPU CORES data from AWS source ({})".format(cores_data_url))

    c_page = requests.get(cores_data_url, verify=False)
    c_soup = BeautifulSoup(c_page.text, 'html.parser')
    c_divs = c_soup.find_all('div', class_='lb-content-wrapper')
    c_list_tables = [t.find_all('table') for t in c_divs]

    for c_tables in c_list_tables:
        for c_table in c_tables:
            c_rows = c_table.find_all('tr')
            for row in c_rows:
                splited_line = row.text.split("\n")
                inst_type = splited_line[1]
                inst_vcpu = splited_line[2]

                if inst_type in raw_instances:
                    raw_instances[inst_type]['yarn.cores'] = int(inst_vcpu)

    # Removing Old Instances
    instances = []
    for i in raw_instances:
        if 'yarn.cores' in raw_instances[i]:
            inst : dict = {}
            inst['instance_name'] = i 
            inst['mapreduce_map_java_opts'] = raw_instances[i]['mapreduce.map.java.opts']
            inst['mapreduce_reduce_java_opts'] = raw_instances[i]['mapreduce.reduce.java.opts']
            inst['mapreduce_map_memory_mb'] = raw_instances[i]['mapreduce.map.memory.mb']
            inst['mapreduce_reduce_memory_mb'] = raw_instances[i]['mapreduce.reduce.memory.mb']
            inst['yarn_app_mapreduce_am_resource_mb'] = raw_instances[i]['yarn.app.mapreduce.am.resource.mb']
            inst['yarn_scheduler_minimum_allocation_mb'] = raw_instances[i]['yarn.scheduler.minimum-allocation-mb']
            inst['yarn_scheduler_maximum_allocation_mb'] = raw_instances[i]['yarn.scheduler.maximum-allocation-mb']
            inst['yarn_nodemanager_resource_memory_mb'] = raw_instances[i]['yarn.nodemanager.resource.memory-mb']
            inst['yarn_cores'] = raw_instances[i]['yarn.cores']
            instances.append(inst)           

  
    return instances
