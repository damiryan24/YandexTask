input_table = open('pid_table.CSV', 'r')
output_table = open('hex_pid_table.CSV', 'w')

while True:
    old_line = input_table.readline()
    if not old_line:
        break
    if old_line == 'pid\n':
        new_line = 'pid,hex_pid\n'
    else:
        new_line = str(int(old_line)) + ',' + hex(int(old_line)) + '\n'
    output_table.write(new_line)

input_table.close()
output_table.close()