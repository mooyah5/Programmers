function solution(my_str, n) {
  var answer = [];
  let i = 0;
  let tmpN = 1;
  let tmpS = "";
  while (i < my_str.length) {
      tmpS += my_str[i];
      if (tmpN == n) {        // n개 도달마다 문자열 추가 후 tmpS 초기화
          tmpN = 0;
          answer.push(tmpS)
          tmpS = "";
      }
      i++;
      tmpN++;
  };
  // 남은 문자도 추가
  if (tmpS.length > 0) {
      answer.push(tmpS);
  };
  return answer;
}