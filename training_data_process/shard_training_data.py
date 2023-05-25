import numpy as np
import random
import os


# START configurations

# NOTE if you don't want set env, then set your working dir here
data_dir = ''
if not data_dir:
    # NOTE to avoid exposing your personal working folder
    working_dir = os.getenv('ChineseGPTDataDirectory')
    if not working_dir:
        raise ValueError('data directory should be set')

# NOTE this is the large training data file
DataFile = '{0}/chinese_corpus_token_len_1024.txt'.format(data_dir)
DataFile_Sharded = '{0}/chinese_corpus_sharded/train_{0}.tsv'.format(data_dir)

TrainingDataFileNum = 1000

# END configurations


def get_ranges(shard_num):
    step = 1 / shard_num
    index = 0
    shard_ranges = {}
    for i in np.arange(0, 1, step):
        shard_ranges[i] = index
        index += 1
    return shard_ranges


def shard_data():
    shard_ids = list(range(0, TrainingDataFileNum))
    sharded_samples = {}
    refresh_threshold = 100
    for k in shard_ids:
        sharded_samples[k] = []
    with open(DataFile, 'r', encoding='utf-8') as rf:
        for line in rf:
            shard_id = random.choice(shard_ids)
            sharded_samples[shard_id].append(line)
            if len(sharded_samples[shard_id]) > refresh_threshold:
                shard_file = DataFile_Sharded.format(shard_id)
                with open(shard_file, 'a', encoding='utf-8') as wf:
                    for i in sharded_samples[shard_id]:
                        wf.write(i)
                sharded_samples[shard_id] = []

    # handle left samples
    for shard_id in sharded_samples:
        if sharded_samples[shard_id]:
            shard_file = DataFile_Sharded.format(shard_id)
            with open(shard_file, 'a', encoding='utf-8') as wf:
                for i in sharded_samples[shard_id]:
                    wf.write(i)


if __name__ == '__main__':
    shard_data()
