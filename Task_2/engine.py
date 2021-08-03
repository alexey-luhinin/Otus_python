'''Engine'''
from dataclasses import dataclass


@dataclass
class Engine:
    '''Engine'''
    is_worked: bool = False

    def start(self):
        '''start'''
        print('start engine')
        self.is_worked = True
        return self.is_worked

    def stop(self):
        '''stop'''
        print('stop engine')
        self.is_worked = False
        return self.is_worked
