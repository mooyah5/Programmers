function solution(x, n) {
  var answer = [];
  state = true
  for (let i = 1; i <= n; i++ ){
      answer.push(x*i)
  }
  return answer;
}