"""
This Script is used to add values entered in non persistent obj in Item Master
Created by Selva on 11-10-2016

"""

from psdi.mbo import MboConstants
from psdi.security import UserInfo
from psdi.server import MXServer
from psdi.mbo import MboSet

print 'nexus Executing WO dialog'
print 'Item Number '+ item
print 'Tem description' + desc

itemSet = mbo.getMboSet("ITEM");
itembo = itemSet.addAtEnd();
itembo.setValue("ITEMNUM", item);
itembo.setValue("DESCRIPTION", desc);
itemSet.save();