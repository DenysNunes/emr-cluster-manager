
from metastore import instances as inst
from tornado.web import RequestHandler

data_inst = inst.get_metastore()

class Instances(RequestHandler):
    def get(self, instance_name):
        if not instance_name:
            self.write({'instances': data_inst})
        else:
            self.write({instance_name: data_inst[instance_name]})