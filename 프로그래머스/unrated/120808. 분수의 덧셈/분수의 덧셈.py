def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

def solution(numer1, denom1, numer2, denom2):
    
    # 1. 두 분수의 합 계산
    boonmo = denom1 * denom2
    boonja = numer1 * denom2 + denom1 * numer2

    # 2. 최대공약수 계산
    gcd_value = gcd(boonmo, boonja)
    
    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    return answer