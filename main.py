from config import settings
from bs4 import BeautifulSoup

import requests
import logging
import functools as fn
import pickle

logger = logging.getLogger()
logger.setLevel(logging.INFO)



def get_metastore():
    with open(settings.file_instance_dump,'rb') as fl:
        return pickle.load(fl, encoding='bytes')

def set_metastore():
    yarn_data_url = "https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop-task-config.html"
    cores_data_url = "https://aws.amazon.com/pt/ec2/instance-types/"

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
    instances = {}
    for i in raw_instances:
        if 'yarn.cores' in raw_instances[i]:
            instances[i] = raw_instances[i]

    with open(settings.file_instance_dump, 'wb') as fl:
        pickle.dump(instances, fl)
    
if __name__ == "__main__":
    set_metastore()
    print(get_metastore())