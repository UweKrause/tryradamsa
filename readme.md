# tryradamsa

Try
[pyradamsa](https://github.com/tsundokul/pyradamsa),
the python interface to
[libradamsa](https://github.com/andreafioraldi/libradamsa),
the precompiled
[radamsa](https://gitlab.com/akihe/radamsa)
library.

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

