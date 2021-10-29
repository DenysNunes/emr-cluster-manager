from fastapi import FastAPI, HTTPException
from typing import Optional
from metastore import base as bs, db
from model import schemas
from typing import List

app = FastAPI()


from core import cluster as c
c.runjobflow("example_profile")

bs.init_database()

@app.post("/instances/", response_model=schemas.Instance)
async def instances(inst: schemas.Instance):
    r = db.create_instance(bs.session, inst)    
    return r


@app.get("/instances/", response_model=List[schemas.Instance])
async def instances(instance_name: Optional[str] = None):
    return db.get_instances(bs.session, instance_name)


@app.post("/clusters/", response_model=schemas.Cluster)
async def clusters(clst: schemas.Cluster):
    r = db.create_cluster(bs.session, clst)    
    return r


@app.post("/jobflow/", response_model=List[schemas.Cluster])
async def clusters(cluster_profile: Optional[str] = None):
    return db.get_clusters(bs.session, cluster_profile)   