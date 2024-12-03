# tryradamsa

Try [pyradamsa](https://github.com/tsundokul/pyradamsa).

## Goal

Have a working http client that uses radamsa as a base for future http fuzzing projects.

## Architecture

### Server

Simple http echo server.  
Echoes the clients request.

### Client

Http client.  
Todo: Use [pyradamsa](https://github.com/tsundokul/pyradamsa) to create fuzzing payloads.  
ToDo: Compare sent payload with echoed payload. 

