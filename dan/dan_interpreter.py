class DanInterpreter:
    def __init__(self, code):
        self.code = code
        self.memory = [0] * 30000
        self.pointer = 0
        self.code_pointer = 0
        self.bracket_map = self.build_bracket_map()

    def build_bracket_map(self):
        stack = []
        bracket_map = {}
        for pos, char in enumerate(self.code):
            if char == '[':
                stack.append(pos)
            elif char == ']':
                start = stack.pop()
                bracket_map[start] = pos
                bracket_map[pos] = start
        return bracket_map

    def run(self):
        while self.code_pointer < len(self.code):
            command = self.code[self.code_pointer]

            if command == '>':
                self.pointer += 1
            elif command == '<':
                self.pointer -= 1
            elif command == '+':
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
            elif command == '-':
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
            elif command == '.':
                print(chr(self.memory[self.pointer]), end='')
            elif command == ',':
                self.memory[self.pointer] = ord(input()[0])
            elif command == '[' and self.memory[self.pointer] == 0:
                self.code_pointer = self.bracket_map[self.code_pointer]
            elif command == ']' and self.memory[self.pointer] != 0:
                self.code_pointer = self.bracket_map[self.code_pointer]

            self.code_pointer += 1

if __name__ == "__main__":
    code = "++++++++[>++++++++<-]>.<+++++[>----<-]>-.+++++++.--------."
    interpreter = DanInterpreter(code)
    interpreter.run()
