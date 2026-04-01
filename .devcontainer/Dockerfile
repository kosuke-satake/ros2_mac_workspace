# 1. THE FOUNDATION (Skips your first 14 lines of native setup)
FROM osrf/ros:jazzy-desktop

# 2. INSTALL YOUR SPECIFIC TOOLS (The last 3 lines of your native script)
RUN apt-get update && apt-get install -y \
    git \
    ros-dev-tools \
    ros-jazzy-turtlesim \
    nano \
    && rm -rf /var/lib/apt/lists/*

# 3. AUTOMATE THE SOURCING
# This runs the setup.bash automatically every time you open a VS Code terminal
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc