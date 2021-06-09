#include <algorithm>
#include <cstring>
#include <iostream>
#include <map>
#include <random>
#include <set>
#include <vector>

constexpr int mer = 12;
constexpr std::size_t dataset_size = 1618;
constexpr std::size_t read_size = 1000;
constexpr std::size_t max_error_count = 2;

int calculate_overlap(const std::string &a, const std::string &b) noexcept
{
  for (int i = 0, n = 1 + a.size() - mer; i < n; ++i)
  {
    std::size_t errors = 0;
    for (int j = 0, s = a.size() - i; j < s && errors <= max_error_count; ++j)
    {
      if (a[i + j] != b[j])
      {
        ++errors;
      }
    }

    if (errors <= max_error_count)
    {
      return a.size() - i;
    }
  }

  return 0;
}

char get_most_frq(const std::vector<char> chars)
{
  std::map<char, int> counts;
  for (auto c : chars)
  {
    ++counts[c];
  }

  std::pair<char, int> most_frq = *counts.begin();
  for (auto each : counts)
  {
    if (each.second > most_frq.second)
    {
      most_frq = each;
    }
  }

  return most_frq.first;
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
    std::vector<int> overlaps;
    std::vector<int> positions;

    for (int j = 0; j < reads.size(); ++j)
    {
      int overlap = calculate_overlap(cur_read, reads[j]);
      if (overlaps.empty() || overlap >= overlaps.back())
      {
        overlaps.push_back(overlap);
        positions.push_back(j);
        idx = j;
      }
    }

    const auto os = overlaps.size();
    const auto ps = positions.size();
    if (os > 3)
    {
      char *suffix = &g[g.size() - overlaps[os - 4]];
      char *prefix1 = &reads[positions[ps - 4]][0];
      char *prefix2 = &reads[positions[ps - 3]][(overlaps[os - 3] - overlaps[os - 4])];
      char *prefix3 = &reads[positions[ps - 2]][(overlaps[os - 2] - overlaps[os - 4])];
      char *prefix4 = &reads[positions[ps - 1]][(overlaps[os - 1] - overlaps[os - 4])];

      for (int i = 0, n = overlaps[os - 4]; i < n; ++i,
               ++suffix, ++prefix1, ++prefix2, ++prefix3, ++prefix4)
      {
        if (*suffix == *prefix1 &&
            *prefix1 == *prefix2 &&
            *prefix2 == *prefix3 &&
            *prefix3 == *prefix4)
        {
          continue;
        }

        const char c = get_most_frq({*suffix, *prefix1, *prefix2, *prefix3, *prefix4});
        *suffix = *prefix1 = *prefix2 = *prefix3 = *prefix4 = c;
      }
    }

    g += reads[idx].substr(overlaps.back());
  }

  g.erase(0, calculate_overlap(reads[0], f));
  return g;
}

int main()
{
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);

  std::vector<std::string> reads;
  reads.reserve(dataset_size);
  std::string s;

  while (std::cin >> s)
  {
    reads.emplace_back(std::move(s));
  }

  std::random_device rd;
  std::mt19937 g(rd());
  std::shuffle(reads.begin(), reads.end(), g);

  std::cout << assemble_genome(std::move(reads)) << std::endl;

  return 0;
}