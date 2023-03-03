// 1. apply() 메소드 사용
//  - 매개변수로 this값과 배열을 받아 함수를 실행함
//  - 이를 통해 Math.min() 정적 함수에 배열을 입력할 수 있다.
function solution(s) {                      // s = "1 2 3 4"
  const nums = s.split(" ").map(Number)     // split으로 공백기준 분리, map(Number)로 숫자로 변환
  const maxN = Math.max.apply(Math, nums);// apply() 메소드
  const minN = Math.min.apply(Math, nums);
  const answer = [minN, maxN];
  return answer.join(" ");
}

// 2. reduce() 메소드 사용
function solution(s) {
  const nums = s.split(" ").map(Number)
  let minN = nums.reduce((a, b) => {
    return Math.min(a, b)
  })
  let maxN = nums.reduce((a, b) => {
    return Math.max(a, b)
  })
  const answer = [minN, maxN];
  return answer.join(" ");
}

// 3. 기본 for loop 사용
function solution(s) {
  const nums = s.split(" ").map(Number)
  let maxTmp = nums[0];
  let minTmp = nums[0];
  for (let i = 1; i < nums.length; i++) {
      if (maxTmp < nums[i]) {
          maxTmp = nums[i]
      } else if (minTmp > nums[i]) {
          minTmp = nums[i]
      }
  }
  const ansList = [minTmp, maxTmp];
  const answer = ansList.join(" ");
  return answer;
}