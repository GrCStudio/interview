class Stack:

    def __init__(self,):
        self.list = []

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def push(self,push_param):
        self.list.append(push_param)

    def pop(self):
        if len(self.list) > 0:
            last_elem = self.list[-1]
            self.list.pop()
            return last_elem

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)


def stack_processing(inp_str):
    #Блок первоначальных проверок, чтобы не делать лишних вычислений, если не проходит, сразу возвращаем отрицательный ответ.
    if len(inp_str) % 2 != 0:
        return "Несбалансированно"
    if inp_str[0] in closer:
        return "Несбалансированно"

    '''Создаем объект стэка. Делаем из строки список и проводим итерацию по элементам списка.
    Если элемент списка в открывающих, помещаем его в стэк. Если в закрывающих, 
    то возвращаем последний из стека. Если он не соответствует возвращенному, то несбалансированно.
    Иначе продолжаем.
    '''
    foolist = list(inp_str)
    stack_obj = Stack()
    for elem in foolist:
        if elem in opener:
            stack_obj.push(elem)
            #print('Добавлено ', elem)
        if elem in closer:
            last_stack = stack_obj.pop()
            if last_stack  == '[':
                if elem == ']':
                    #print('Обнулено []')
                    continue
            elif last_stack == '(':
                if elem == ')':
                    #print('Обнулено ()')
                    continue
            elif last_stack == '{':
                if elem == '}':
                    #print('Обнулено {}')
                    continue
            return "Несбалансированно"
    if stack_obj.isEmpty():
        return "Сбалансированно"
    return "Несбалансированно"


data = ("(((([{}]))))","[([])((([[[]]])))]{()}","{{[()]}}","}{}","{{[(])]}}","[[{())}]")
opener = ('{','[','(')
closer = ('}',']',')')

for element in data:
    print(stack_processing(element))