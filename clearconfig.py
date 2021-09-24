from os import environ, remove, path
from time import sleep
from shutil import rmtree

if path.isdir(environ['appdata'] + '/fakesession'):
    rmtree(environ['appdata'] + '/fakesession')
    print("All fakesession configs deleted succesfully!")
    sleep(2)
if path.isdir(environ['appdata'] + '/openlecture'):
    rmtree(environ['appdata'] + '/openlecture')
    print("All openlecture configs deleted succesfully!")
    sleep(2)
else:
    print("Nothing to clear")
    sleep(2)