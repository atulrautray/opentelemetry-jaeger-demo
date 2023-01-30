# Introduction

Observability can be defined as the measure of how well the internal states of a system can be inferred from knowledge of its external outputs. Logs, metrics, and traces are often known as the three pillars of observability. While plainly having access to logs, metrics, and traces doesn’t necessarily make systems more observable, these are powerful tools that, if understood well, can unlock the ability to build better systems.

# Three Pillars of Observability

## Event Logs
*  An event log is an immutable, timestamped record of discrete events that happened over time. Logs allow systems to be debugged at a very fine level of granularity. But, failures in complex distributed systems rarely arise because of one specific event happening in one specific component of the system. Often, various possible triggers across a highly interconnected graph of components are involved. By simply looking at discrete events that occurred in any given system at some point in time, it becomes impossible to determine all such triggers.

## Metrics
* Metrics are a numeric representation of data measured over intervals of time. Metrics can harness the power of mathematical modeling and prediction to derive knowledge of the behavior of a system over intervals of time in the present and future. Since numbers are optimized for storage, processing, compression, and retrieval, metrics enable longer retention of data as well as easier querying. This makes metrics perfectly suited to building dashboards that reflect historical trends. Metrics also allow for gradual reduction of data resolution. After a certain period of time, data can be aggregated into daily or weekly frequency. The biggest drawback with both application logs and application metrics is that they are system scoped, making it hard to understand anything else other than what’s happening inside a particular system.

## Traces
* A trace is a representation of a series of causally related distributed events that encode the end-to-end request flow through a distributed system. A single trace can provide visibility into both the path traversed by a request as well as the structure of a request. Collecting this information and reconstructing the flow of execution while preserving causality for retrospective analysis and troubleshooting enables one to better understand the lifecycle of a request. Having an understanding of the entire request lifecycle makes it possible to debug requests spanning multiple services to pinpoint the source of increased latency or resource utilization.

Logs, metrics, and traces serve their own unique purpose and are complementary. In unison, they provide maximum visibility into the behavior of distributed systems.

Sources:
* [Distributed Systems Observability by Cindy Sridharan](https://www.oreilly.com/library/view/distributed-systems-observability/9781492033431/ch04.html)

# Distributed Tracing

```
Abstraction makes things easier, which makes things harder.
```

```
A distributed system is one in which the failure of a computer you didn't even know existed can render your computer unusable. Leslie Lamport, 1987
```

## Why has distributed tracing become so popular? Logging and Metrics not enough?

* Systems are getting more complex by the day. In the past there was one big monolithic application that was running your business logic and finding an error was as simple as following the error logs. As we move to distributed system architectures, a single application might be composed of hundreds of sub-services. A failure in a complex, connected, ditributed system is a not an easy task. This is where tracing shines, tracing provides much required <b>context</b> to find these failure components.

Sources:
* [Observability, Distributed Tracing & the Complex World, talk by Dave McAllister](https://www.youtube.com/watch?v=2nTJSsBngao)

# History (OpenTrace, OpenCensus, OpenTelemetry)

In 2016 OpenTracing was released as a CNCF  project focused only around distributed tracing. Because the libraries were lightweight and  simple, it could be used to fit any use case. While it made it easy to instrument data, it made it hard to instrument software that was shipped as binaries without a lot of manual engineering work. In 2018, a similar project called OpenCensus was open source out of Google, which supported both the capturing retracing permission and metrics. While it made it easier to get telemetry data  from software that was shipped as binaries like Kubernetes, and databases, it made it hard to  use the API to instrument custom implementations, not part of the default use case. Both projects were able to make observability easy for modern applications and expedite wide adoption of distributed tracing by the software industry. However, developers had to choose  between two options with pros and cons. It turns out that the approaches of  the two projects were complimentary rather than contradictory. In late 2019, the two projects  merged to form OpenTelemetry. This brought forward the idea  of having a single standard for observability instead of two competing standards.

# What does a trace look like?

![alt text](https://www.sentinelone.com/wp-content/uploads/2020/08/26115528/span.png)

* Trace ID is generated when the first request is made
* Span ID is generated as the request arrives at each microservice
* Parent ID stores the parent service

![alt text](https://www.jaegertracing.io/img/spans-traces.png)

# OpenTelemetry

## Instrumentation

## Collector

## Exporter

# Jaeger

# Demo
* [work in progress]

## OpenTelemetry Community Demo

* [The OpenTelemetry Astronomy Shop](https://github.com/open-telemetry/opentelemetry-demo), a microservice-based distributed system intended to illustrate the implementation of OpenTelemetry in a near real-world environment. It a community driven project and is the most comprehensive OpenTelemetry showcase/demo available.