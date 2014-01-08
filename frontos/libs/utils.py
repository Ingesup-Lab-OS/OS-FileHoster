from django.conf import settings
import keystoneclient.v2_0.client as ksclient

class KeystoneHelper:
    def getKsadmin(self):
        USER          = settings.KEYSTONE_USER
        PASS          = settings.KEYSTONE_PASS
        TENANT_NAME   = settings.KEYSTONE_TENANT
        KEYSTONE_URL  = settings.KEYSTONE_URL


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

    def deleteKsuser(self, username, password, email, tenant):
        ksadmin.users.delete(user)