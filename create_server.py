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

# 인스턴스 생성에 필요한 정보 설정
server_name = 'test'  # 인스턴스 이름
image_name = 'cirros-0.5.2-x86_64-disk'  # 사용할 이미지 이름
flavor_name = 'm1.micro'  # 사용할 플레이버(flavor) 이름
network_name = 'private'  # 사용할 네트워크 이름
keypair_name = 'test'  # 사용할 키페어 이름

# 이미지, 플레이버, 네트워크, 키페어 가져오기
image = auth.compute.find_image(image_name)
print("\nimage\n")
print(image)
flavor = auth.compute.find_flavor(flavor_name)
print("\nflaver\n")
print(flavor)
network = auth.network.find_network(network_name)
print("\nnetwork\n")
print(network)
keypair = auth.compute.find_keypair(keypair_name)
print("\nkeypair\n")
print(keypair)

# 서버 생성
server = auth.compute.create_server(
        name=server_name, image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}], key_name=keypair.name)

server = auth.compute.wait_for_server(server)


print("\nserver\n")
print(server)

print("ssh -i {key} root@{ip}".format(
        key=keypair.name,
        ip=server.access_ipv4))

# # 서버 정보 출력
# print("Server ID: ", server.id)
# print("Server Name: ", server.name)
# print("Server Status: ", server.status)
# print("Server IP Address: ", server['addresses'][network_name][1]['addr'])
