def args_or_kwargs_call(arg1, arg2, arg3):
    print("{}, {}, {}".format(arg1, arg3, arg2))

args = ("BXNN", "Omah lay", "Burna")
args_or_kwargs_call(*args)

kwargs = {"arg1": "FC", "arg2":25, "arg3": "WH"}
args_or_kwargs_call(**kwargs)