#!/bin/python3
import random
import time
import numpy as np
import sys

import os
import math 
import pybullet
import pybullet_data
from datetime import datetime
import pybullet_data



ROBOT_URDF_PATH = "robots/gen3_robotiq.urdf"
TABLE_URDF_PATH = os.path.join(pybullet_data.getDataPath(), "table/table.urdf")
CUBE_URDF_PATH = os.path.join(pybullet_data.getDataPath(), "cube_small.urdf")


pybullet.connect(pybullet.GUI)
pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
pybullet.loadURDF("plane.urdf", [0, 0, -0.3], useFixedBase=True)
kinovaId = pybullet.loadURDF(ROBOT_URDF_PATH, [0, 0, 0], useFixedBase=True)
pybullet.resetBasePositionAndOrientation(kinovaId, [0, 0, 0], [0, 0, 0, 1])
kukaEndEffectorIndex = 6
numJoints = pybullet.getNumJoints(kinovaId)
if (numJoints != 7):
  print ("Num of Joints ", numJoints)
  print ("ERROR Joint is not 7")
  #exit()

pybullet.setGravity(0, 0, -10)
cubeStartPos = [0, 0, 1]
cubeStartOrientation = pybullet.getQuaternionFromEuler([0, 0, 0])

useRealTimeSimulation = 0

if (useRealTimeSimulation):
  pybullet.setRealTimeSimulation(1)

while 1:
  if (useRealTimeSimulation):
    pybullet.setGravity(0, 0, -10)
    sleep(0.01)  # Time in seconds.
  else:
    pybullet.stepSimulation()
