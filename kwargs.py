def test_for_kwargs(**kwargs):
    """ kwargs function definition """
    
    if kwargs is not None:
        """ check for non-empty parameter list """
        
        for key, value in kwargs.items():
            print("{:s} = {:s}".format(key, value))
            
test_for_kwargs(Diallo ="Amad", Aleandro = "Garnacho")