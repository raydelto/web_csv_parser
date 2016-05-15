'''
Created on May 15, 2016

@author: raydelto
'''

import bottle

@bottle.route('/')
def index():
    return bottle.template('index')

def start_server():
    bottle.debug(True)
    bottle.run(host='localhost', port=8082)

if __name__ == '__main__':
    start_server()