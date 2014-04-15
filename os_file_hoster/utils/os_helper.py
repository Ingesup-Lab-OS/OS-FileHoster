from django.conf import settings
import keystoneclient.v2_0.client as ksclient
from swiftclient import client as swiftclient
from openstack_auth.user import create_user_from_token, Token, User
from openstack_auth.backend import KeystoneBackend

class KeystoneHelper:
    USER          = settings.KEYSTONE_USER
    PASS          = settings.KEYSTONE_PASS
    TENANT_NAME   = settings.KEYSTONE_TENANT
    KEYSTONE_URL  = settings.KEYSTONE_URL
    USERS_TENANT = settings.USERS_TENANT
    ksadmin = None
    client = None

    def get_ksadmin(self, request):
        if not self.client:
            self.client = ksclient.Client(
                username=self.USER,
                password=self.PASS,
                tenant_name=self.TENANT_NAME,
                auth_url=self.KEYSTONE_URL,
             )
        if not 'ksadmin' in request.session or not request.session['ksadmin']:
            ksadmin = self.set_ksadmin(request)
            self.ksadmin = ksadmin
        return self.ksadmin

    def set_ksadmin(self, request):
        backend = KeystoneBackend()
        ksadmin = backend.authenticate(request, self.USER, self.PASS, 'Default', self.KEYSTONE_URL)
        return ksadmin

    def get_ksadmin_fom_token_id(self, token_id):
        return self.client

    def get_ksadmin_from_credentials(self, username, password):
        ksadmin = self.ksadmin.Client(
            username=username,
            password=password,
            tenant_name=self.TENANT_NAME,
            auth_url=self.KEYSTONE_URL,
         )
        return ksadmin

    def create_ksuser(self, username, password, email):
        self.ksadmin.users.create(
            name=username,
            password=password,
            email=email,
            tenant_id="6ca0f39be8bc4b208abb4dbd1f9eb1e2",
            enabled=True,
        )

    def delete_ksuser(self, id):
        self.ksadmin.users.delete(id)

class SwiftHelper:
    USER          = settings.KEYSTONE_USER
    PASS          = settings.KEYSTONE_PASS
    TENANT_NAME   = settings.KEYSTONE_TENANT
    SWIFT_URL  = settings.SWIFT_URL
    KEYSTONE_URL  = settings.KEYSTONE_URL

    def put_file(self, auth_token, container, name, content):
        if not self.container_exists(self.SWIFT_URL, auth_token, container):
            swiftclient.put_container(self.SWIFT_URL, auth_token, container,  {'X-Container-Read' : '.r:*'})
        args = (self.SWIFT_URL, auth_token, container, name, content)
        swiftclient.put_object(*args)

    def container_exists(self, url, auth_token, container):
        try:
            swiftclient.head_container(url, auth_token, container)
        except swiftclient.ClientException:
            return False
        return True

    def gen_url_for_file(self, container, name):
        return "%s/%s/%s" % (self.SWIFT_URL, container, name)

    def get_files(self, auth_token, container):
        if not self.container_exists(self.SWIFT_URL, auth_token, container):
            swiftclient.put_container(self.SWIFT_URL, auth_token, container,  {'X-Container-Read' : '.r:*'})
        return swiftclient.get_container(self.SWIFT_URL, auth_token, container)

    def delete_file(self, auth_token, container, name):
        return swiftclient.delete_object(self.SWIFT_URL, auth_token, container, name)
