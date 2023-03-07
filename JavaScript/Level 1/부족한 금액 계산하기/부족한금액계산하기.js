function solution(price, money, count) {
  sumOfPrice = (count * price * (count + 1)) / 2
  if (sumOfPrice > money) {
      answer = sumOfPrice - money
  } else {
      answer = 0
  }
  return answer;
}

// 등차수열 A(n) = A(1) + (n-1) * 공비
// 등차수열 합 Sn = n(a(1) + a(n)) // 2
