from psdi.server import MXServer;


srSet = MXServer.getMXServer().getMboSet("SR", MXServer.getMXServer().getSystemUserInfo());
newSR = srSet.add();
if('assetnum' in request.getQueryParam("Body")):
 array=request.getQueryParam("Body").split();
 j=array.index("assetnum")
 newSR.setValue("DESCRIPTION", request.getQueryParam("Body"));
 newSR.setValue("REPORTEDPHONE", request.getQueryParam("From"));
 newSR.setValue("ASSETNUM", array[j+1]);
 srSet.save();
else:
 newSR.setValue("DESCRIPTION", request.getQueryParam("Body"));
 newSR.setValue("REPORTEDPHONE", request.getQueryParam("From"));
 srSet.save();