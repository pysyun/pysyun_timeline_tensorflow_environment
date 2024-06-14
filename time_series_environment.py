import numpy as np
from tf_agents.environments import py_environment
from tf_agents.specs import array_spec
from tf_agents.trajectories import time_step as ts


class TimeSeriesEnvironment(py_environment.PyEnvironment):
    def __init__(self):
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=1, name='action')
        self._observation_spec = array_spec.ArraySpec(
            shape=(None,), dtype=np.float32, name='observation')
        self._state = 0
        self._episode_ended = False
        self.data = []

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
        self._state = 0
        self._episode_ended = False
        return ts.restart(np.array(self.data[self._state]['values'], dtype=np.float32))

    def _step(self, action):
        if self._episode_ended:
            return self._reset()

        self._state += 1
        if self._state >= len(self.data):
            self._episode_ended = True
            return ts.termination(np.array(self.data[-1]['values'], dtype=np.float32), reward=0.0)
        else:
            return ts.transition(np.array(self.data[self._state]['values'], dtype=np.float32), reward=0.0, discount=1.0)

    def process(self, data):
        # Group data by week
        grouped_data = {}
        start_timestamp = None
        end_timestamp = None
        for item in data:
            timestamp = item['time']
            value = item['value']
            if start_timestamp is None:
                start_timestamp = timestamp
            end_timestamp = timestamp
            week_start = timestamp - (timestamp - 1) % (7 * 24 * 60 * 60 * 1000)  # Start of the week (Monday 00:00:01) in milliseconds
            if week_start not in grouped_data:
                grouped_data[week_start] = []
            grouped_data[week_start].append(value)

        # Fill in missing weeks with empty steps
        current_week = start_timestamp - (start_timestamp - 1) % (7 * 24 * 60 * 60 * 1000)
        last_week = end_timestamp - (end_timestamp - 1) % (7 * 24 * 60 * 60 * 1000)
        while current_week <= last_week:
            if current_week not in grouped_data:
                grouped_data[current_week] = [tf.constant([], shape=(0,), dtype=tf.float32)]
            current_week += 7 * 24 * 60 * 60 * 1000  # Move to the next week

        # Create step data with all values for each week (including empty weeks)
        self.data = [{'time': week_start, 'values': values} for week_start, values in sorted(grouped_data.items())]

        return self