from ssh_utils import ssh_command, append_data, get_time_stamp
import pytest
import os


@pytest.mark.cli
def test_ssh_command_disk(ssh_client):
    filename = os.path.normpath('Tests/ssh_disk_logs.txt')
    disk_stats = ssh_command(ssh_client_object=ssh_client, command='df /dev/sda1 -h | grep /dev/sda1')
    disk_stats = disk_stats.split(" ")
    used_disk_percent = float(disk_stats[-2].strip('%'))
    print(f'used_disk : {used_disk_percent}')

    # data logging
    t_stamp = get_time_stamp()
    log_string = f'{t_stamp} : {used_disk_percent}%'
    append_data(filename=filename, line=log_string)

    assert used_disk_percent < 90.00
