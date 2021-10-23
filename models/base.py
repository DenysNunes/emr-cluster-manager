from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Instance(Base):
	__tablename__ = 'instances'
	instance_name = Column(String(50), primary_key=True)
	mapreduce_map_java_opts = Column(String(50))
	mapreduce_reduce_java_opts = Column(String(50))
	mapreduce_map_memory_mb = Column(String(50))
	mapreduce_reduce_memory_mb = Column(String(50))
	yarn_app_mapreduce_am_resource_mb = Column(String(50))
	yarn_scheduler_minimum_allocation_mb = Column(String(50))
	yarn_scheduler_maximum_allocation_mb = Column(String(50))
	yarn_nodemanager_resource_memory_mb = Column(String(50))
	yarn_cores  = Column(String(50))

	def json(self):
		return {
			"instance_name": self.instance_name, 
			"mapreduce_map_java_opts": self.mapreduce_map_java_opts,
			"mapreduce_reduce_java_opts": self.mapreduce_reduce_java_opts,
			"mapreduce_map_memory_mb": self.mapreduce_map_memory_mb,
			"mapreduce_reduce_memory_mb": self.mapreduce_reduce_memory_mb,
			"yarn_app_mapreduce_am_resource_mb": self.yarn_app_mapreduce_am_resource_mb,
			"yarn_scheduler_minimum_allocation_mb": self.yarn_scheduler_minimum_allocation_mb,
			"yarn_scheduler_maximum_allocation_mb": self.yarn_scheduler_maximum_allocation_mb,
			"yarn_nodemanager_resource_memory_mb": self.yarn_nodemanager_resource_memory_mb,
			"yarn_cores": self.yarn_cores
		}

	def __repr__(self):
		return  "Instance " + self.instance_name
	

class Cluster(Base):
	__tablename__ = 'clusters'
	cluster_profile = Column(String(50), primary_key=True)
	bootstrap_path = Column(String(150))
	slave_core_count_ondemand = Column(Integer)
	slave_task_count_instance = Column(Integer)
	slave_task_count_ondemand = Column(Integer)
	master_instance_id = Column(String(50), ForeignKey('instances.instance_name'))
	slave_instance_id = Column(String(50), ForeignKey('instances.instance_name'))
	subnet_id = Column(String(50))
	applications = Column(String(150))
	spark_cores_per_executor = Column(Integer)
	release_label = Column(String(10))
	tags = Column(String(150))	

	def json(self):
		return {
			"cluster_profile": self.cluster_profile,
			"bootstrap_path": self.bootstrap_path,
			"slave_core_count_ondemand": self.slave_core_count_ondemand,
			"slave_task_count_instance": self.slave_task_count_instance,
			"slave_task_count_ondemand": self.slave_task_count_ondemand,
			"master_instance_id": self.master_instance_id,
			"slave_instance_id": self.slave_instance_id,
			"subnet_id": self.subnet_id,
			"applications": self.applications,
			"spark_cores_per_executor": self.spark_cores_per_executor,
			"release_label": self.release_label,
			"tags": self.tags,
		}

	def __repr__(self):
		return "Cluster " + self.cluster_profile