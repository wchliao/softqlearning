# Soft Q-learning For Trajectories Collection

## Introduction

This repo fixes some bugs in the [original repo](https://github.com/haarnoja/softqlearning). 

## Usage

Please refer to the [instructions](README.origin.md) and the following corrections for the usage.
   
1. ` ImportError: No module named 'softqlearning'`  
   If `softqlearning` module cannot be found, please add its path to the `PYTHONPATH` environment variable.
   ```
   cd <softqlearning PATH>
   export PYTHONPATH=$(pwd):${PYTHONPATH}
   ```
   
2. `ImportError: cannot import name 'LinearNDInterpolator'`  
   If 'LinearNDInterpolator' cannot be found, reinstall `scipy`.  
   ```
   pip uninstall scipy
   pip install scipy
   ```

## Contributions

The following are the contributions. The corrected `rllab` is included in this repo.

1. Fix `rllab` typo  
   According to the [issue](https://github.com/rll/rllab/issues/240), there is a typo in the original `rllab`.
     
   In file `<rllab PATH>/rllab/sampler/stateful_pool.py`:  
   `from joblib.pool import MemmapingPool` -> `from joblib.pool import MemmappingPool`.  

2. Disable animation  
   In file `<softqlearning PATH>/softqlearning/scripts/sim_policy.py`:
   Remove `animated=True`

3. Remove useless rollout return  
   Rllab requires action information and environment information in rollout, but soft Q-learning does not implement these elements, which will trigger an error.  
   Therefore, we remove the requirement for action and environment information in order to avoid the error.
   
   In file `<rllab PATH>/rllab/sampler/utils.py`:  
   Remove `agent_infos` and `env_infos` for return

4. Add a variable to assign the number of trajectory
   In file `<softqlearning PATH>/softqlearning/scripts/sim_policy.py`:  
   Add `num-trajectory`