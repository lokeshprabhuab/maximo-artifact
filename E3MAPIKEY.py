#############################################################################################
# Author    : Lokesh
# Date      : 26-04-22
# Logic     : Automatically generate API key if user is added to E3M Security Group
# Customer  : Region of PEEL
# Object    : GROUPUSER
# LauchPoint Event: Add
#############################################################################################
from psdi.security import UserInfo
from psdi.server import MXServer
# Obtain User ID and Group Name
userid=mbo.getString("USERID")
user_groupname=mbo.getString("GROUPNAME")
#groupname= ["E3MTECHNICIAN","E3MSUPERVISOR","E3MADMIN"]
groupname=MXServer.getMXServer().getProperty("mxe.e3m.apikey.group").split(",")
# Obtain APIKEYTOKEN MboSet. If apikey does not exist for user, then generate APIKEY
apikeySet=MXServer.getMXServer().getMboSet("APIKEYTOKEN",MXServer.getMXServer().getSystemUserInfo())
whereclause="userid='"+userid+"'"
apikeySet.setWhere(whereclause)
if (apikeySet.isEmpty()==True and (user_groupname in groupname)):
    apikey=apikeySet.add()
    apikey.setValue("USERID",userid)
    apikeySet.save()
apikeySet.close()