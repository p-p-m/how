from collections import defaultdict
from datetime import datetime


class UnprocessedBatch(Exception):
    pass


class Batch:

    def __init__(self, index, timestamp, is_bot, *users):
        self.timestamp = timestamp
        self.is_bot = is_bot
        self.users = users
        self.score = -1 if is_bot else 1
        self.index = index


class Stream:

    def __init__(self, allowance):
        self.users_scores = defaultdict(lambda: allowance)

    def add_batch(self, batch):
        scores_copy = self.users_scores.copy()
        for user in batch.users:
            scores_copy[user] += batch.score
        for score in scores_copy.values():
            if score < 0:
                raise UnprocessedBatch
        self.users_scores = scores_copy


def _is_next_day(previous, current):
    return (
        datetime.utcfromtimestamp(previous).day !=
        datetime.utcfromtimestamp(current).day
    )


def rateLimit(sentBatches, receivedMessages, startingAllowance):
    batches = [
        Batch(i, b[0], True, *b[1:]) for i, b in enumerate(sentBatches)
    ]
    batches += [
        Batch(i, m[0], False, *m[1:]) for i, m in enumerate(receivedMessages)
    ]
    stream = Stream(startingAllowance)
    batches = sorted(batches, key=lambda b: (b.timestamp, b.index, b.is_bot))
    result = []
    previous = None
    for batch in batches:
        if previous and _is_next_day(previous.timestamp, batch.timestamp):
            stream = Stream(startingAllowance)
        try:
            stream.add_batch(batch)
        except UnprocessedBatch:
            result.append(batch.index)
        previous = batch
    return result


sentBatches = [[1471040000, 736273, 827482, 2738283],
               [1471040005, 736273, 2738283],
               [1471040010, 827482, 2738283],
               [1471040015, 2738283],
               [1471040025, 827482],
               [1471046400, 736273, 827482, 2738283]]

receivedMessages = [[1471040001, 2738283],
                    [1471040002, 2738283],
                    [1471040010, 827482],
                    [1471040020, 2738283]]

startingAllowance = 1


print rateLimit(sentBatches, receivedMessages, startingAllowance)
