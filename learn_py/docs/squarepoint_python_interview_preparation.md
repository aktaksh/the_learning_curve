# Platform Compute and Storage: Python Interview Preparation

## Scope

Python-only preparation for a Platform Compute and Storage Specialist interview. Focus: infrastructure automation, Linux and storage data processing, production safety, Python fundamentals, testing, and easy-to-medium coding problems.

For each problem: clarify input, output, scale, and failures; explain approach; code; state complexity; test edge cases; describe production improvements.

## 1. Core Python

Cover:

- Lists, tuples, sets, dictionaries, hashing, and complexity
- Mutable versus immutable objects
- `is` versus `==`
- Shallow versus deep copy
- Mutable default arguments
- Comprehensions, sorting, exceptions, type hints, and dataclasses

Questions: Why must dictionary keys be hashable? Why is lookup usually `O(1)`? What is wrong with `def add(host, hosts=[])`? When should a tuple replace a list?

## 2. Iterators, Generators, Decorators, Context Managers

Cover:

- Iterable versus iterator; `iter()`, `next()`, `StopIteration`
- Generator functions, `yield`, lazy evaluation, and memory use
- Decorators, `*args`, `**kwargs`, and `functools.wraps`
- Context managers and `with`

Questions: How would you process a 100 GB log? Write a retry decorator. Why use a context manager for files and locks?

## 3. Files, Logs, Regex, Data Cleaning

Cover:

- Streaming files line by line
- `pathlib`, `csv`, `json`, and `re`
- Malformed record validation and duplicate detection
- Aggregation with `Counter` and `defaultdict`

Questions: Count errors per host. Clean corrupted inventory. Compare expected and discovered hosts. Return top error-producing devices.

## 4. Concurrency and Internals

Cover:

- GIL and its operational effect
- I/O-bound versus CPU-bound work
- Threads, processes, futures, timeouts, locks, and race conditions
- `ThreadPoolExecutor` and `ProcessPoolExecutor`
- Bounded concurrency and exception collection

Questions: Why do threads help SSH checks despite the GIL? How would you check 500 servers using only 20 workers? When should multiprocessing be used?

## 5. Infrastructure Automation

Cover:

- Safe `subprocess.run` usage
- Timeouts, return codes, and command-injection prevention
- Retry with backoff and jitter
- Structured logging, idempotency, batch execution, and partial failure
- Parsing `df`, `iostat`, and storage-health output

## 6. Data Structures and Algorithms

Prioritize dictionaries, sets, strings, stacks, queues, sorting, heaps, intervals, sliding windows, and basic graphs. Start with correct easy-to-medium solutions rather than hard dynamic programming.

## 7. Testing and Debugging

Cover `pytest`, assertions, fixtures, parameterization, mocking `subprocess`, temporary files, and failure testing.

Find and repair whole-file reads, unsafe `shell=True`, missing timeouts, broad exception handling, unbounded threads, shared mutable state, and retries of permanent failures.

## Libraries to Know

Standard library:

- `collections`: `Counter`, `defaultdict`, `deque`
- `re`, `pathlib`, `os`, `subprocess`
- `concurrent.futures`, `threading`
- `json`, `csv`, `logging`, `argparse`
- `datetime`, `time`, `heapq`, `itertools`, `functools`
- `contextlib`, `dataclasses`, `typing`, `tempfile`, `unittest.mock`

Useful external libraries: `pytest`, `requests`, `psutil`, `PyYAML`. Prefer the standard library in timed coding environments unless external packages are permitted.

---

# 15 Common Practice Problems with Simple Solutions

## 1. Two Sum

```python
def two_sum(values: list[int], target: int) -> tuple[int, int] | None:
    seen: dict[int, int] = {}
    for index, value in enumerate(values):
        required = target - value
        if required in seen:
            return seen[required], index
        seen[value] = index
    return None
```

Complexity: `O(n)` time, `O(n)` space. Infrastructure variation: find two capacity allocations that meet a target.

## 2. Remove Duplicates While Preserving Order

