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

Sources:
* [Ania Kubów's OpenTelemetry Course](https://www.youtube.com/watch?v=r8UvWSX3KA8)

# What does a trace look like?

![alt text](https://www.sentinelone.com/wp-content/uploads/2020/08/26115528/span.png)

* Trace ID is generated when the first request is made
* Span ID is generated as the request arrives at each microservice
* Parent ID stores the parent service

![alt text](https://www.jaegertracing.io/img/spans-traces.png)

* Span - a single operation within a trace. It represents work done by a single service which can be broken down further depending on the use case.
* Trace - A collection of spans from a single user request forms a trace. A trace context is passed along when requests travel between services, which tracks a user request across services.

# OpenTelemetry

OpenTelemetry, also known as OTel for short, is a vendor-neutral open-source Observability framework for instrumenting, generating, collecting, and exporting telemetry data such as traces, metrics, logs. It is a collection of tools, APIs, and SDKs. Use it to instrument, generate, collect, and export telemetry data (metrics, logs, and traces) to help analyze software performance and behavior.

## Instrumentation

* In order to make a system observable, it must be instrumented: That is, the code must emit traces, metrics, and logs.

## Collector

* The OpenTelemetry Collector is a vendor-agnostic proxy that can receive, process, and export telemetry data. It supports receiving telemetry data in multiple formats (e.g., OTLP, Jaeger, Prometheus, as well as many commercial/proprietary tools) and sending data to one or more backends.

## Exporter

# Jaeger

Jaeger is an open-source distributed tracing tool meant to monitor and troubleshoot transactions in distributed systems. It was built by teams at Uber and then open-sourced in 2015. Jaeger is also a Cloud Native Computing Foundation graduate project.

OpenTelemetry will only provide the structured tracing data, this data needs to be exported to be analyzed and visualized. This is where tools like Jaeger come into play.

## Architecture

![alt text](https://www.aspecto.io/wp-content/uploads/2022/02/All-Jaeger-Architecture--1024x612.jpg)

* Jaeger Client: Jaeger clients are language specific implementations of the OpenTracing API. They can be used to instrument applications for distributed tracing either manually or with a variety of existing open source frameworks, such as Flask, Dropwizard, gRPC, and many more, that are already integrated with OpenTracing.
* Jaeger Agent: Jaeger agent is a network daemon that listens for spans received from the Jaeger client over UDP. It gathers batches of them and then sends them together to the collector.
* Jaeger Collector: The Jaeger collector is responsible for receiving traces from the Jaeger agent and performs validations and transformations. After that, it saves them to the selected storage backends.
* Storage Backends: Jaeger supports various storage backends – which store the spans & traces for later retrieving them. Supported storage backends are In-Memory, Cassandra, Elasticsearch, and Kafka (only as a buffer to another storage like Cassandra or elasticsearch).
* Jaeger Query: This is a service responsible for retrieving traces from the jaeger storage backend and making them accessible for the jaeger UI.
* Jaeger UI: a React application that lets you visualize the traces and analyze them. Useful for debugging system issues.
* Ingester: Ingester is relevant only if we use Kafka as a buffer between the collector and the storage backend. It is responsible for receiving data from Kafka and ingesting it into the storage backend. More info can be found in the official Jaeger Tracing docs.

Sources:
* [Jaeger Architecture](https://www.jaegertracing.io/docs/1.23/architecture/)
* [Components of Jaeger Architecture](https://www.aspecto.io/blog/jaeger-tracing-the-ultimate-guide/#jaeger-tracing-architecture)

# Demo
* View readme in demo directory for details.

## OpenTelemetry Community Demo

* [The OpenTelemetry Astronomy Shop](https://github.com/open-telemetry/opentelemetry-demo), is a microservice-based distributed system intended to illustrate the implementation of OpenTelemetry in a near real-world environment. It a community driven project and is the most comprehensive OpenTelemetry showcase/demo available.