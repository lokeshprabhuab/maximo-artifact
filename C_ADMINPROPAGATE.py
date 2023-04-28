from psdi.mbo import MboConstants
from psdi.security import UserInfo
from psdi.server import MXServer
from psdi.mbo import MboSet
from psdi.mbo import MboSetRemote

techdataSet=mbo.getThisMboSet()
techdataSet=mbo.getMboSet("E3MTECHNICIAN")
wherestring="E3MADMINNUM ='AUTO'"
autotechSet=mbo.getMboSet("C_PROPA")
techdataSet=techdataSet.getMbo(0)
auto=autotechSet.getMbo(0)

bul=techdataSet.getString("E3MADMINID")
#raise TypeError(bul)
auto.setValue("E3MALLOWATTACHMENTS",techdataSet.getInt("E3MALLOWATTACHMENTS"),11L)
auto.setValue("E3MALLOWTZMISMATCH",techdataSet.getInt("E3MALLOWTZMISMATCH"),11L)
auto.setValue("E3MALLOWVIDEO",techdataSet.getInt("E3MALLOWVIDEO"),11L)
auto.setValue("E3MAPPLEMAPS",techdataSet.getInt("E3MAPPLEMAPS"),11L)
auto.setValue("E3MARCGIS",techdataSet.getInt("E3MARCGIS"),11L)
auto.setValue("E3MARCGISURL",techdataSet.getString("E3MARCGISURL"),11L)
auto.setValue("E3MARCMAP",techdataSet.getInt("E3MARCMAP"),11L)
auto.setValue("E3MASSETHIST",techdataSet.getInt("E3MASSETHIST"),11L)
auto.setValue("E3MASSETMENU",techdataSet.getInt("E3MASSETMENU"),11L)
auto.setValue("E3MASSIGNWO",techdataSet.getInt("E3MASSIGNWO"),11L)
auto.setValue("E3MATTACHMENTPATH",techdataSet.getString("E3MATTACHMENTPATH"),11L)
auto.setValue("E3MBULKDATAURL",techdataSet.getString("E3MBULKDATAURL"),11L)
auto.setValue("E3MCREATEMR",techdataSet.getInt("E3MCREATEMR"),11L)
auto.setValue("E3MCREATESR",techdataSet.getInt("E3MCREATESR"),11L)
auto.setValue("E3MCREATEWO",techdataSet.getInt("E3MCREATEWO"),11L)
auto.setValue("E3MDASHBOARDMENU",techdataSet.getInt("E3MDASHBOARDMENU"),11L)
auto.setValue("E3MDRMENU",techdataSet.getInt("E3MDRMENU"),11L)
auto.setValue("E3MFILEDESTINATION",techdataSet.getString("E3MFILEDESTINATION"),11L)
auto.setValue("E3MFOLLOWUPSRFROMWO",techdataSet.getInt("E3MFOLLOWUPSRFROMWO"),11L)
auto.setValue("E3MFOLLOWUPWOFROMSR",techdataSet.getInt("E3MFOLLOWUPWOFROMSR"),11L)
auto.setValue("E3MFOLLOWUPWOFROMWO",techdataSet.getInt("E3MFOLLOWUPWOFROMWO"),11L)
auto.setValue("E3MGOOGLE",techdataSet.getInt("E3MGOOGLE"),11L)
auto.setValue("E3MINSPECTIONMENU",techdataSet.getInt("E3MINSPECTIONMENU"),11L)
auto.setValue("E3MMAPISLDAP",techdataSet.getInt("E3MMAPISLDAP"),11L)
auto.setValue("E3MMAPSERVER",techdataSet.getString("E3MMAPSERVER"),11L)
auto.setValue("E3MMAPURL",techdataSet.getString("E3MMAPURL"),11L)
auto.setValue("E3MMAPUSER",techdataSet.getString("E3MMAPUSER"),11L)
auto.setValue("E3MMAPWD",techdataSet.getString("E3MMAPWD"),11L)
auto.setValue("E3MMATERIALMODE",techdataSet.getString("E3MMATERIALMODE"),11L)
auto.setValue("E3MMODIFYASSET",techdataSet.getInt("E3MMODIFYASSET"),11L)
auto.setValue("E3MMOVEASSET",techdataSet.getInt("E3MMOVEASSET"),11L)
auto.setValue("E3MOPENWO",techdataSet.getInt("E3MOPENWO"),11L)
auto.setValue("E3MPRINTASSET",techdataSet.getInt("E3MPRINTASSET"),11L)
auto.setValue("E3MREASSIGNWF",techdataSet.getInt("E3MREASSIGNWF"),11L)
auto.setValue("E3MRESCHEDULE",techdataSet.getInt("E3MRESCHEDULE"),11L)
auto.setValue("E3MSCANASSETMENU",techdataSet.getInt("E3MSCANASSETMENU"),11L)
auto.setValue("E3MSELFREG",techdataSet.getInt("E3MSELFREG"),11L)
auto.setValue("E3MSHAREPOINTHOST",techdataSet.getString("E3MSHAREPOINTHOST"),11L)
auto.setValue("E3MSHOWCHATBOT",techdataSet.getInt("E3MSHOWCHATBOT"),11L)
auto.setValue("E3MSHOWDIRECTISSUE",techdataSet.getInt("E3MSHOWDIRECTISSUE"),11L)
auto.setValue("E3MSHOWMODULARVIEW",techdataSet.getInt("E3MSHOWMODULARVIEW"),11L)
auto.setValue("E3MSHOWSIGNUP",techdataSet.getInt("E3MSHOWSIGNUP"),11L)
auto.setValue("E3MSRMENU",techdataSet.getInt("E3MSRMENU"),11L)
auto.setValue("E3MTAKEOWNERSHIP",techdataSet.getInt("E3MTAKEOWNERSHIP"),11L)
auto.setValue("E3MTODOSR",techdataSet.getInt("E3MTODOSR"),11L)
auto.setValue("E3MTODOWO",techdataSet.getInt("E3MTODOWO"),11L)
auto.setValue("E3MVIEWMR",techdataSet.getInt("E3MVIEWMR"),11L)
auto.setValue("E3MVIEWSR",techdataSet.getInt("E3MVIEWSR"),11L)
auto.setValue("E3MVIEWWO",techdataSet.getInt("E3MVIEWWO"),11L)
auto.setValue("E3MVIEWWOMENU",techdataSet.getInt("E3MVIEWWOMENU"),11L)
auto.setValue("E3MWOCREATESTATUS",techdataSet.getString("E3MWOCREATESTATUS"),11L)

