const array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

for (let i = 0; i < array.length; i++) {
  for (let j = i + 1; j < array.length; j++) {
    if (array[i] > array[j]) {
      let swap = array[i];
      array[i] = array[j];
      array[j] = swap;
    }
  }
}

console.log(array);
