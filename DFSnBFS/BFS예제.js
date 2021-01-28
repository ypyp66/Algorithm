const graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7],
];

const bfs = (graph, start) => {
  let visited = []; //return할 배열
  let next = []; //큐

  next.push(start); // 처음 시작 노드를 다음방문할 배열에 넣음

  while (next.length !== 0) {
    //방문할 배열의 길이가 0이 될때까지 반복
    const v = next.shift(); //방문할 배열에서 맨 왼쪽 원소를 꺼냄

    if (!visited.includes(v)) {
      //return할 배열에 원소가 포함되어있지 않다면
      visited.push(v); //원소를 넣어주고
      next = [...next, ...graph[v]]; //다음 방문배열에 해당 노드의 자식노드들을 전부 방문할 배열에 넣어줌
      //spread연산자 사용
    }
  }
  return visited;
};
console.log(bfs(graph, 1));
