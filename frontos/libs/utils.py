from django.conf import settings
import keystoneclient.v2_0.client as ksclient
from swiftclient import client as swiftclient

class KeystoneHelper:
    USER          = settings.KEYSTONE_USER
    PASS          = settings.KEYSTONE_PASS
    TENANT_NAME   = settings.KEYSTONE_TENANT
    KEYSTONE_URL  = settings.KEYSTONE_URL

    def getKsadmin(self):
        ksadmin = ksclient.Client(
            username=self.USER,
            password=self.PASS,
            tenant_name=self.TENANT_NAME,
            auth_url=self.KEYSTONE_URL,
         )
        return ksadmin

    def getKsadminFromCredentials(self, username, password):
        ksadmin = ksclient.Client(
            username=username,
            password=password,
            tenant_name=self.TENANT_NAME,
            auth_url=self.KEYSTONE_URL,
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

class SwiftHelper:
    USER          = settings.KEYSTONE_USER
    PASS          = settings.KEYSTONE_PASS
    TENANT_NAME   = settings.KEYSTONE_TENANT
    KEYSTONE_URL  = settings.KEYSTONE_URL

    def putFile(self, auth_token, container, name, fileContent):
        args = ('http://www.test.com', auth_content, container, name, fileContent)
        value = swiftclient.put_object(*args)
