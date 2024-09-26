#!/bin/zsh

# zsh shell for macos
source ~/.zshrc

# This code will download and install micromamba for MacOS and create
# two python environments for the course.

# The first environment has AI/ML and GIS pacakges needed
# The second environment has the DSP packages needed

dir_to_download_to="/Users/beckie/Documents/Portsmouth/Training_Courses/Phase_2/yamls"

micromamba env create --name UKSA_course_env -c conda-forge --file ${dir_to_download_to}/UKSA_course.yaml
micromamba activate UKSA_course_env
micromamba list 
jupyter lab &
#micromamba deactivate

# To remove
#micromamba env remove --name test

