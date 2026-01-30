# get_next_line

## Description
A project focused on file manipulation and memory management. You must write a function that reads a line from a file descriptor.

## Usage

### Compilation
This project uses a Makefile for compilation. Available rules:

- `make all`: Compile the project
- `make clean`: Remove object files
- `make fclean`: Remove object files and executable/library
- `make re`: Recompile the project

### Running
This project produces a static library `get_next_line.a`.
To use it in your program, compile with:
```bash
gcc your_program.c -L. -lget_next_line -o your_program
```
