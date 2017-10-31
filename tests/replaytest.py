import os

from cacofonisk import BaseReporter
from cacofonisk.channel import ChannelManager
from cacofonisk.runners.file_runner import FileRunner
from cacofonisk.utils.testcases import BaseTestCase


class TestReporter(BaseReporter):
    """TestReporter collects the events generated by ChannelManager.

    The events can be retrieved later to see which events have been generated
    during the test.
    """
    def __init__(self):
        super(TestReporter, self).__init__()
        self.events = []

    def on_b_dial(self, call_id, caller, to_number, targets):
        targets.sort(key=lambda callee: callee.code)

        self.events.append({
            'event': 'on_b_dial',
            'call_id': call_id,
            'caller': caller,
            'to_number': to_number,
            'targets': targets,
        })

    def on_warm_transfer(self, new_id, merged_id, redirector, caller, callee):
        self.events.append({
            'event': 'on_warm_transfer',
            'redirector': redirector,
            'caller': caller,
            'callee': callee,
            'new_id': new_id,
            'merged_id': merged_id,
        })

    def on_cold_transfer(self, call_id, merged_id, redirector, caller, to_number, targets):
        targets.sort(key=lambda callee: callee.code)

        self.events.append({
            'event': 'on_cold_transfer',
            'redirector': redirector,
            'caller': caller,
            'targets': targets,
            'new_id': call_id,
            'merged_id': merged_id,
            'to_number': to_number,
        })

    def on_up(self, call_id, caller, to_number, callee):
        self.events.append({
            'event': 'on_up',
            'caller': caller,
            'to_number': to_number,
            'callee': callee,
            'call_id': call_id,
        })

    def on_hangup(self, call_id, caller, to_number, reason):
        self.events.append({
            'event': 'on_hangup',
            'caller': caller,
            'to_number': to_number,
            'reason': reason,
            'call_id': call_id,
        })


class BogoRunner(object):
    def __init__(self, events, reporter):
        self.events = events
        self.reporter = reporter
        self.channel_managers = []

    def run(self):
        channelmgr = ChannelManager(reporter=self.reporter)
        for event in self.events:
            if ('*' in channelmgr.INTERESTING_EVENTS or
                    event['Event'] in channelmgr.INTERESTING_EVENTS):
                channelmgr.on_event(event)

        self.channel_managers.append(channelmgr)


class ChannelEventsTestCase(BaseTestCase):
    """
    Run event tests based on the JSON sample data.
    """
    maxDiff = 8192

    def events_from_tuples(cls, tuples):
        """
        Convert a list of tuples to the expected event list.

        Example::

            events = events_from_tuples((
                ('on_b_dial', (126680001, '', '201', True),
                              (126680003, '', '203', True)),
                ('on_transfer', (126680001, '', '201', True),
                                (126680002, '', '202', True),
                                (126680003, '', '203', True)),
            ))
            events == tuple([
                {'event': 'on_b_dial',
                 'caller': CallerId(126680001, '', '201', True),
                 'callee': CallerId(126680003, '', '203', True)},
                {'event': 'on_transfer',
                 'redirector': CallerId(126680001, '', '201', True),
                 'caller': CallerId(126680002, '', '202', True),
                 'callee': CallerId(126680003, '', '203', True)},
            ])

        Args:
            tuples: An iterable with iterables, see example.

        Returns:
            tuple: A tuple of dictionaries, see example.
        """
        results = []

        for data in tuples:
            event_name, event_data = data
            event_data['event'] = event_name
            results.append(event_data)

        return tuple(results)

    def run_and_get_events(self, filename, reporter=None):
        absolute_path = os.path.join(os.path.dirname(__file__), filename)

        if reporter is None:
            reporter = TestReporter()

        runner = FileRunner([absolute_path], reporter=reporter)
        runner.run()

        assert len(runner.channel_managers) == 1
        return tuple(reporter.events)
