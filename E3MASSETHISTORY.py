#//load("nashorn:mozilla_compat.js");

#///importClass(Packages.psdi.server.MXServer);
#//importClass(Packages.psdi.common.parse.ParserService);
#//importClass(Packages.psdi.mbo.SqlFormat);

#// response = {};
#//var responseBody;
#//var assetnum = request.getQueryParam("assetnum");
#//raise TypeError(.assetnum);
#//response.assetnum=assetnum
#//responseBody = JSON.stringify(response);

conKey = ""
con = ""
s = ""

try:
    conKey = mbo.getThisMboSet().getUserInfo().getConnectionKey();
    con = mbo.getThisMboSet().getMboServer().getDBConnection(conKey)
    s = con.createStatement()
    val = "select wonum from workorder where assetnum = '" + mbo.getString("assetnum") + "'"
    rs = s.execute(val)
    con.commit()
finally:
    if s != "":
        s.close()
    if conKey != "" and con != "":
        mbo.getThisMboSet().getMboServer().freeDBConnection(conKey)