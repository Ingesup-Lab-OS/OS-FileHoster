import keystoneclient.v2_0.client as ksclient

def getAdminKeystone():
  USER          = "admin"
  PASS          = "pass"
  TENANT_NAME   = "demo"
  KEYSTONE_URL  = 'http://localhost:35357/v2.0'


  ksadmin = ksclient.Client(username=USER,
                            password=PASS,
                            tenant_name=TENANT_NAME,
                            auth_url=KEYSTONE_URL)