autotechSet.save()

#techmbo=techdataSet.getMbo(0)
#raise TypeError(techdataSet.getInt("E3MTECHNICIANID"))

e3mwhereset=techdataSet.getMboSet("E3MWHERE")
e3mwhereset.reset()
wherecount=e3mwhereset.count()

e3mwhereautoset=auto.getMboSet("E3MWHERE")
e3mwhereautoset.reset()
e3mwhereautocount=e3mwhereautoset.count()
for i in range(0,wherecount):
    wherembo=e3mwhereset.getMbo(i)
    
    techclause=wherembo.getString("E3MCLAUSETYPE")
    wherestring="E3MCLAUSETYPE='"+techclause+"'"
    e3mwhereautoset.setWhere(wherestring)
    e3mwhereautoset.reset()
    whereautombo=e3mwhereautoset.getMbo(0)
     
    
    if whereautombo is not None:
        #raise TypeError(techclausetype,whereautombo.getString("E3MCLAUSETYPE"))

        whereautombo.setValue("E3MWHERE",wherembo.getString("E3MWHERE"),11L)
    
        e3mwhereautoset.save()


e3madminobjectmbo=techdataSet.getMboSet("E3MADMINOBJECT")
e3madminobjectmbo.reset()
for j in range(0,e3madminobjectmbo.count()):
    e3mautoadminstat=auto.getMboSet("E3MADMINOBJECT")
    e3mautoadminstat.reset()
    e3mautofromstatcount=e3mautoadminstat.count()
    e3madminmbo=e3madminobjectmbo.getMbo(j)
    e3madminobjname=e3madminmbo.getString("E3MOBJECTNAME")
    wherestring="E3MOBJECTNAME='"+e3madminobjname+"'"
    e3mautoadminstat.setWhere(wherestring)
    e3mautoadminstat.reset()
    e3mautoadminmbo=e3mautoadminstat.moveFirst()
    
    e3mfromstatusset=e3madminmbo.getMboSet("E3MFROMSTATUS")
    e3mfromstatusset.reset()
    e3mfromstatcount=e3mfromstatusset.count()
    
    if e3mautoadminmbo is not None:
        e3mautofromset=e3mautoadminmbo.getMboSet("E3MFROMSTATUS")
        e3mautofromset.reset()
        e3mautofrstatcount=e3mautofromset.count()
    #raise TypeError(e3mautofromstatcount,e3mautoadminmbo.getString("E3MOBJECTNAME"),e3madminmbo.getString("E3MOBJECTNAME"))
    
        for k in range(0,e3mfromstatcount):
            e3mfromstatmbo=e3mfromstatusset.getMbo(k)
            e3mfromstatobj=e3mfromstatmbo.getString("E3MFROMSTATUS")
            for k in range(0,e3mautofromstatcount):
                #e3mautostatmbo=e3mautofromset.getMbo(k)
                wherestring="E3MFROMSTATUS='"+e3mfromstatobj+"'"
                e3mautofromset.setWhere(wherestring)
                e3mautofromset.reset()
                e3mautostatmbo=e3mautofromset.getMbo(k)
                if e3mautostatmbo is not None:
                    #raise TypeError(e3mfromstatmbo.getString("DESCRIPTION"),e3mautostatmbo.getString("DESCRIPTION"))
                    e3mautostatmbo.setValue("E3MMAXVALUE",e3mfromstatmbo.getString("E3MMAXVALUE"),11L)
                    e3mautostatmbo.setValue("DESCRIPTION",e3mfromstatmbo.getString("DESCRIPTION"),11L)
                    e3mautostatmbo.setValue("E3MTERMINATING",e3mfromstatmbo.getString("E3MTERMINATING"),11L)
                    e3mautofromset.save()
                    e3mtostatusSet=e3mfromstatmbo.getMboSet("E3MTOSTATUS")
                    e3mtostatusSet.reset()
                    e3mtostatcount=e3mtostatusSet.count()
                    e3mautotostatSet=e3mautostatmbo.getMboSet("E3MTOSTATUS")
                    e3mautotostatSet.reset()
                    e3mautotocount=e3mautotostatSet.count()
                    for k in range(0,e3mtostatcount):
                        e3mtostatmbo=e3mtostatusSet.getMbo(k)
                        if e3mtostatmbo is not None:
                            e3mtostatobj=e3mtostatmbo.getString("E3MTOSTATUS")
                            for k in range(0,e3mautotocount):
                                wherestring="E3MTOSTATUS='"+e3mtostatobj+"'"
                                e3mautotostatSet.setWhere(wherestring)
                                e3mautotostatSet.reset()
                                e3mtotostatmbo=e3mautotostatSet.getMbo(k)
                                if e3mtotostatmbo is not None:
                        
                                    #raise TypeError(e3mautotocount,e3mtotostatmbo.getString("DESCRIPTION"),e3mtostatmbo.getString("DESCRIPTION"))
                                    e3mtotostatmbo.setValue("E3MMAXVALUE",e3mtostatmbo.getString("E3MMAXVALUE"),11L)
                                    e3mtotostatmbo.setValue("DESCRIPTION",e3mtostatmbo.getString("DESCRIPTION"),11L)
                                    e3mautotostatSet.save()
                                    e3mautotostatSet.close()
                                    e3mtostatusSet.close()

