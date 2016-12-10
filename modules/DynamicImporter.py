class DynamicImporter:
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, module_name, class_name):
        """Constructor"""
        module = __import__(module_name)
        my_class = getattr(module, class_name)
        instance = my_class()
        print instance
 
