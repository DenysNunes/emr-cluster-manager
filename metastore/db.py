from sqlalchemy.orm import Session
from metastore import instances
from model import models, schemas

# Instances


def get_instances(session: Session):
	return session.query(models.Instance).all()


def get_instance(session: Session, instance_name: str):
	return session.query(models.Instance).filter(models.Instance.instance_name == instance_name).first()


def create_instance(session: Session, instance: schemas.Instance):
	db_item = models.Instance(**instances.dict())
	session.add(db_item)
	session.commit()
	session.refresh(db_item)
	return db_item

# Clusters

