EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2
def bake_time_remaining(elapsed_bake_time):
    """
    Returns the time for which the lasagna has been inside the oven.
    Takes elapsed bake time as a parameter and uses constant preparation time
    given in the recipe for calculation.
    """
    return EXPECTED_BAKE_TIME-elapsed_bake_time
    
def  preparation_time_in_minutes(number_of_layers):
    """
    Returns the preparation time required in minutes, depending upon the number of
    layers in lasagna.
    Takes one parameter i.e. number_of_layers and uses constant preparation
    time required per layer given in recipe book for calculation.
    """
    return PREPARATION_TIME*number_of_layers
def  elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """
    Return elapsed cooking time.
    This function takes two numbers representing the number of layers & the time       already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return (PREPARATION_TIME*number_of_layers)+elapsed_bake_time
