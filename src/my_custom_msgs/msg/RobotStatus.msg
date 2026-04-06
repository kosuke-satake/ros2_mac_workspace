# RobotStatus.msg
# This is a custom data type describing the overall status of the robot.

# 1. The battery percentage (integer between 0 and 100)
int32 battery_percentage

# 2. A string explaining what the robot is doing right now (e.g., "Driving", "Charging")
string current_state

# 3. A boolean indicating if something has gone horribly wrong (True) or if we are okay (False)
bool has_error