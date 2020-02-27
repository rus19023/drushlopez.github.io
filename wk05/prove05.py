class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def prompt_filename():
    ''' Get file name '''
    file_name = input("Please enter the data file: ")
    '''file_name = "d:\\hello\\wk05\\stacks06.txt"'''
    return file_name


def open_reader(filename):
    ''' Open the file '''
    with open(filename, "r", encoding="utf-8", newline='') as readfile:
        reader = readfile.readlines()
        return reader


def parse_file(reader):
    ''' set up variables for stack and characters '''
    stack1 = Stack()
    match = {"[": "]", "(": ")", "{": "}"}
    result = ""
    word_count = 0
    ''' Read through file character by character '''
    for line in reader:
        line = line.strip()
        for word in line:
            word_count += 1
            if word in "[({":
                ''' If current char is opener, push it onto stack '''
                stack1.push(word)
            else:
                if stack1.size() == 0:
                    ''' if open stack is empty, it's not balanced '''
                    result = "stack empty, Not balanced"
                    break
                compare_with = word
                last_in = match[stack1.peek()]
                if last_in == compare_with:
                    '''if current char is closer, compare to top of stack'''
                    '''if opener/closer match, pop item off stack'''
                    stack1.pop()
                    result = "matched, Balanced"
                else:
                    result = "not matched, Not balanced"
                    break
            if word_count == 1 or word_count % 2 > 0:
                result = "Not balanced"
                break
    return result


def main():
    filename1 = prompt_filename()
    read_file1 = open_reader(filename1)
    print(parse_file(read_file1))


if __name__ == "__main__":
    main()
