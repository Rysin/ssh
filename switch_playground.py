from ssh_utils import ssh_command, append_data, get_time_stamp, ssh_connect


def run_switch_commands(list_commands: list[str], sss_client: object) -> dict:
    result_dict = {command: ssh_command(sss_client, command) for command in list_commands}

    with open(f'switch_output_{get_time_stamp()}.txt', 'w+') as file:
        for k, v in result_dict.items():
            file.write('#~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #')
            file.write('\n')
            file.write(f'COMMAND : {k}\n Output:\n{v}')
            file.write('\n')
            file.write('#~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #~ #')

    return result_dict


if __name__ == '__main__':
    commands = ['show vlan', 'hostname', 'show running-config', 'show mac address-table', 'show interfaces',
                'show cdp', 'show interfaces status']

    switch_object = ssh_connect(port=22, ip='10.255.43.175', username='arista', password='arista')
    run_switch_commands(commands, switch_object)
