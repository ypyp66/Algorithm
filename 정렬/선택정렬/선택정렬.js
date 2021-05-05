const array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

for (let i = 0; i < array.length; i++) {
  let min_index = i;
  for (let j = i + 1; j < array.length; j++) {
    if (array[min_index] > array[j]) {
      min_index = j; //전체 비교를 한 번 할때마다 최솟값인덱스를 저장해줌
    }
  }
  let temp = array[min_index];
  array[min_index] = array[i];
  array[i] = temp;
}

console.log(array);
