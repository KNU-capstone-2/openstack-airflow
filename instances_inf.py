import socket
print(socket.gethostbyname(socket.gethostname()))


import openstack
import os
import errno

# 인증 정보 설정
auth = openstack.connect(
    auth_url='http://127.0.0.1/identity',  # 인증 URL
    project_name='demo',  # 프로젝트 이름
    username='admin',  # 사용자 이름
    password='pw2468!',  # 비밀번호
    user_domain_name='Default',  # 사용자 도메인 ID
    project_domain_name='Default',  # 프로젝트 도메인 ID
)

session = auth.session

# 서버 목록 조회
servers = auth.compute.servers()
print(servers)

for server in servers:
    # print(server)
    # 서버 이름, 가용 vCPU, RAM 사용량 출력
    print('Name:', server.name)
    print('Status: ', server.status)
    print('Image: ', server.image)
    print('Flavor: ', server.flavor)
    print('Addresses: ', server.addresses)
    print('Keypair: ', server.key_name)

    # print('')
    # print('vCPUs:', server.vcpus)
    # print('RAM:', server.memory_mb)
