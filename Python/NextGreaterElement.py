def nextGreaterElement(array):
    answer = [-1 for _ in array]
    stack = [0]
    for i in range(1, len(array)):
        while stack and array[stack[-1]] < array[i]:
            curr = stack.pop()
            answer[curr] = array[i]
        stack.append(i)

    for i in range(len(array[:stack[0] + 1])):
        while stack and array[stack[-1]] < array[i]:
            curr = stack.pop()
            answer[curr] = array[i]

    return answer