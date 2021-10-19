from pydantic import BaseModel
from fastapi import FastAPI


class Instance(BaseModel):
    mapreduce_map_java_opts: str
    mapreduce_reduce_java_opts: str
    mapreduce_map_memory_mb: str
    mapreduce_reduce_memory_mb: str
    yarn_scheduler_minimum_allocation: str
    yarn_scheduler_maximum_allocation_mb: str
    yarn_nodemanager_resource_memory_mb: str
    yarn_cores: int