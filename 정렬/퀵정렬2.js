const array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

const quick_sort = (array) => {
  let left = [];
  let right = [];

  if (array.length <= 1) {
    return array;
  }

  const pivot = array[0];
  const tail = array.slice(1, array.length); //array[1] ~ array[끝]

  tail.forEach((element) => {
    if (element <= pivot) left.push(element);
  });

  tail.forEach((element) => {
    if (element > pivot) right.push(element);
  });

  return quick_sort(left) + [pivot] + quick_sort(right);
};
console.log(quick_sort(array));
