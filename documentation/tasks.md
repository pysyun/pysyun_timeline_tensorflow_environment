# Tasks

## 2024.04.05

- [ ] Set up the project repository and development environment
  - [ ] Pull the Git repository
  - [ ] Set up virtual environment and install necessary dependencies
  - [ ] Configure IDE/editor for Python development

- [ ] Implement the `Environment` class
  - [ ] Inherit from the `Chainable` class to support chainable pipeline development
  - [ ] Implement the required methods for the `TFEnvironment` interface
    - [ ] `reset()`
    - [ ] `step(action)`
    - [ ] `current_time_step()`
  - [ ] Add any additional helper methods or properties as needed

- [ ] Integrate `StorageTimelineTimeline` with the `Environment`
  - [ ] Implement the necessary methods to feed timeline data into the `Environment`
  - [ ] Test the integration to ensure data flows correctly from the timeline to the environment

- [ ] Create a pipeline example using the Uniswap timeline
  - [ ] Fetch the list of timelines from the provided URL
  - [ ] Iterate over the list and build a `StorageTimelineTimeline` for each step
  - [ ] Create an instance of the `Environment` class
  - [ ] Build a pipeline to forward timeline data to the environment using the `|` operator
  - [ ] Test the pipeline and verify that the factual Tensorflow environment is obtained

- [ ] Update project documentation
  - [ ] Add usage instructions and examples to the README.md file
  - [ ] Document the `Environment` class and its methods
  - [ ] Provide instructions for running the Uniswap timeline example
