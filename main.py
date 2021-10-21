from fastapi import FastAPI
from typing import Optional
from metastore import instances as inst

app = FastAPI()

@app.get("/instances/")
async def instances(instance_id: Optional[str] = None):
    app.lock = True
    instances = inst.get_metastore()
    app.lock = False

    if instance_id:
        return {"instances" : instances[instance_id]}
    else:
        return {"instances" : instances}