#!/bin/bash
cd "$(dirname "$0")"
python3 bridge.py --login
read -n 1 -s -r -p "按任意键关闭……"