```python
def unique_hosts(hosts: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for host in hosts:
        if host not in seen:
            seen.add(host)
            result.append(host)
    return result


assert unique_hosts(["node1", "node2", "node1"]) == ["node1", "node2"]
```

Complexity: `O(n)` average time, `O(n)` space.

## 3. Reconcile Server Inventory

```python
def reconcile(expected: dict[str, str], actual: dict[str, str]) -> dict:
    expected_hosts = set(expected)
    actual_hosts = set(actual)
    mismatched = {
        host: (expected[host], actual[host])
        for host in expected_hosts & actual_hosts
        if expected[host] != actual[host]
    }
    return {
        "missing": sorted(expected_hosts - actual_hosts),
        "unexpected": sorted(actual_hosts - expected_hosts),
        "mismatched": mismatched,
    }
```

Complexity: `O(n + m)` time and space.

## 4. Valid Brackets

```python
def valid_brackets(text: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for character in text:
        if character in "([{":
            stack.append(character)
        elif character in pairs:
            if not stack or stack.pop() != pairs[character]:
                return False
    return not stack
```

Complexity: `O(n)` time, `O(n)` worst-case space.

## 5. First Non-Repeating Event

```python
from collections import Counter


def first_unique(events: list[str]) -> str | None:
    counts = Counter(events)
    return next((event for event in events if counts[event] == 1), None)
```

Complexity: `O(n)` time, `O(n)` space.

## 6. Top-K Error Hosts

Input format: `timestamp level host message`.

```python
from collections import Counter


def top_error_hosts(lines: list[str], limit: int = 3) -> list[tuple[str, int]]:
    counts: Counter[str] = Counter()
    for line in lines:
        fields = line.split(maxsplit=3)
        if len(fields) == 4 and fields[1] == "ERROR":
            counts[fields[2]] += 1
    return counts.most_common(limit)
```

Parsing is `O(n)`. Discuss malformed lines and deterministic ordering for equal counts.

## 7. Stream a Large Log File

```python
from collections.abc import Iterator
from pathlib import Path


def matching_lines(path: Path, keyword: str) -> Iterator[str]:
    with path.open(encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if keyword in line:
                yield line.rstrip("\n")
```

Complexity: `O(n)` time and approximately `O(1)` additional memory.

## 8. Merge Maintenance Windows

```python
def merge_windows(windows: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not windows:
        return []
    ordered = sorted(windows)
    merged = [ordered[0]]
    for start, end in ordered[1:]:
        previous_start, previous_end = merged[-1]
        if start <= previous_end:
            merged[-1] = previous_start, max(previous_end, end)
        else:
            merged.append((start, end))
    return merged
```

Complexity: `O(n log n)` time, `O(n)` result space.

## 9. Moving Average of Latency

```python
from collections import deque


def moving_average(values: list[float], window: int) -> list[float]:
    if window <= 0:
        raise ValueError("window must be positive")
    queue: deque[float] = deque()
    total = 0.0
    averages: list[float] = []
    for value in values:
        queue.append(value)
        total += value
        if len(queue) > window:
            total -= queue.popleft()
        if len(queue) == window:
            averages.append(total / window)
    return averages
```

Complexity: `O(n)` time, `O(window)` space.

## 10. Detect Repeated Events Within a Time Window

Input must be ordered by timestamp.

```python
def repeated_events(events: list[tuple[int, str]], seconds: int) -> set[str]:
    last_seen: dict[str, int] = {}
    repeated: set[str] = set()
    for timestamp, name in events:
        if name in last_seen and timestamp - last_seen[name] <= seconds:
            repeated.add(name)
        last_seen[name] = timestamp
    return repeated
```

Complexity: `O(n)` average time, `O(u)` space for `u` unique events.

## 11. Retry Decorator

```python
from collections.abc import Callable
from functools import wraps
import time
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def retry(attempts: int, delay: float = 0.1):
    if attempts < 1:
        raise ValueError("attempts must be positive")

    def decorate(function: Callable[P, R]) -> Callable[P, R]:
        @wraps(function)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for attempt in range(attempts):
                try:
                    return function(*args, **kwargs)
                except TimeoutError:
                    if attempt == attempts - 1:
                        raise
                    time.sleep(delay * (2**attempt))
            raise RuntimeError("unreachable")
        return wrapper
    return decorate
```

