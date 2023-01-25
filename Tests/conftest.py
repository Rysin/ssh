from ssh_utils import ssh_connect
import pytest

@pytest.fixture
def ssh_client():
    print('Running Fixuture!')
    return ssh_connect(port=3022, ip='127.0.0.1', username='sdesai', password='admincli')


if __name__ == '__main__':
    ssh_client()