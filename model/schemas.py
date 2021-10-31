from typing import List, Optional
from pydantic import BaseModel


class Instance(BaseModel):
	instance_name : str
	mapreduce_map_java_opts : str
	mapreduce_reduce_java_opts : str
	mapreduce_map_memory_mb : str
	mapreduce_reduce_memory_mb : str
	yarn_app_mapreduce_am_resource_mb : str 
	yarn_scheduler_minimum_allocation_mb : str
	yarn_scheduler_maximum_allocation_mb : str
	yarn_nodemanager_resource_memory_mb : str
	yarn_cores  : str

	class Config:
		orm_mode = True
		

class Cluster(BaseModel):
	cluster_profile : str
	bootstrap_path : str
	slave_core_count_ondemand : int	
	slave_task_count_ondemand : int
	slave_task_count_spot : int
	master_instance_id : str
	slave_instance_id : str
	subnet_id : str
	applications : str
	spark_cores_per_executor : int
	glue_spark_metastore : bool
	glue_hive_metastore : bool
	glue_presto_metastore : bool
	release_label : str
	tags : str

	class Config:
		orm_mode = True