Production discussion: retry only transient failures, add jitter, and confirm idempotency.

## 12. Run a Linux Command Safely

```python
import subprocess


def filesystem_usage(path: str) -> str:
    result = subprocess.run(
        ["df", "-P", path],
        capture_output=True,
        text=True,
        timeout=5,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "df failed")
    return result.stdout
```

Explain argument lists, timeout, return-code handling, and why untrusted input with `shell=True` is dangerous.

## 13. Concurrent Host Checks

```python
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed


def check_hosts(
    hosts: list[str], check: Callable[[str], bool], workers: int = 20
) -> dict[str, bool | str]:
    results: dict[str, bool | str] = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(check, host): host for host in hosts}
        for future in as_completed(futures):
            host = futures[future]
            try:
                results[host] = future.result()
            except Exception as error:
                results[host] = f"ERROR: {error}"
    return results
```

Discuss per-check timeouts, structured errors, bounded workers, and why threads fit network I/O.

## 14. Simple LRU Cache

```python
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.data: OrderedDict[str, object] = OrderedDict()

    def get(self, key: str) -> object | None:
        if key not in self.data:
            return None
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: str, value: object) -> None:
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)
```

Average `get` and `put`: `O(1)`. Variation: cache recently requested host metadata.

## 15. Detect a Dependency Cycle

```python
def has_cycle(graph: dict[str, list[str]]) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for dependency in graph.get(node, []):
            if visit(dependency):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in graph if node not in visited)
```

Complexity: `O(V + E)` time, `O(V)` space. Variation: validate service or rollout dependencies.

---

# Practice Sequence

1. Problems 1-7: dictionaries, sets, strings, generators, validation, and complexity.
2. Problems 8-10 and 14-15: intervals, queues, caches, and graphs.
3. Problems 11-13: subprocess safety, retry, concurrency, timeout, and partial failures.

For each answer say: “Let me confirm input, output, scale, and failure behaviour.” Then explain the straightforward approach, improvement, complexity, tests, and production safeguards.


# Round 2
Squarepoint Interview Syllabus
P0 — 1. General Linux
Boot flow: firmware → bootloader → kernel → systemd
Processes, threads, signals and exit codes
File descriptors, pipes, sockets and /proc
CPU, memory, disk and network troubleshooting
Permissions, users, groups, sudo, capabilities
Filesystems, mounts, page cache and disk space
Package management and shared libraries
Services, timers and dependency ordering with systemd
DNS, routing, ports, firewalls and TLS basics
Resource limits, cgroups and namespaces
Logs: journalctl, application logs and kernel logs
Commands to master:
ps top pidstat vmstat free iostat df du
ss ip dig curl lsof strace perf
systemctl journalctl dmesg
find awk sed grep sort uniq xargs
Interview scenarios:
Service is running but unreachable
Server has high load but low CPU utilization
Disk is full although large files cannot be found
Process is killed unexpectedly
Application works manually but fails under systemd
Intermittent DNS or connection failures
P0 — 2. Python Automation
Language
Lists, dictionaries, sets, tuples and complexity
Functions, comprehensions and generators
Classes, dataclasses and composition
Type hints and interfaces
Iterators, decorators and context managers
Modules, packages and virtual environments
Production automation
pathlib, os, subprocess, shutil
Files, JSON, YAML and configuration
REST APIs using requests or httpx
Logging and command-line interfaces
Threads, multiprocessing and asyncio
Timeouts, retries and bounded concurrency
Testing with pytest
Mocking external APIs and commands
Exception handling
Catch specific exceptions, not bare except
Preserve the original traceback
Use raise ... from ... for error context
Separate recoverable and fatal errors
Always apply timeouts to external operations
Retry only transient and idempotent operations
Clean up resources using context managers
Return meaningful exit codes from automation
Example discussion:
try:
    response = client.get(url, timeout=5)
    response.raise_for_status()
