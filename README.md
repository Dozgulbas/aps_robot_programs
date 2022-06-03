# aps_droplet
This repository consists a documentation for the "Droplet" experiment to be performed at APS, Argonne National Laboratory.

## RoboDK

For this experiment, RoboDK software has been utilized and 3D CAD drawings have been exported into the simulation environment identical to the actual experimental environment located at APS/8_ID_I. An UR3e robot has been programmed to perform the "Droplet" experiment and a Python program is implemented to establish palletizing movements on the 96 pipette tips.

## Python palletizing program
`robodk_scripts/96_tip_simulation` This program performs the full experiment by each time picking up a new tip from the tip bin. 
# Installation 

To install the RoboDK library 

`pip install robodk`
