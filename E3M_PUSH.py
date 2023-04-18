from psdi.mbo import MboConstants
from psdi.security import UserInfo
from psdi.server import MXServer
from java.io import OutputStream
from java.io import BufferedReader
from java.io import IOException
from java.net import HttpURLConnection
from java.net import URL
from java.util import Base64
from java.lang import String

autoscriptName=mbo.getString("AUTOSCRIPT")
source=mbo.getString("SOURCE")
sourceCode=Base64.getEncoder().encodeToString(String(source).getBytes("UTF-8"));
gitHubApi=MXServer.getMXServer().getProperty("e3m.github.api")+autoscriptName+".py"
gitHubToken=MXServer.getMXServer().getProperty("e3m.github.token")
githubcontent = String.format("{\"message\":\"Add file\",\"content\":\"%s\"}",sourceCode);

url = URL(gitHubApi)
con= url.openConnection()
con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json")
con.setRequestProperty("Authorization", "Bearer " + gitHubToken)
con.setDoOutput(True)

os = con.getOutputStream()
content=String(githubcontent).getBytes("UTF-8")
os.write(content)
os.flush()
os.close()

responseCode= con.getResponseCode();
errorgroup=str(con.getURL())
errorkey=str(responseCode)

con.disconnect()