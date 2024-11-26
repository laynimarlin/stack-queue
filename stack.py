stack = []
history = []
def push(elemen):
    stack.append(elemen)
    history.append(stack[:])
def pop():
    if stack:
        history.append(stack[:])
        return stack.pop()
    else:
        return None
def undo():
    if len(history) > 1:
        history.pop()
        stack.clear()
        stack.extend(history[-1])
    else:
        stack.clear()
def redo():
    if len(history) > 1 and len(stack) == 0:
        stack.extend(history[-1])
push(10)
push(20)
push(30)
print ("stack setelah push:", stack)
elemen = pop()
print ("elemen yang di pop pertama:", elemen)
print ("stack setelah pop pertama:", stack)
elemen = pop()
print ("elemen yang di pop kedua:", elemen)
print ("stack setelah pop kedua:", stack)
undo()
print ("stack setelah undo:", stack)
redo()
print ("stack setelah redo:", stack)
if stack:
    print ("elemen teratas:", stack[-1])
else:
    print ("stack kosong")
