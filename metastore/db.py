from sqlalchemy.orm import Session
from metastore import instances
from model import models, schemas

# Instances

def get_instances(session: Session, instance_name: str=None):
	if instance_name:
		return [session.query(models.Instance).filter(models.Instance.instance_name == instance_name).first()]
	else:
		return session.query(models.Instance).all()
		

def create_instance(session: Session, instance: schemas.Instance):
	db_item = models.Instance(**instance.dict())
	session.add(db_item)
	session.commit()
	session.refresh(db_item)
	return db_item


# Clusters


def get_clusters(session: Session, cluster_profile: str=None):
	if cluster_profile:
		return [session.query(models.Cluster).filter(models.Cluster.cluster_profile == cluster_profile).first()]
	else:
		return session.query(models.Cluster).all()
		

def create_cluster(session: Session, cluster: schemas.Cluster):
	db_item = models.Cluster(**cluster.dict())
	session.add(db_item)
	session.commit()
	session.refresh(db_item)
	return db_item
