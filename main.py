from fastapi import FastAPI
from typing import Optional
from metastore import database as db
from models import base as bs
from config import settings

app = FastAPI()

db.init_database()

@app.get("/instances/")
async def instances(instance_name: Optional[str] = None):
    if instance_name:
        inst = db.session.query(bs.Instance).filter_by(instance_name=instance_name).first()

        if inst:
            return {"instances" : [inst.json()]}
        else:
            return {"instances": {}}
    else:
        return {"instances" : [i.json() for i in db.session.query(bs.Instance).all()]}


@app.get("/clusters/")
async def clusters(cluster_profile: Optional[str] = None):
    if cluster_profile:
        clust = db.session.query(bs.Cluster).filter_by(cluster_profile=cluster_profile).first()

        if clust:
            return {"clusters": [clust.json()]}
        else:
            return {"clusters": {}}        
    else:
        return {"clusters" : [i.json() for i in db.session.query(bs.Cluster).all()]}
