import socket

def is_website_online(Host):
    """ This function checks to see if a Host name has a DNS entry by checking
        for socket info. If the website gets something in return, 
        we know it's available to DNS.
    """
    try:
        socket.gethostbyname(Host)
    except socket.gaierror:
        print('\033[1;31mSITE OFFLINE')
    else:
        print('	\033[1;32mSITE ONLINE!')

is_website_online("www.pudim.com.br")