# Dan Programming Language

Dan is an esoteric programming language designed for simplicity and fun. It operates on a single memory tape, similar to Brainfuck, and uses a minimal set of commands to perform operations.

## Commands

- `>` : Move the memory pointer to the right.
- `<` : Move the memory pointer to the left.
- `+` : Increment the value at the memory pointer.
- `-` : Decrement the value at the memory pointer.
- `.` : Output the value at the memory pointer as a character.
- `,` : Input a character and store it at the memory pointer.
- `[` : Jump to the matching `]` if the value at the memory pointer is zero.
- `]` : Jump back to the matching `[` if the value at the memory pointer is non-zero.

## Example Program

Here is an example program that prints "Hello, World!" in Dan:

```
++++++++[>++++++++<-]>.<+++++[>----<-]>-.+++++++.--------.
```

## Interpreter

An interpreter for Dan is provided below in Python.
