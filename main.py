from fastapi import FastAPI, HTTPException
from typing import Optional
from metastore import base as bs, db
from model import models, schemas
from config import settings

app = FastAPI()

bs.init_database()

@app.post("/instances/", response_model=schemas.Instance)
async def instances(instance: schemas.Instance):
    db.create_instance(instance)

    if instance:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return db.create_instance(instance=instance)

#@app.get("/clusters/")
#async def clusters(cluster_profile: Optional[str] = None):
#    if cluster_profile:
#        clust = db.session.query(bs.Cluster).filter_by(cluster_profile=cluster_profile).first()

#        if clust:
#            return {"clusters": [clust.json()]}
#        else:
#            return {"clusters": {}}        
#    else:
#        return {"clusters" : [i.json() for i in db.session.query(bs.Cluster).all()]}
