from ssh_utils import ssh_command, append_data, get_time_stamp
import os

def test_ssh_command_memory(ssh_client):
    filename = os.path.normpath('Tests/ssh_memory_logs.txt')
    memory_stat_free = ssh_command(ssh_client_object=ssh_client, command='cat /proc/meminfo | grep MemFree')
    memory_stat_total = ssh_command(ssh_client_object=ssh_client, command='cat /proc/meminfo | grep MemTotal')
    memory_stat_free = int(memory_stat_free.split(" ")[-2])
    memory_stat_total = int(memory_stat_total.split(" ")[-2])

    free_memory_percent = int((memory_stat_free / memory_stat_total) * 100)

    # data logging
    t_stamp = get_time_stamp()
    log_string = f'{t_stamp} : {memory_stat_total}, {memory_stat_free}, {free_memory_percent}%'
    append_data(filename=filename, line=log_string)

    assert free_memory_percent < 80