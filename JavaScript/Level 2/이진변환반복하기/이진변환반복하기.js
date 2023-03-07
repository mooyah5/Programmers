function solution(S) {
  var answer = [0, 0];    // 0항은 없앤 횟수, 1항은 없앤 0의 개수
  function binary(S) {
      // 1이 되면 리턴
      if(S === '1') {
          return answer
      }
      S = S.split('');    // 한글자씩 배열의 요소로 변환
      let tmp = S.filter(v => v === '0').length;  // 각 요소가 0인 것의 개수만 셈.
      answer[0] += 1;     // 없앤 횟수 + 1
      answer[1] += tmp;   // 없앤 0의 개수
      S = (S.length-tmp).toString(2);     // 2진수로 변환
      return binary(S)
  }
  binary(S);
  return answer;
}