except TimeoutError:
    # Retry with a bounded policy
    ...
except AuthenticationError:
    # Fail immediately; retry will not help
    ...
P0 — 3. Python Coding Exercises
Practise easy-to-medium problems involving:
Strings and arrays
Dictionaries and frequency counting
Sets and duplicate detection
Stacks and queues
Sorting and custom keys
Sliding window
Two pointers
Binary search
Heaps
BFS and DFS
Intervals
Log parsing and aggregation
LRU cache
Rate limiter
Producer-consumer queue
Platform-oriented exercises:
Parse logs and return the top failing endpoints
Detect duplicate events within a time window
Implement exponential backoff
Run commands concurrently with a fixed limit
Tail a file and handle rotation
Compare two configuration files
Build a dependency execution order
Implement a health checker
Design a small command-line game cleanly
Focus on correctness, edge cases, complexity, tests and readable code—not clever one-line solutions.
P0 — 4. Centralised Logging
Architecture
Application
   → stdout/file/journald
   → Fluent Bit/Filebeat/Vector
   → Kafka or direct ingestion
   → Elasticsearch/OpenSearch/Loki
   → Kibana/Grafana
Topics
Structured JSON logging
Timestamps, time zones and clock synchronization
Log levels and correlation/request IDs
Multiline logs
Buffering and backpressure
Rotation and retention
Parsing and schema evolution
Indexing and partitioning
High-cardinality fields
Access control and sensitive-data redaction
Agent failure and local disk buffering
At-least-once delivery and duplicate logs
Cost and storage management
Design exercise: centralised logging for 5,000 servers across multiple regions.
P0 — 5. Git, GitLab and CI/CD
Git
Working tree, staging area and commit graph
Branches, tags and remote tracking
Merge, rebase and cherry-pick
Conflict resolution
Revert versus reset
Squash commits
Release tags
Protected branches and CODEOWNERS
Rebase versus merge
Merge: preserves existing commit history and creates a merge commit.
Rebase: rewrites commits onto a new base and changes commit hashes.
Avoid rebasing shared or protected branches.
Rebase feature branches before review when clean linear history is required.
Merge or squash-merge through the protected branch workflow.
CI normally validates the proposed merged result, not only the feature branch.
GitLab
Pipelines, stages, jobs and runners
Artifacts versus caches
Variables, secrets and environments
Rules, includes and reusable templates
Parent-child and multi-project pipelines
Merge-request pipelines
Protected variables and branches
Manual approvals and deployment gates
Retry, timeout and interruptible jobs
Pipeline design
Lint → Unit Test → Security Scan → Build
     → Integration Test → Publish Artifact
     → Deploy Staging → Smoke Test
     → Approval → Production → Verification
Know rollback, immutable artifacts, deployment locks and preventing two pipelines from racing.
P0 — 6. Containers and Docker
Fundamentals
Images, layers, containers and registries
Namespaces and cgroups
Overlay filesystem
PID 1 and signal handling
Volumes and networking
Image tags versus immutable digests
Runtime users and Linux capabilities
Optimising Python Dockerfiles
Use a suitable minimal base image
Pin dependencies
Copy dependency files before source code
Exploit layer caching
Use multi-stage builds
Build wheels separately
Avoid compilers in the runtime image
Run as a non-root user
Set PYTHONDONTWRITEBYTECODE=1
Set PYTHONUNBUFFERED=1
Use exec-form ENTRYPOINT or CMD
Add health checks only when meaningful
Handle SIGTERM and graceful shutdown
Scan images and generate an SBOM
Do not place secrets in image layers
.dockerignore
Exclude:
.git
.venv
__pycache__
.pytest_cache
coverage
tests/data
logs
secrets
build artifacts
Explain how build context size affects performance, cache efficiency and secret exposure.
P0 — 7. Containers in CI/CD
Understand this flow:
Git commit
  → CI tests
  → Build container once
  → Security scan
  → Push immutable image
  → Deploy same digest to staging
  → Integration/smoke tests
  → Promote same digest to production
  → Monitor or roll back
