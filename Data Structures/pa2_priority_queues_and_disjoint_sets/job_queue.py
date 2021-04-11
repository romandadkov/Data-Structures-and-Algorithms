# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["started_at", "worker"])

def update_worker_job(worker, job):
    lst = list(worker)
    lst[0] = lst[0] + job
    return tuple(lst)

def assign_jobs(n_workers, jobs):
    result = []
    next_free_time = [0] * n_workers
    workers = list(zip(next_free_time, list(range(n_workers))))
    heapq.heapify(workers)

    for job in jobs:
        next_worker = heapq.heappop(workers)
        result.append(AssignedJob(*next_worker))
        heapq.heappush(workers, update_worker_job(next_worker, job))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
