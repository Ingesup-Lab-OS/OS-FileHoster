import keystoneclient.v2_0.client as ksclient

class KeystoneHelper:
    def getKsadmin(self):
        USER          = "admin"
        PASS          = "pass"
        TENANT_NAME   = "admin"
        KEYSTONE_URL  = 'http://127.0.0.1:35357/v2.0'


        ksadmin = ksclient.Client(  
                                    username=USER,
                                    password=PASS,
                                    tenant_name=TENANT_NAME,
                                    auth_url=KEYSTONE_URL,
                                 )
        return ksadmin

    def createKsuser(self, username, password, email, tenant):
        ksadmin.users.create(   
                                username=username,
                                password=password,
                                email=email, 
                                tenant_id=tenant.id,
                            )

    def createKsuser(self, username, password, email, tenant):
        ksadmin.users.delete(user)