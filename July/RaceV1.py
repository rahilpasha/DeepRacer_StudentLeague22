def reward_function(params):

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    steering = abs(params['steering_angle'])
    is_reversed = params['is_reversed']
    left = params['is_left_of_center']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Set the reward to 0
    reward = 0
    
    # Give higher reward if the car is closer to center line and vice versa
    if left:
        reward += 0.2
    elif distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3 # likely crashed

    # add speed penalty
    if speed < 1.0:
        reward *= 0.80
    else:
        reward += speed
    
    # Add penalty for going in the wrong direction
    if is_reversed:
        reward = 1e-3
    
    # Steering penality threshold set to 20 degrees
    ABS_STEERING_THRESHOLD = 20

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.75  # cuts off 25% from the reward
    
    return float(reward)
