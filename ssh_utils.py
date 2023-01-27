import paramiko
from datetime import datetime


def get_time_stamp() -> str:
    timestamp = datetime.timestamp(datetime.now())
    date_time = datetime.fromtimestamp(timestamp)
    return date_time.strftime("%d_%m_%Y-%H_%M_%S")


def ssh_command(ssh_client_object: object, command: str) -> str:
    ssh_client_object.invoke_shell()
    stdin, stdout, stderr = ssh_client_object.exec_command(command)
    return stdout.read().decode()


def ssh_connect(port: int, ip: str, username: str, password: str) -> object:
    try:
        ssh_cl = paramiko.SSHClient()
        ssh_cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_cl.connect(port=port, hostname=ip, username=username, password=password)
    except Exception as e:
        print(f'Connection Failed due to error :\n{e}')
        ssh_cl = None

    return ssh_cl


def append_data(filename: str, line: str) -> None:
    try:
        with open(filename, 'a+') as file:
            file.write(f'{line}\n')
    except Exception as e:
        print(f'Failed to create logger file due to error :\n{e}')


if __name__ == '__main__':
    # print(get_time_stamp())
    for i in range(10):
        append_data(filename='data.txt', line=i)
