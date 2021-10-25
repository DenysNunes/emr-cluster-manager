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

	def __repr__(self):
		return "Cluster " + self.cluster_profile