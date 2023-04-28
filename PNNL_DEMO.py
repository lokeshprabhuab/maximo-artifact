#############################################################################################
# Author    : Lokesh
# Date      : 28-04-23
# Logic     : Set Work Priority to 1 If Work Type is CM for Lokesh User
# Customer  : PNNL
# Object    : WORKORDER
# LauchPoint Event: Add, Before Save
#############################################################################################
worktype=mbo.getString("WORKTYPE")
if (worktype=="CM"):
    wopriority=1