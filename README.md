# Soft Q-learning For Trajectories Collection

## Introduction

This repo fixes some bugs in the [original repo](https://github.com/haarnoja/softqlearning). 

## Usage

Please refer to the [instructions](README.origin.md) and the following corrections for the usage.

1. Fix `rllab` typo  
   According to the [issue](https://github.com/rll/rllab/issues/240), there is a typo in the original `rllab`.  
   In the file `<rllab PATH>/rllab/sampler/stateful_pool.py`, the line  
   `from joblib.pool import MemmapingPool`  
   should be  
   `from joblib.pool import MemmappingPool`.  
   This repo has already fixed the typo and includes the corrected `rllab` in this repo.
2. If `softqlearning` module cannot be found, please add its path to the `PYTHONPATH` environment variable.
   ```
   cd <softqlearning PATH>
   export PYTHONPATH=$(pwd):${PYTHONPATH}
   ```
   