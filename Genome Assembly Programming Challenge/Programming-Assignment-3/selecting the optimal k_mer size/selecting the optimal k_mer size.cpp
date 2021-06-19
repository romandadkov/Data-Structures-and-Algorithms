#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <vector>

using vlist_t = std::vector<std::string>;
using sset_t = std::set<std::string>;
using graph_t = std::map<std::string, sset_t>;
using vstack_t = std::stack<std::string>;
constexpr int kmer = 100;

enum class result
{
    no_cycle,
    one_cycle,
    multiple_cycles
};

vlist_t read_input()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    vlist_t reads;
    std::string s;

    while (std::cin >> s)
    {
        reads.emplace_back(std::move(s));
    }

    return reads;
}

result check_ecycle(const graph_t graph)
{
    for (auto &k : graph)
    {
        if (k.second.empty())
        {
            return result::no_cycle;
        }

        if (k.second.size() > 1)
        {
            return result::multiple_cycles;
        }
    }

    return result::one_cycle;
}

graph_t debruijn_graph(const vlist_t &reads, const int k)
{
    graph_t graph;

    for (const auto &read : reads)
    {
        for (size_t i = 0; i + k < read.size(); ++i)
        {
            graph[read.substr(i, k - 1)].emplace(read.substr(i + 2, k - 1));
            if (i + k + 1 < read.size())
            {
                graph[read.substr(i + 2, k - 1)];
            }
        }
    }

    return graph;
}

int bskmer(const vlist_t reads, int left, int right)
{
    while (right >= left)
    {
        const int mid = left + (right - left) / 2;

        result res = check_ecycle(debruijn_graph(reads, mid));
        switch (res)
        {
        case result::one_cycle:
            return mid;
        case result::no_cycle:
            right = mid - 1;
            continue;
        case result::multiple_cycles:
            left = mid + 1;
            continue;
        }
    }
}

int main()
{
    const auto reads = read_input();
    std::cout << bskmer(reads, 0, kmer) << std::endl;

    return 0;
}
