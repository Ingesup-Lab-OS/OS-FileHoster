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

    def __init__(self):
        self._ksclient = ksclient.Client(
            username=self.USER,
            password=self.PASS,
            tenant_name=self.TENANT_NAME,
            auth_url=self.KEYSTONE_URL)

    def get_ksclient(self):
        return self._ksclient

    def create_ksuser(self, username, password, email):
        self._ksclient.users.create(
            name=username,
            password=password,
            email=email,
            tenant_id="6ca0f39be8bc4b208abb4dbd1f9eb1e2",
            enabled=True)

    def delete_ksuser(self, id):
        self._ksclient.users.delete(id)

class SwiftHelper():
    USER          = settings.KEYSTONE_USER
    PASS          = settings.KEYSTONE_PASS
    TENANT_NAME   = settings.KEYSTONE_TENANT
    SWIFT_URL  = settings.SWIFT_URL
    KEYSTONE_URL  = settings.KEYSTONE_URL

    def __init__(self):
        self._connection = swiftclient.Connection(
        authurl=self.KEYSTONE_URL,
        auth_version=2,
        user=self.USER,
        key=self.PASS,
        tenant_name="filehoster_users")

    def put_file(self, container, name, content):
        if not self.container_exists(container):
            self._connection.put_container(container,  {'X-Container-Read' : '.r:*'})
        self._connection.put_object(container, name, content)

    def container_exists(self, container):
        try:
            self._connection.head_container(container)
        except swiftclient.ClientException:
            return False
        return True

    def gen_url_for_file(self, container, name):
        return "%s/%s/%s" % (self.SWIFT_URL, container, name)

    def get_files(self, container):
        if not self.container_exists(container):
            self._connection.put_container(container,  {'X-Container-Read' : '.r:*'})
        return self._connection.get_container(container)

    def delete_file(self, container, name):
        return self.connection.delete_object(container, name)
