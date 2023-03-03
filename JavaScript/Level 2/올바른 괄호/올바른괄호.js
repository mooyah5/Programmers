// 2. 효율성 5~6
function solution(s) {
  var answer = true;
  let stack = [];
  for (i of s) {
      if (i == '(') {
          stack.push(i);
      } else if (stack.length < 0 || stack.pop() != '(') {
          return false
      }
  }
  if (stack.length > 0) {
      return false
  } else {
      return true
  }
}

// 3. 효율성 7
function solution(s) {
  let n = 0;
  for (i of s) {
      if (i == "(") {
          n++;
      } else {
          n--;
      }
      if (n < 0) {
          return false;
      }
  }
  if (n == 0) {
      return true
  } else {
      return false
  }
}