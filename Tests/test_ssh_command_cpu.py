import os
from ssh_utils import ssh_command, append_data, get_time_stamp

import logging

# log_filename = os.path.normpath('logs/ssh_cpu.log')
log_filename = os.path.join('logs', 'ssh_cpu.log')

logging.basicConfig(filename=log_filename,
                    format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger()


# logger.debug("This is a debug log")
# logger.info("This is an info log")
# logger.critical("This is critical")
# logger.error("An error occurred")


def test_ssh_command_cpu(ssh_client):
    logger.debug("Started SSH_CPU Test")
    command = 'mpstat | grep all'
    logger.debug(f"Executing command : {command}")
    filename = os.path.normpath('Tests/Testsssh_cpu_logs.txt')
    logger.debug(f"Storing CPU stats in : {filename}")
    cpu_stats_raw = ssh_command(ssh_client_object=ssh_client, command=command)
    cpu_stats_raw = cpu_stats_raw.split(" ")
    float(cpu_stats_raw[-1].strip('\n'))
    available_cpu_percent = float(cpu_stats_raw[-1])
    # print(f'available_cpu : {available_cpu_percent}')

    # data logging
    t_stamp = get_time_stamp()
    log_string = f'{t_stamp} : {available_cpu_percent}%'
    append_data(filename=filename, line=log_string)
    logger.debug(f'Appended datat : {log_string} to file {filename} ')
    assert available_cpu_percent > 90.00
