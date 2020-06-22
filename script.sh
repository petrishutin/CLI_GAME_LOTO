#!/bin/bash
set -e
if [ "$ENV" = 'GAME' ]; then
  exec python main.py
elif [ "$ENV" = 'TEST' ]; then
  exec python -m pytest
fi