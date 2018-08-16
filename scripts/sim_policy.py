import argparse

import joblib
import numpy as np
import tensorflow as tf

from rllab.sampler.utils import rollout


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='Path to the snapshot file.')
    parser.add_argument('--max-path-length', '-l', type=int, default=1000)
    parser.add_argument('--speedup', '-s', type=float, default=1)
    parser.add_argument('--num-trajectory', '-n', type=int, default=100)
    parser.set_defaults(deterministic=True)

    args = parser.parse_args()

    return args


def simulate_policy(args):
    with tf.Session():
        data = joblib.load(args.file)
        if 'algo' in data.keys():
            policy = data['algo'].policy
            env = data['algo'].env
        else:
            policy = data['policy']
            env = data['env']

        paths = []
        for _ in range(args.num_trajectory):
            path = rollout(env, policy,
                           max_path_length=args.max_path_length,
                           speedup=args.speedup)
            paths.append(path)

        print('Average reward: {}'.format(np.mean([sum(p['rewards']) for p in paths])))


def main():
    args = parse_args()
    simulate_policy(args)


if __name__ == "__main__":
    main()
