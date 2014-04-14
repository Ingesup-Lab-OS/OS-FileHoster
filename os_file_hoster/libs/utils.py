from django.conf import settings
import keystoneclient.v2_0.client as ksclient
from swiftclient import client as swiftclient

class KeystoneHelper:
    USER          = settings.KEYSTONE_USER
    PASS          = settings.KEYSTONE_PASS
    TENANT_NAME   = settings.KEYSTONE_TENANT
    KEYSTONE_URL  = settings.KEYSTONE_URL
    USERS_TENANT = settings.USERS_TENANT

    def get_ksadmin(self):
        ksadmin = ksclient.Client(
            username=self.USER,
            password=self.PASS,
            tenant_name=self.TENANT_NAME,
            auth_url=self.KEYSTONE_URL,
         )
        return ksadmin
    def get_ksadmin_fom_token_id(self, token_id):
        client = ksclient.Client(
            endpoint=self.KEYSTONE_URL,
            token=token_id,
        )
        return client

    def get_ksadmin_from_credentials(self, username, password):
        ksadmin = ksclient.Client(
            username=username,
            password=password,
            tenant_name=self.TENANT_NAME,
            auth_url=self.KEYSTONE_URL,
         )
        return ksadmin

    def create_ksuser(self, ksclient, username, password, email):
        ksclient.users.create(
            name=username,
            password=password,
            email=email,
            tenant_id="6ca0f39be8bc4b208abb4dbd1f9eb1e2",
            enabled=True,
        )

    def delete_ksuser(self, username, password, email, tenant):
        ksadmin.users.delete(user)

class SwiftHelper:
    USER          = settings.KEYSTONE_USER
    PASS          = settings.KEYSTONE_PASS
    TENANT_NAME   = settings.KEYSTONE_TENANT
    SWIFT_URL  = settings.SWIFT_URL
    KEYSTONE_URL  = settings.KEYSTONE_URL

    def put_file(self, auth_token, container, name, fileContent):
        args = (settings.SWIFT_URL, auth_token, container, name, fileContent)
        value = swiftclient.put_object(*args)
