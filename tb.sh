#!/bin/bash
echo http://127.0.0.1:6006
tensorboard --logdir=runtime_files/logs > log.txt 2>&1 &
