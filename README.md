## Adaptive-FAM: *Adaptive Multi-Resolution Encoding for Interactive Large-Scale Volume Visualization through Functional Approximation*
Created by <a href="https://sunjianxin.github.io/" target="_blank">Jianxin Sun</a>, <a href="https://cse.unl.edu/~yu/" target="_blank">Hongfeng Yu</a> from University of Nebraska-Lincoln, and <a href="https://mathweb.ucsd.edu/~dlenz/" target="_blank">David Lenz</a>, <a href="https://www.mcs.anl.gov/~tpeterka/" target="_blank">Tom Peterka</a> from Argonne National Laboratory

Paper can be found <a href="https://arxiv.org/abs/2409.00184" target="_blank">here</a>.

![results](https://github.com/adaptive-fam/Adaptive-FAM/blob/main/flame_blocks_small.png)

### Introduction
This repo contains the code of practicing the proposed Adaptive-FAM multi-resolution encoding and how to render the encoded micro-models for visualization.

### Execution
1. Encoding

Run Adaptive-FAM.ipynb for the proposed adaptive encoding using functional approximation. It includes steps of micro-blocks (without ghost area) creation and their modeling into micro-models.

Run block_partition_down_sampling.ipynb for micro-blocks without ghost area.

2. Rendering

