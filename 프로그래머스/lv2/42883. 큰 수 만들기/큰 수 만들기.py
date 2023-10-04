def solution(number, k):
    stack = []

    for digit in number:
        # 스택에 요소가 있고, 스택의 맨 위 요소가 현재 digit보다 작고, 아직 제거해야 할 숫자가 남아있다면
        while stack and stack[-1] < digit and k > 0:
            stack.pop()  # 스택의 맨 위 요소를 제거하고 k를 1 감소
            k -= 1
        stack.append(digit)

    # 만약 k개의 숫자를 제거하지 못한 경우, 뒤에서부터 남은 k개를 제거
    stack = stack[:-k] if k > 0 else stack

    answer = ''.join(stack)
    return answer

# 예제 테스트
number = "1924"
k = 2
result = solution(number, k)
print(result)  # 출력: "94"