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



def create_keypair(conn, keypair_name):
    keypair = conn.compute.find_keypair(keypair_name)

    if not keypair:
        print("Create Key Pair:")

        keypair = conn.compute.create_keypair(name=keypair_name)

        print(keypair)

        try:
            os.mkdir("./ssh_dir")
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise e
        
        PRIVATE_KEYPAIR_FILE = './ssh_dir/id_rsa.{key}'.format(key=keypair_name)
        with open(PRIVATE_KEYPAIR_FILE, 'w') as f:
            f.write("%s" % keypair.private_key)

        os.chmod(PRIVATE_KEYPAIR_FILE, 0o400)

    return keypair

create_keypair(auth, "test123")