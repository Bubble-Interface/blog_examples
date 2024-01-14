from functools import wraps

def singleton(class_):
    instances = {}

    @wraps(class_)
    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)

        return instances[class_]

    return get_instance
