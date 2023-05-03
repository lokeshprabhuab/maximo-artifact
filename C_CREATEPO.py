from psdi.server import MXServer
from psdi.mbo import Mbo
from psdi.mbo import MboConstants
from psdi.app.pr import PR
from psdi.app.pr import PRRemote

mbo.changeStatus("APPR", MXServer.getMXServer().getDate(),"");
mbo.setFlag(MboConstants.NOACCESSCHECK, 0);
mbo.createPOsFromPR(MXServer.getMXServer().getDate());