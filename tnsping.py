import subprocess
import re

# Returns the connection string according to the desired ALIAS.
def tnsping(base):
    try:
        command_string = 'tnsping {b}'.format(b=base)
        proc = subprocess.Popen(command_string, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
        stdout, stderr = proc.communicate()
        dns = str(stdout)
        dns = re.search('\([D].+[\)]{3}', dns).group(0)
        return dns
    except:
        print('BASE NAO ENCONTRADA')
    
    

if __name__ == '__main__':
    print(tnsping('ALIAS'))
