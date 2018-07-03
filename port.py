import nmap


def port_scanner():
    file_name = input("What is your source file name: ")
    f = open(file_name, 'r')

    if f.mode == 'r':
        contents = f.readlines()
        port_list = []
        for content in contents:
            port_list.append(content.rstrip().split(':'))
    f.close()

    nm = nmap.PortScanner()
    for item in port_list:
        nm.scan(item[0], item[1])
        for host in nm.all_hosts():
            write_to_file('ip : {0}'.format(host))

            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                lport = sorted(lport)
                for port in lport:
                    write_to_file(
                        "port : {0}\tstate : {1}".format(port,
                        nm[host][proto][port]['state']))


def write_to_file(contents):
    file_name = 'port_list.txt'
    try:
        f = open(file_name, 'a+')
        f.write(contents + '\n')

    except IOError:
        f = open(file_name, 'w+')
        f.write(contents + '\n')
    f.close()


def main():
    port_scanner()


if __name__ == "__main__":
    main()
