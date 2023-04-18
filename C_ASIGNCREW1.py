"""
This Script is used to assign labor from Crew to assignment at Task level from assignment 
manager App. 

Created by Selva on 13-9-16

"""

from psdi.mbo import MboConstants
from psdi.security import UserInfo
from psdi.server import MXServer
from psdi.mbo import MboSet

print 'max fun app: assignment manager update test'
crewname = mbo.getString("AMCREW");
modval   = mbo.isModified("AMCREW");
wonum = mbo.getString("WONUM");
stat =  mbo.getString("STATUS");
org  = mbo.getString("ORGID");


if modval == True:
 print 'inside true '
 crewSet = mbo.getMboSet("AMCREW");
 asgnmntset = mbo.getThisMboSet();
 crewmbo = crewSet.getMbo(0);
 if crewmbo is not None:
         laborSet = crewmbo.getMboSet("AMCREWLABOR");
         print 'fetched labor set'
         print laborSet.count();
         mxsevr = MXServer.getMXServer();
         userInfo = mbo.getThisMboSet().getUserInfo();
         asgnSet = mxsevr.getMboSet("ASSIGNMENT",userInfo);
         #asgnSet1 = mxsevr.getMboSet("ASSIGNMENT",userInfo);
         for i in range(0,laborSet.count()): 
               
               labmbo = laborSet.getMbo(i);
               if labmbo is not None:

                 laborcode = labmbo.getString("LABORCODE");
                 labAsgSet = labmbo.getMboSet("C_ASSIGNMENT");
                 print 'labor name'+laborcode
                 #assignset = mbo.getMboSet("C_REFASSIGN");
                 asgnSet.setWhere(" LABORCODE ='"+laborcode+"' and WONUM = '"+wonum+"' ");
                 asgnSet.reset();
                 print 'assignset.count '
                 print asgnSet.count()
                 print 'work order'+wonum
                 
                 if asgnSet.count() == 0 :
                   if   asgnSet is not None  :               
                    print 'inside assign set'
                    newasignmbo = asgnmntset.addAtEnd() ;
                    newasignmbo.setValue("WONUM", wonum,11L)
                    newasignmbo.setValue("LABORCODE", laborcode,11L) 
                    newasignmbo.setValue("STATUS", stat,11L) 
                    newasignmbo.setValue("orgid", org,11L)