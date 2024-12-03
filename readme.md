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
Uses [pyradamsa](https://github.com/tsundokul/pyradamsa) to create fuzzing payloads.  
ToDo: Compare sent payload with echoed payload.

# Usage

Currently docker-only (due to hard coded server url in client).  
ToDo: Don't hard code server url.

## Docker

`docker compose up` starts client and server.

`docker compose up --build` rebuilds and starts client and server.  
(Use this after code changed.)

`docker compose up --build --watch` watches code for changes and rebuilds accordingly.  
(Use this when code changes frequently / while developing.)
