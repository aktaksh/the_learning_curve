# Study path from foundations to HFT engineering

Work through one foundation and one practical exercise at a time. Advance when you can explain your observations without reading the answer.

## 1 Networking foundations

Read [networking foundations](01_networking_foundations.md), then the [CCNA syllabus](../01_networking/01_ccna/00_syllabus.md) and [labs](../01_networking/01_ccna/06_labs.md).

**LEARN** Addressing, subnet boundaries, Ethernet switching, routing, transport and packet capture.

**LAB** Draw the path between hosts across a router. Identify address changes, lookups and possible failure points.

**EVIDENCE** A topology, addressing table and capture you can explain. Distinguish DNS, transport and link problems before tuning.

## 2 Programming in parallel

Follow the [Python syllabus](../03_python/00_study_routes/syllabus_python.md) and [C++ refresher](../02_cpp/notes_syntax.md). Existing code files are exercises; some lessons contain prose and partial examples rather than complete programs.

**LAB** Parse a log, count events, handle malformed input and test the result. In C++, practise lifetime and ownership before concurrency.

**EVIDENCE** Working examples, test inputs and an explanation of error handling. A successful run alone does not establish correctness.

## 3 Operating and inspecting systems

Combine [Docker](02_docker_foundations.md), [Ansible](03_ansible_foundations.md), packet analysis and the Linux references.

**LAB** Explain a listening service, its process, its socket and how another host reaches it. Record the commands and observations supporting your explanation.

## 4 Apply foundations to HFT

Open the [HFT study route](../../HFT_Docs/index.html#05_learning_roadmaps%2F00_study_route.md). Follow queue ownership, CPU placement, memory access and time measurement through the same system.

**INTERNAL / LATENCY** Treat throughput, median latency, tail latency and jitter as separate observations. A change can improve one while worsening another.

**LAB** Record a baseline, change one factor and compare repeated runs. Explain the likely mechanism and an alternative explanation.

## 5 Advanced networking and revision

Use the [CCNP syllabus](../01_networking/02_ccnp/00_syllabus.md) after you can trace ordinary switching and routing without guessing. Let scenario questions identify gaps rather than memorising answers.

## A practical study session

Try 10 minutes recalling yesterday's topic, 20 reading, 20 practising and 10 explaining your evidence. Adjust for longer labs. Suggested revisit points are the next day, one week later and one month later; revisit sooner if recall fails.

Mark a topic ready for revision when you can explain it, demonstrate it, diagnose a failure and reproduce the result. Record evidence in the [tracker](05_study_tracker.md).
