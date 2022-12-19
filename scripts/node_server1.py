#! /usr/bin/env python3
# remember to make this file executable (`chmod +x`) before trying to run it

import rospy
from std_srvs.srv import Trigger
from controlled_node import Node

if __name__ == '__main__':
    rospy.init_node('node_server1')
        
    start_from_startup = rospy.get_param('~start_from_startup', False)  # whether to start node already recording
    
    rate = rospy.Rate(1) # 1hz 
    
    # Start recorder object
    node = Node(start_from_startup)
    
    # Services  
    start_service = rospy.Service('~start', Trigger, node.start_srv)
    stop_service = rospy.Service('~stop', Trigger, node.stop_srv)

    # Node is also stopped on node shutdown. This allows stopping to be done via service call or regular Ctrl-C
    rospy.on_shutdown(node.stop_srv)
    
    counter = 0

    while not rospy.is_shutdown():
        if node.stopped:  # stop node if recording has finished
            break
        
        elif node.started:
            """
            # PUT YOUR CODE HERE
            
            # to stop the node when done with its tasks:
            node.stop_srv()
            """
            if counter >= 10:
                node.stop_srv()
                
            rospy.loginfo("%s is doing stuff", rospy.get_name())
            counter += 1
        
        rate.sleep()