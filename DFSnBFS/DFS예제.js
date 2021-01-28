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
let visited = [];
let next = [];

const dfs = (graph, v, visited) => {
  visited.push(v);

  for (let i = 0; i < graph[v].length; i++) {
    if (!visited.includes(graph[v][i])) {
      dfs(graph, graph[v][i], visited);
    }
  }

  return visited;
};

console.log(dfs(graph, 1, visited));
