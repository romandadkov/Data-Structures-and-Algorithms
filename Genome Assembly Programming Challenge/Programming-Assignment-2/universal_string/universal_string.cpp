#include <algorithm>
#include <bitset>
#include <cmath>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <vector>

using vlist_t = std::vector<std::string>;
using graph_t = std::map<std::string, std::set<std::string>>;
using vstack_t = std::stack<std::string>;

vlist_t eulerian_cycle(graph_t graph)
{
  vstack_t verteces;
  vlist_t path;
  verteces.push(graph.begin()->first);

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
      verteces.push(*graph[current].begin());
      graph[current].erase(graph[current].begin());
    }
  }

  std::reverse(path.begin(), path.end());
  path.pop_back();

  return path;
}

graph_t debruijn_graph(const int k, const int n)
{
  graph_t graph;

  for (size_t i = 0; i < n; ++i)
  {
    auto s1 = std::bitset<16>{i}.to_string().substr(16 - k, k - 1);
    auto s2 = std::bitset<16>{i * 2 % n}.to_string().substr(16 - k);
    auto s3 = std::bitset<16>{i * 2 % n + 1}.to_string().substr(16 - k);

    graph[s1].emplace(s2.substr(0, k - 1));
    graph[s1].emplace(s3.substr(0, k - 1));
  }

  return graph;
}

void print_universal_string(const vlist_t &cycle, const int k)
{
  auto get_substr = [amendment = (k - 2)](const std::string &s) { return s.substr(0, s.size() - amendment); };
  for (const auto &s : cycle)
  {
    std::cout << get_substr(s);
  }
  std::cout << std::endl;
}

int main()
{
  int k;
  std::cin >> k;
  int n = pow(2, k);

  const auto cycle = eulerian_cycle(debruijn_graph(k, n));
  print_universal_string(cycle, k);

  return 0;
}