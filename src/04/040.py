id_name = {"01001":"felix","01005":"arne","01008":"samuel", "01015":"pia","01020":"matilda","01035":"kimo"}
name_id = {}
for id, name in id_name.items():#
    name_id[name] = id
print(name_id["pia"])