e3madminobjset=techdataSet.getMboSet("E3MADMINOBJECT")
e3madminobjset.reset()
adminobjcount=e3madminobjset.count()

for i in range(0,adminobjcount):
    e3mautoadmobjset=auto.getMboSet("E3MADMINOBJECT")
    e3mautoadmobjset.reset()
    e3mautoobjcount=e3mautoadmobjset.count()
    e3madminobjmbo=e3madminobjset.getMbo(i)
    e3madminobjnam=e3madminobjmbo.getString("E3MOBJECTNAME")
    wherestring="E3MOBJECTNAME='"+e3madminobjnam+"'"
    e3mautoadmobjset.setWhere(wherestring)
    e3mautoadmobjset.reset()
    e3mautoadmmbo=e3mautoadmobjset.moveFirst()
    
    e3mtabset=e3madminobjmbo.getMboSet("E3MADMINTAB")
    e3mtabset.reset()
    e3mtabsetcount=e3mtabset.count()
    
    if e3mautoadmmbo is not None:
        e3mautotabset=e3mautoadmmbo.getMboSet("E3MADMINTAB")
        e3mautotabset.reset()
        e3mautotabcount=e3mautotabset.count()
    for k in range(0,e3mtabsetcount):
        e3mtabmbo=e3mtabset.getMbo(k)
        e3mtabname=e3mtabmbo.getString("E3MTABNAME")
        for k in range(0,e3mautotabcount):
            wherestring="E3MTABNAME='"+e3mtabname+"'"
            e3mautotabset.setWhere(wherestring)
            e3mautotabset.reset()
            e3mautotabmbo=e3mautotabset.getMbo(k)
            if e3mautotabmbo is not None:
                e3mautotabmbo.setValue("E3MORDERNUM",e3mtabmbo.getInt("E3MORDERNUM"),11L)
                e3mautotabmbo.setValue("E3MISHIDDEN",e3mtabmbo.getInt("E3MISHIDDEN"),11L)
                e3mautotabset.save()
                e3mautotabset.close()
#techdataSet.close()
autotechSet.close()
e3madminobjectmbo.close()
e3mfromstatusset.close()
e3mautoadminstat.close()
e3mautofromset.close()
e3madminobjset.close()
e3mwhereset.close()
e3mwhereautoset.close()
e3mautoadmobjset.close()
e3mtabset.close()
e3mautotabset.close()
service.invokeScript("C_ADMINSUPPROPAGATE")