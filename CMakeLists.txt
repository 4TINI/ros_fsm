cmake_minimum_required(VERSION 3.0.2)
project(ros_fsm)

find_package(catkin REQUIRED)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ros_fsm
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
# ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############
install(PROGRAMS
  scripts/node_client.py
  scripts/node_server1.py
  scripts/node_server2.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch/
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)