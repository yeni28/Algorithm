function solution(numbers) {
    const sum = numbers.reduce((prev,cur) => prev + cur, 0)
    const size = numbers.length
    answer = sum / size
    return answer
}