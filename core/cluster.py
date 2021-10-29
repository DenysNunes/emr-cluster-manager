from metastore import db
from metastore import base as bs

def runjobflow(cluster_profile: str):
	ss = bs.session
	cprof = db.get_clusters(ss, cluster_profile)[0]
	master_info = db.get_instances(ss, cprof.master_instance_id)[0]
	slave_info = db.get_instances(ss, cprof.slave_instance_id)[0]

	x = 0
	"""spark_executors_cores = cores_per_executor
    executor_per_instance = int(int(slave_data['yarn.cores']) / cores_per_executor)

    executor_memory = int(slave_data['yarn.nodemanager.resource.memory-mb']) / executor_per_instance

    spark_executors_memory = int(executor_memory * 0.90)
    spark_executor_memoryOverhead = int(executor_memory * 0.10)

    spark_driver_memory = int(int(master_data['yarn.nodemanager.resource.memory-mb']) * 0.4)
    spark_driver_cores = master_data['yarn.cores']
    spark_driver_memoryOverhead = int(int(master_data['yarn.nodemanager.resource.memory-mb'])  * 0.10)

    spark_executor_instances = (executor_per_instance * total_slave_count) - 1
    spark_default_parallelism = spark_executor_instances * spark_executors_cores * 2

    # -XX:ParallelGCThreads={spark_executors_cores} -XX:ConcGCThreads={spark_executors_cores * 2} -XX:XX:InitiatingHeapOccupancyPercent=35 

    emr_config = [
    {
      "Classification":"spark-log4j",
      "Properties":{
         "log4j.rootCategory":"WARN, console"
      },
      "Configurations":[
         
      ]
    },    
    {
        "Classification": "yarn-site",
        "Properties": {
            "yarn.app.mapreduce.am.resource.mb": slave_data["yarn.app.mapreduce.am.resource.mb"],
            "yarn.scheduler.minimum-allocation-mb": slave_data["yarn.scheduler.minimum-allocation-mb"],
            "yarn.scheduler.maximum-allocation-mb": slave_data["yarn.scheduler.maximum-allocation-mb"],
            "yarn.nodemanager.resource.memory-mb": slave_data["yarn.nodemanager.resource.memory-mb"]
        }
    },
    {
      "Classification":"yarn-env",
      "Properties":{
         
      },
      "Configurations":[
         {
            "Classification":"export",
            "Properties":{
               "ARROW_PRE_0_15_IPC_FORMAT":"1"
            },
            "Configurations":[
               
            ]
         }
      ]
   },
   {
      "Classification":"livy-env",
      "Properties":{
         
      },
      "Configurations":[
         {
            "Classification":"export",
            "Properties":{
               "ARROW_PRE_0_15_IPC_FORMAT":"1"
            },
            "Configurations":[
               
            ]
         }
      ]
    },
    {
        "Classification": "spark",
        "Properties": {
            "maximizeResourceAllocation": "false"
        }
    },
    {
        "Classification": "spark-defaults",
        "Properties": {
            "spark.network.timeout": "800s",
            "spark.driver.maxResultSize":"5g",
            "spark.executor.heartbeatInterval": "60s",
            "spark.dynamicAllocation.enabled": "false",
            "spark.driver.memory": "{}M".format(spark_driver_memory),
            "spark.executor.memory": "{}M".format(spark_executors_memory),
            "spark.executor.cores": str(spark_driver_cores),
            "spark.executor.instances": str(spark_executor_instances + 1),
            "spark.executor.memoryOverhead": "{}M".format(spark_executor_memoryOverhead),
            "spark.driver.memoryOverhead": "{}M".format(spark_executor_memoryOverhead),
            "spark.memory.fraction": "0.80",
            "spark.memory.storageFraction": "0.30",
            "spark.executor.extraJavaOptions": f"-XX:+UseG1GC -XX:+UnlockDiagnosticVMOptions -XX:+G1SummarizeConcMark -XX:InitiatingHeapOccupancyPercent=35 -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:OnOutOfMemoryError='kill -9 %p'",
            "spark.driver.extraJavaOptions": "-XX:+UseG1GC -XX:+UnlockDiagnosticVMOptions -XX:+G1SummarizeConcMark -XX:InitiatingHeapOccupancyPercent=35 -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:OnOutOfMemoryError='kill -9 %p'",
            "spark.yarn.scheduler.reporterThread.maxFailures": "5",
            "spark.storage.level": "MEMORY_AND_DISK",
            "spark.rdd.compress": "true",
            "spark.shuffle.compress": "true",
            "spark.shuffle.spill.compress": "true",
            "spark.default.parallelism": str(spark_default_parallelism),
            "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
            "spark.sql.execution.arrow.enabled": "true",
            "spark.sql.cbo.enabled": "true",
            "spark.sql.cbo.joinReorder.dp.star.filter": "true",
            "spark.sql.cbo.planStats.enabled": "true",
            "spark.sql.cbo.starSchemaDetection": "true"
        }
    },
    {
            "Classification": "mapred-site",
            "Properties": {
                "mapreduce.map.output.compress": "true",
                "mapreduce.map.java.opts": slave_data["mapreduce.map.java.opts"],
                "mapreduce.reduce.java.opts": slave_data["mapreduce.reduce.java.opts"],
                "mapreduce.map.memory.mb": slave_data["mapreduce.map.memory.mb"],
                "mapreduce.reduce.memory.mb": slave_data["mapreduce.reduce.memory.mb"]
            }
        },
        {
            "Classification": "spark-env",
            "Configurations": [{
                "Classification":"export",
                "Properties":{
                "PYSPARK_PYTHON":"/usr/bin/python3",
                "ARROW_PRE_0_15_IPC_FORMAT":"1"
                },
                "Configurations":[
                
                ]
            }],
            "Properties": {}
        },
        {
            "Classification":"hive-site",
            "Properties":{
                "hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"
            },
            "Configurations":[

            ]
        },
        {
            "Classification":"spark-hive-site",
            "Properties":{
                "hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"
            },
            "Configurations":[

            ]
        },
        {
            "Classification": "presto-connector-hive",
            "Properties":{
                "hive.metastore.glue.datacatalog.enabled":"true"
            },
            "Configurations":[
                
            ]
        },
        {
        "Classification": "emrfs-site",
        "Properties": {
            "fs.s3.maxRetries": "200"
        }
        }
    ]"""


