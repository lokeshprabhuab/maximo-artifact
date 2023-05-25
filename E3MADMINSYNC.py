################################################################################## 
#Purpose         		: Technician/Supervisor: display warning msg if any changes in admin app
#Version        		: 1.0
#Create By				: Harini
#Last Modified By		: Harini
#Last Modified Date		: 10-05-2023
#Last Modified Comment	: changed the description
#API Name               : Not Applicable
#Realted Script         : Not Applicable
################################################################################## 
if launchPoint=="E3MTECHNICIAN" and  mbo.isModified()==True:
    owner=mbo.getOwner()
    owner.setValue("E3MDIRECT",True)
    owner.getThisMboSet().save()
    
    
    
if launchPoint=="E3MADMINOBJECT" and  mbo.isModified()==True:
    owner=mbo.getOwner().getOwner()
    owner.setValue("E3MDIRECT",True)