import openstack

# 인증 정보 설정
auth = openstack.connect(
    auth_url='http://127.0.0.1/identity',  # 인증 URL
    project_name='demo',  # 프로젝트 이름
    username='admin',  # 사용자 이름
    password='pw2468!',  # 비밀번호
    user_domain_name='Default',  # 사용자 도메인 ID
    project_domain_name='Default',  # 프로젝트 도메인 ID
)

if auth.authorize:
    print("OpenStack cloud connect success.")
else:
    print("OpenStack cloud connect faild.")

def list_servers(conn):
    print("List Servers:")

    for server in conn.compute.servers():
        print(server)


def list_images(conn):
    print("List Images:")

    for image in conn.compute.images():
        print(image)


def list_flavors(conn):
    print("List Flavors:")

    for flavor in conn.compute.flavors():
        print(flavor)


def list_keypairs(conn):
    print("List Keypairs:")

    for keypair in conn.compute.keypairs():
        print(keypair)

list_servers(auth)
list_images(auth)
list_flavors(auth)
list_keypairs(auth)