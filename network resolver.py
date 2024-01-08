import re, time, os
from turtle import clear


class IPV4():

    def __init__(self, ip='', prefix='', mask='', network ='', broadcast = '', number = '' ):
        self.ip = ip
        self.prefix = prefix 
        self.mask = mask
        self.network = network
        self.broadcast = broadcast
        self.number = number


        self.regex()
    
        self.ip_numbers()

        self.network_and_broadcast()

        self.prefix_mask()

        self.mask_prefix()
    

    def prefix_mask(self):
        binary_mask = ''

        for x in range(32):
            if x < int(self.prefix):
                binary_mask += '1'
            else:
                binary_mask += '0'

        print('\033[1;91mMáscara da rede: \033[m')
        self.decimal_mask =  self.binary_for_decimal(binary_mask)
        self.mask = self.decimal_mask
        self.binary_mask = binary_mask

    def network_and_broadcast(self):
        self.binary_ip = self.decimal_for_binary(self.ip)
        self.binary_ip = self.binary_ip.replace('.', '')
        self.binary_mask = self.decimal_for_binary(self.mask)
        self.binary_mask = self.binary_mask.replace('.', '')
    
        network = ''
        broadcast = ''

        for x, bit in enumerate(self.binary_ip):
            if x < int(self.prefix):
                network += str(bit)
                broadcast += str(bit)
            else:
                network += '0'
                broadcast += '1'
        
        
        print("\033[36mEndereço de rede:\033[m")
        self.network = self.binary_for_decimal(network)
        print("\033[33mEndereço de broadcast:\033[m")
        self.broadcast = self.binary_for_decimal(broadcast)
        

    ''' || Calculating number of networks. || '''
    def ip_numbers(self):
        bits = 32-int(self.prefix)
        self.prefix = int(self.prefix)
        self.number = pow(2, bits)
        
        if self.prefix >= 8 and self.prefix < 16:
            self.networks = pow(2, 24-bits)
        elif self.prefix >16 and self.prefix <= 24:
            self.networks = pow(2, 16-bits)
        elif self.prefix > 24 and self.prefix <= 32:
            self.networks = pow(2, 8-bits)
        
        print('\033[36mRedes:\033[m', self.networks)
        print('Hosts:', self.number,'\n\033[32mHosts disponíveis: \033[m',self.number-2)
        

    def mask_prefix(self):
        prefix = 0

        for x in self.binary_mask:
            if x == '1':
                prefix += 1
        
        self.prefix = prefix
        
        if self.prefix >= 8 and self.prefix < 16:
            print("\033[1;92mClasse: A/033[m")
        elif self.prefix >=16 and self.prefix < 24:
            print("\033[1;92mClasse: B\033[m")
        elif self.prefix >= 24 and self.prefix < 32:
            print("\033[1;92mClasse: C\033[m")


    def binary_for_decimal(self, ip=''):
        self.decimal = str(int(ip[0:8], 2))+'.'
        s = 8
        e = 16
        for x in range(0, 3, 1):
            if e == 32:
                self.decimal += str(int(ip[s:e], 2))
            else:
                self.decimal += str(int(ip[s:e], 2))+'.'
                s += 8
                e += 8

        print(self.decimal)
        
    def decimal_for_binary(self, ip=''):
        if not ip:
            ip = self.ip

        octets = ip.split('.')
        binary_ip = []

        for x in octets:
            binary = bin(int(x))

            ''' || [2:] = read from character two onwards. || zfill = eight-character binaries || '''
            binary = binary[2:].zfill(8)
            binary_ip.append(binary)

        ''' || '.'.join = return with dot. '''
        binary_ip = '.'.join(binary_ip)
        return binary_ip

               

    def regex(self):
        ''' || IP and Prefix Regex check || '''
        regex = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/[0-9]{1,2}$')

        if not regex.search(self.ip):
           return

        ''' || split('/') = separating IP from prefix. IP: 0 / Prefix: 1 || '''
        broken = self.ip.split('/')
        self.ip = broken[0]
        self.prefix = broken[1]
    
    

if __name__ == '__main__':
    i = 0
    word = ('\033[35mNetwork Calculator\033[m\n')
    for x in range(0, len(word), 1):
            print(word[x], end='', flush = True)
            time.sleep(0.10)

    while i == 0:
        
        try:
            ipv4 = IPV4(input('\n\033[36mIP and Mask: \n\033[m'))
                
        except:
            print("\033[31mINVALID IP!\033[m")
            print('\033[33mPlease! send in the format: 0-3.0-3.0-3.0-3/0-2\033[33m')
            time.sleep(3)
            os.system('cls')
    