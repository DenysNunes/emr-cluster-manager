from metastore import instances as ins

if __name__ == "__main__":
    ins.set_metastore()
    print(ins.get_metastore())