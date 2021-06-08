#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>

constexpr int mer = 12;
constexpr std::size_t dataset_size = 1618;
constexpr std::size_t read_size = 1000;

int calculate_overlap(const std::string &a, const std::string &b) noexcept
{
  for (int i = 0, n = 1 + a.size() - mer; i < n; ++i)
  {
    if (strncmp(b.c_str(), a.c_str() + i, a.size() - i) == 0)
    {
      return a.size() - i;
    }
  }
  return 0;
}

std::string pop_front(std::vector<std::string> &v, const std::size_t count)
{
  const std::string c = std::move(v[count]);
  v.erase(v.begin() + count);
  return c;
}

std::string assemble_genome(std::vector<std::string> reads) noexcept
{
  std::string g;
  g.reserve(read_size);
  g += reads.front();

  const auto f = reads.front();

  for (std::size_t idx = 0; reads.size() > 1;)
  {
    const auto cur_read = pop_front(reads, idx);

    auto result = std::max_element(reads.begin(), reads.end(),
                                   [cur_read](const std::string &a, const std::string &b) {
                                     return calculate_overlap(cur_read, a) < calculate_overlap(cur_read, b);
                                   });

    idx = std::distance(reads.begin(), result);
    const auto overlap = calculate_overlap(cur_read, reads.at(idx));
    g += reads[idx].substr(overlap);
  }

  g.erase(0, calculate_overlap(reads.at(0), f));

  return g;
}

int main()
{

  std::vector<std::string> reads;
  reads.reserve(dataset_size);
  std::string s;

  std::cin.tie(NULL);
  std::ios::sync_with_stdio(false);
  while (std::cin >> s)
  {
    if (reads.back() != s)
    {
      reads.emplace_back(std::move(s));
    }
  }

  std::cout << assemble_genome(std::move(reads)) << std::endl;

  return 0;
}