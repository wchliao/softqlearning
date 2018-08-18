# Soft Q-learning For Trajectories Collection

## Introduction

This repo fixes some bugs in the [original repo](https://github.com/haarnoja/softqlearning). 

## Installation

Please refer to the [instructions](README.origin.md) and the following corrections for the usage.
   
1. ` ImportError: No module named 'softqlearning'`  
   If `softqlearning` module cannot be found, please add its path to the `PYTHONPATH` environment variable.
   ```
   cd <softqlearning PATH>
   export PYTHONPATH=$(pwd):${PYTHONPATH}
   ```
   
2. `ImportError: cannot import name 'LinearNDInterpolator'`  
   If `LinearNDInterpolator` cannot be found, reinstall `scipy`.  
   ```
   pip uninstall scipy
   pip install scipy
   ```

## How To Use

1. Train soft Q-learning in SingleGoalEnv
   1. In file `<softqlearning PATH>/examples/all_sql.py`:
      Assign goal position in line 109
   2. ```python ./examples/all_sql.py --env=singlegoal --log_dir=<model PATH>```

2. Save trajectories  
   ```
   python ./scripts/sim_policy.py <model PATH> --save --save_name <trajectory FILENAME>
   ```
   You can also use flag `--num-trajectory` to assign the number of trajectories you want to sample. (Default: 50)

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

4. Add more features to simulation
   Add features in `<softqlearning PATH>/softqlearning/scripts/sim_policy.py`  

5. Add MultiGoalEnv and SingleGoalEnv in `<softqlearning PATH>/examples/all_sql.py`
