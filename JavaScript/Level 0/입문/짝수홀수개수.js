// https://school.programmers.co.kr/learn/courses/30/lessons/120824

function solution(num_list) {
  var answer = [0, 0];
  for (n of num_list) {
      if (n % 2 == 0) {
          answer[0]++;
      } else {
          answer[1]++;
      }
  }
  return answer;
}