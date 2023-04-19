# Purpose         		: Move Asset functionality for transactions created from mobile
# Create By				: Abhinav
# Last Modified By		: Ashwini
# Last Modified Date	: 2022-DEC-20
# Last Modified Comment	: Added condition to check if movetolocation and movetoparent values are different from current value then only move the asset

isparentModified = 0
islocationModified = 0
isreplcaementModified = mbo.isModified('replaceassetnum')
recordclass = mbo.getString('recordclass')

if(mbo.isModified('movetolocation')):
   if (not mbo.getMboValue("movetolocation").getInitialValue().asString() == mbo.getString("movetolocation")):
       islocationModified=1
       
if(mbo.isModified('movetoparent')):
   if (not mbo.getMboValue("movetoparent").getInitialValue().asString() == mbo.getString("movetoparent")):
       isparentModified=1

if not interactive:
    if (isparentModified or islocationModified or isreplcaementModified) and recordclass in ('WORKORDER', 'ACTIVITY'):
        mbo.moveAsset()