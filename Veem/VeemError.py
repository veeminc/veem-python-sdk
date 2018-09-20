'''
Created on Aug 20, 2018

@author: dhars
'''

import json

class VeemError(BaseException):
    '''
    classdocs
    '''

    
    def __init__(self, response):
        '''
        Constructor
        '''

        try:
            error=response.json()
            self.code=error['code']
            self.message=error['message']
        except Exception:
            self.message=response
        
