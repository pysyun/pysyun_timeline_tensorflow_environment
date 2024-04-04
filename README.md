# PySyun Timeline Tensorflow Environment

## Introduction

This library implements the [`TFEnvironment`](https://www.tensorflow.org/agents/tutorials/2_environments_tutorial) adapter 
for [`PySyun Timeline`](https://github.com/pysyun/pysyun-timeline) Pipelines.

The `Environment` class, implemented in this library, implements the [`Chainable`](https://github.com/pysyun/pysyun_chain?tab=readme-ov-file#chainable-class) interface to simplify chainable pipeline development. 

![Tensor flow](tensor_flow.png)

## Examples

### Uniswap Environment example
1. Consider, we have the [`List of timelines`](https://europe-west1-hype-dev.cloudfunctions.net/storage-timeline?schema=0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73.last-1000-pair). 
2. We iterate over this list to build [`StorageTimelineTimeline`](https://github.com/pysyun/pysyun-timeline/blob/master/pysyun/timeline/sources.py#L25) on each step.

   2.1. We make the time-line [`Chainable`](https://github.com/pysyun/pysyun_chain?tab=readme-ov-file#chainable-class).
3. We create the `Environment` instance.

   3.1. We make this also [`Chainable`](https://github.com/pysyun/pysyun_chain?tab=readme-ov-file#chainable-class).
4. We build a pipeline to forward all time-line data to the environment. Like that:

   ```text
   TimeLine() | Environment()
   ```

5. We get the factual Tensorflow environment from this chain. Like that:
   ```text
   (TimeLine() | Environment()).process()
   ```

## Team coordination
- Development tasks: [documentation/tasks.md](./documentation/tasks.md).
