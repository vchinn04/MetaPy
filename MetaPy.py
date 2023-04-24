class Metatable:
    def __init__(self, my_dict, meta_table):
        self.dict = my_dict
        self.meta = meta_table
    
    def setmetatable(dict, meta_dict):
        return Metatable(dict, meta_dict)

    def __getitem__(self, dict_key):
        if (dict_key not in self.dict):
            if ("__index" in self.meta):
                return self.meta["__index"](self.dict, dict_key)
            else:
                return None
        else:
            return self.dict[dict_key]

    def setitem(self, dict_key, value):
        self.dict[dict_key] = value
        if ("__newindex" in self.meta):
            self.meta["__newindex"](self.dict, dict_key, value)
            
    def getmetatable(self):
        return self.meta

    def __add__(self, obj):
        if ("__add" in self.meta):
            self.meta["__add"](self.dict, obj)

    def __call__(self, **kwargs):
        if ("__call" in self.meta):
            self.meta["__call"](self.dict, **kwargs)
