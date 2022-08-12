Code used in the July Student League Qualifier: BreadCentric Loop

RaceV1 was a slight modification to the given reward functions. It combines the reward functions to stick to the center of the race track and minimize the steering angle.

SteerToPointAhead (RaceV2) was taken from falktan's deepracer repo: https://github.com/falktan/deepracer (https://medium.com/twodigits/aws-deepracer-how-to-train-a-model-in-15-minutes-3a0dca1175fb). I started to tweak the function but ended up scrapping this idea and using V3 as my final submission.

RaceV3 pushes the vehicle to finish the race as fast a possible by figuring out its own racing lines.

Versions 4, 5, and 6 made slight modifications to RaceV3 but weren't able to outperform Version 3.
Version 4 multiplies the speed input when returning the reward, Version 5 quadruples the speed input before squaring it, and Version 6 multiplies the speed input by 5 before squaring it. Version 6 also uses a SAC (Soft Actor Critic) algorithm wheras Versions 1 through 5 all use a PPO (Proximal Policy Optimization) algorithm.

RaceV3/CasefileV3 peaked around 57th in July and finished the race in 1:14 minutes placing in the top 5%.
