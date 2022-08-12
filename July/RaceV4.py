def reward_function(params):

    # Create variables for each parameter used
    steps = params["steps"]
    progress = ["progress"] # a percentage
    
    speed = ["speed"]
    
    on_track = params["all_wheels_on_track"]
    
    
    if on_track and steps > 0:
        reward = (speed * 2) + ((progress / steps) * 100) # doubles speed and adds it to the progress per step taken
    else:
        reward = 1e-3 # lowest reward possible
        
    return float(reward)
