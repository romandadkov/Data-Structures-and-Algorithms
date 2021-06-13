#include <algorithm>
#include <iostream>
#include <map>
#include <stack>
#include <string>
#include <vector>

using vlist_t = std::vector<std::string>;
using graph_t = std::map<std::string, vlist_t>;
using vstack_t = std::stack<std::string>;

void print_cycle(const vlist_t &cycle)
{
  std::cout << cycle.front();
  // count of nucleotides - 1
  const auto size = cycle.size() - 9;
  for (size_t i = 1; i < size; ++i)
  {
    std::cout << cycle.at(i).back();
  }
  std::cout << std::endl;
}

vlist_t eulerian_cycle(graph_t graph)
{
  vstack_t verteces;
  vlist_t path;
  path.reserve(graph.size());
  verteces.push(graph.begin()->first);

  while (not verteces.empty())
  {
    const auto current = verteces.top();
    if (graph[current].empty())
    {
      path.emplace_back(std::move(current));
      verteces.pop();
    }
    else
    {
      verteces.push(std::move(graph[current].back()));
      graph[current].pop_back();
    }
  }

  std::reverse(path.begin(), path.end());

  return path;
}

int main()
{
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);

  std::string s;
  // debruijn graph
  graph_t graph;

  while (std::cin >> s)
  {
    graph[s.substr(0, s.size() - 1)].emplace_back(s.substr(1));
  }

  print_cycle(eulerian_cycle(graph));

  return 0;
}