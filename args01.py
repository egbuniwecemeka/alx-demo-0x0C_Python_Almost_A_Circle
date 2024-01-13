def test_for_args(f_arg, *args):
    print("First argument is {}".format(f_arg))
    for arg in args:
        print("Another argument in *args is {}".format(arg))
    
test_for_args("Emmanuel", "Nifemi", "Yakubu", "Victoria")