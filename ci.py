import wandb
import os

print(f"the version of wandb is: {wandb.__version__}")
assert wandb.__version__ == '0.17.5', f'Expected version 0.17.5 but got {wandb.__version__}'
