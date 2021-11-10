from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
from metastore import instances as inst

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

	def __repr__(self):
		return "Instance " + self.cluster_profile
		

class Cluster(Base):
	__tablename__ = 'clusters'

	cluster_profile = Column(String(50), primary_key=True)
	bootstrap_path = Column(String(200))
	log_path = Column(String(200))
	slave_core_count_ondemand = Column(Integer)
	slave_task_count_ondemand = Column(Integer)
	slave_task_count_spot = Column(Integer)
	master_instance_id = Column(String(50), ForeignKey('instances.instance_name'))
	slave_instance_id = Column(String(50), ForeignKey('instances.instance_name'))
	subnet_id = Column(String(50))
	applications = Column(String(150))
	spark_cores_per_executor = Column(Integer)
	glue_spark_metastore = Column(Boolean)
	glue_hive_metastore = Column(Boolean)
	glue_presto_metastore = Column(Boolean)
	release_label = Column(String(10))
	jobflow_role = Column(String(100))
	service_role = Column(String(100))
	tags = Column(String(150))

	def __repr__(self):
		return "Cluster " + self.cluster_profile




engine = create_engine(settings.metastore_query, echo=True)  
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

def init_database():
	if session.query(Instance).count() == 0:
		[session.add(Instance(**i)) for i in inst.get_metastore()]
		session.commit()

	if session.query(Cluster).count() == 0:
		cluster : Cluster = Cluster()
		cluster.cluster_profile = "example_profile"
		cluster.bootstrap_path = "s3://example-bucket/myconfig/bootstrap.sh"
		cluster.log_path = "s3://example-bucket/emr-logs/"
		cluster.slave_core_count_ondemand = 1
		cluster.slave_task_count_ondemand = 0
		cluster.slave_task_count_spot = 3
		cluster.master_instance_id = "m5.2xlarge"
		cluster.slave_instance_id = "r5.xlarge"
		cluster.subnet_id = "subnet-94r5y0be"
		cluster.applications = "{Hadoop,Spark,Ganglia,Hive,Tez,Zeppelin}"
		cluster.spark_cores_per_executor = 2
		cluster.glue_spark_metastore = True
		cluster.glue_hive_metastore = True
		cluster.glue_presto_metastore = True
		cluster.log_path = True
		cluster.release_label = "emr-6.3.0"
		cluster.jobflow_role = "myRole"
		cluster.service_role = "myRole"
		cluster.tags = '[{"Key": "type", "Value": "example_profile" },{"Key": "env","Value": "prototype"}]'
		session.add(cluster)
		session.commit()