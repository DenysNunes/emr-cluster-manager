from fastapi import FastAPI
from typing import Optional

#from requests.sessions import session
from model import schemas, models
from metastore import db
from typing import List

app = FastAPI()

from core import cluster as c

models.init_database()

c.runjobflow("example_profile")

x =0



@app.post("/instances/", response_model=schemas.Instance)
async def instances(inst: schemas.Instance):
    r = db.create_instance(models.session, inst)    
    return r


@app.get("/instances/", response_model=List[schemas.Instance])
async def instances(instance_name: Optional[str] = None):
    return db.get_instances(models.session, instance_name)


@app.post("/clusters/", response_model=schemas.Cluster)
async def clusters(clst: schemas.Cluster):
    r = db.create_cluster(models.session, clst)    
    return r


@app.post("/jobflow/", response_model=List[schemas.Cluster])
async def clusters(cluster_profile: Optional[str] = None):
    return db.get_clusters(models.session, cluster_profile)   