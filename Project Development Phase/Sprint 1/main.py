# Python code

# IMPORT SECTION STARTS

import brain

# IMPORT SECTION ENDS
# -----------------------------------------------
# USER INPUT SECTION STARTS

myLocation = "salem"
APIKEY = "89c5555fdfc2d13eaec579cf3d647a2a"

localityInfo = {
    "schools" : {
        "schoolZone" : True,
        "activeTime" : ["7:00","17:30"] # schools active from 7 AM till 5:30 PM
        },
    "hospitalsNearby" : True,
    "usualSpeedLimit" : 40 # in km/hr
    }

# USER INPUT SECTION ENDS
# -----------------------------------------------
# MICRO-CONTROLLER CODE STARTS

print(brain.processConditions(myLocation,APIKEY,localityInfo))

'''
MICRO CONTROLLER CODE WILL BE ADDED IN SPRINT 2 AS PER OUR PLANNED SPRINT SCHEDULE
'''

# MICRO-CONTROLLER CODE ENDS
