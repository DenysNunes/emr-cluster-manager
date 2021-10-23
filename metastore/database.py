from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import settings
from metastore import instances as inst
from models import base as bs

engine = create_engine(settings.metastore_query, echo=True)    
bs.Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


def drop_all():
	bs.Base.metadata.drop_all(bind=engine, tables=[bs.Cluster.__table__])
	bs.Base.metadata.drop_all(bind=engine, tables=[bs.Cluster.__table__])

def init_database():
    if session.query(bs.Instance).count() == 0:
        [session.add(i) for i in inst.get_metastore()]
        session.commit()

    if session.query(bs.Cluster).count() == 0:
        cluster : bs.Cluster = bs.Cluster()
        cluster.cluster_profile = "example_profile"
        cluster.bootstrap_path = "s3://example-bucket/myconfig/bootstrap.sh"
        cluster.slave_core_count_ondemand = 1
        cluster.slave_task_count_instance = 3
        cluster.master_instance_id = "m5.2xlarge"
        cluster.slave_instance_id = "r5.xlarge"
        cluster.subnet_id = "subnet-94r5y0be"
        cluster.applications = "{Hadoop,Spark,Ganglia,Hive,Tez,Zeppelin}"
        cluster.spark_cores_per_executor = 5
        cluster.release_label = "emr-6.3.0"
        cluster.tags = '[{"Key": "type", "Value": "example_profile" },{"Key": "env","Value": "prototype"}]'
        session.add(cluster)
        session.commit()