Key topics:
Build once, promote many
Registry authentication
Layer caching
Reproducible builds
Image signing and provenance
Vulnerability scanning
Deployment configuration versus image contents
Secrets injection
Rolling, blue-green and canary deployment
Database migration ordering
Rollback when schemas are incompatible
P0 — 8. Web Infrastructure and Scalability
Request path
Client → DNS → CDN/WAF → Load Balancer
       → Reverse Proxy → Application
       → Cache/Database/Queue
Topics
HTTP methods, headers and status codes
HTTPS and TLS termination
DNS and service discovery
Reverse proxies and load balancing
L4 versus L7 load balancers
Health checks
Stateless services
Horizontal versus vertical scaling
Connection pooling and keep-alive
Caching and invalidation
Sessions and authentication
Rate limiting
Database replication and partitioning
Queues and asynchronous work
Timeouts, retries and circuit breakers
Backpressure and load shedding
Observability and SLOs
Multi-region failover
Interview scenario: latency rises after traffic doubles although CPU remains below 50%.
P0 — 9. System Design: Start to Finish
Use this sequence consistently:
Clarify functional requirements.
Define availability, latency, throughput and durability targets.
Estimate traffic, storage and bandwidth.
Define APIs and data models.
Draw the high-level architecture.
Explain the request and data flow.
Identify stateful components.
Design scaling and partitioning.
Add caching and asynchronous processing.
Handle failures, retries and idempotency.
Add security and access control.
Define observability and alerts.
Explain deployment and rollback.
Identify bottlenecks and trade-offs.
Design exercises:
URL shortener
Centralised logging platform
CI/CD platform
Container image build service
Kafka-based event platform
Configuration distribution service
Global health-checking system
P0 — 10. URL Shortener
Cover:
URL creation and redirect APIs
Unique ID generation
Base62 encoding
Database schema
Cache strategy
Redirect latency
Expiration and deletion
Custom aliases
Abuse and malicious URLs
Analytics pipeline
Hot-key handling
Multi-region routing
Availability versus consistency
Be ready to explain why redirects are read-heavy and how cache failure affects the database.
P1 — 11. Kafka Onboarding
Concepts
Broker, topic, partition and replica
Producer, consumer and consumer group
Partition keys and ordering
Offsets and retention
At-most-once, at-least-once and effectively-once processing
Producer acknowledgements and idempotence
Consumer rebalancing
Lag and backpressure
Schema Registry and compatibility
Dead-letter topics
Security: TLS, SASL and ACLs
Capacity and partition planning
Onboarding workflow
Establish data owner and use case.
Define schema and compatibility policy.
Estimate message rate, size and retention.
Select partition key and partition count.
Define producer reliability settings.
Define consumer group and offset policy.
Configure ACLs and credentials.
Create dashboards and lag alerts.
Test failure, replay and duplicate handling.
Document support ownership and recovery procedures.
P0 — 12. Project Examples and STAR Preparation
Prepare three strong projects:
Linux automation project
Automated diagnosis or remediation across many servers
Include concurrency limits, safety controls and rollback
Quantify investigation time or failure reduction
CI/CD and container project
Improved build speed, reliability or security
Explain caching, immutable artifacts and deployment strategy
Quantify build-time, deployment-frequency or failure-rate improvement
Scalable infrastructure project
Logging, Kafka, web platform or monitoring architecture
Explain capacity, bottlenecks and failure handling
Quantify availability, throughput, latency and cost
For each project prepare:
Situation: production context and business impact
Task: your ownership and constraints
Action: technical decisions and trade-offs
Result: measurable outcome
Follow-up: what failed, what you learned and what you would redesign
Recommended Study Order
Linux troubleshooting  
Python coding and automation  
Git/GitLab and CI/CD  
Docker and container pipelines  
Networking and web infrastructure  
Centralised logging  
System design and URL shortener  
Kafka onboarding  
Project stories and mock interviews