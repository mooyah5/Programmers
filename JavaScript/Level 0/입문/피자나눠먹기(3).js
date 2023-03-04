// https://school.programmers.co.kr/learn/courses/30/lessons/120816

function solution(slice, n) {
  var answer = 0;
  let i = 0;
  while (true) {
      if (slice * i >= n) {
          answer = i
          break;
      } else {
          i++;
      }
  }
  return answer;
}