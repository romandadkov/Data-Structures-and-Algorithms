#include <algorithm>
#include <cassert>
#include <iostream>
#include <stack>
#include <vector>

using vlist_t = std::vector<int>;
using graph_t = std::vector<vlist_t>;
using vstack_t = std::stack<int>;

void read_edge(int &from, int &to)
{
  std::cin >> from >> to;
  --from;
  --to;
}

void print_cycle(const vlist_t &cycle)
{
  std::cout << 1 << '\n';
  for (auto v : cycle)
  {
    std::cout << v + 1 << ' ';
  }
  std::cout << std::endl;
}

vlist_t eulerian_cycle(graph_t graph)
{
  vstack_t verteces;
  vlist_t path;
  verteces.push(0);

  while (not verteces.empty())
  {
    const auto current = verteces.top();
    if (graph[current].empty())
    {
      path.push_back(current);
      verteces.pop();
    }
    else
    {
      verteces.push(graph[current].back());
      graph[current].pop_back();
    }
  }

  std::reverse(path.begin(), path.end());
  path.pop_back();

  return path;
}

int main()
{
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);

  int num_verteces;
  int num_edges;

  std::cin >> num_verteces >> num_edges;

  graph_t graph(num_verteces);
  vlist_t in(num_verteces);
  vlist_t out(num_verteces);

  for (int i = 0, from = 0, to = 0; i < num_edges; ++i)
  {
    read_edge(from, to);
    graph[from].push_back(to);
    in[to] += 1;
    out[from] += 1;
  }

  assert(in.size() == out.size());
  if (in == out)
  {
    const auto cycle = eulerian_cycle(std::move(graph));
    print_cycle(cycle);
  }
  else
  {
    std::cout << 0 << std::endl;
  }

  return 0;
}
