# libft

## Description
The first project in the 1337 curriculum. You must recode several functions from the C standard library and create your own library.

## Usage

### Compilation
This project uses a Makefile for compilation. Available rules:

- `make all`: Compile the project
- `make clean`: Remove object files
- `make fclean`: Remove object files and executable/library
- `make re`: Recompile the project
- `make bonus`: Compile with bonus features

### Running
This project produces a static library `libft.a`.
To use it in your program, compile with:
```bash
gcc your_program.c -L. -lft -o your_program
```
