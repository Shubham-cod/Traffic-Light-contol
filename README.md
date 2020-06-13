# Traffic-Light-contol
Control 2 way traffic over a 1 way narrow lane using raspberry pi and PCA 9685.

With the increase in number of vehicles on roads it has become very important to have a good and reliable traffic light system. 
In this project we will be implementing such traffic light system which can be used to control 2 – way traffic on a narrow one lane bridge.

This system will be consisting of two traffic lights which will be controlled in four phases. Between each phases there will be
a time delay in order to allow the traffic to behave accordingly. In phase 1, traffic light 1 will be Red stopping the traffic
whereas traffic light 2 will be green allowing the traffic to go. In phase 2, traffic light 1 will glow both Red and Yellow signalling 
vehicles to be ready to go while traffic light 2 will become Yellow signalling vehicles to slow down and stop. In phase 3, 
traffic light 1 will become Green signalling traffic to go whereas traffic light 2 will become Red stopping the traffic.
In phase 4, traffic light 1 will become Yellow signalling traffic to slow down to stop whereas traffic light 2 will glow both
Red and Yellow signalling traffic to get ready to go.
These phases will be repeating in order to control the flow of traffic on one lane
