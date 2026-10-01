#!/bin/bash
cd "$(dirname "$0")"
if command -v python3 >/dev/null 2>&1; then
  python3 bridge.py
else
  echo "启动失败：请先安装 Python 3（https://www.python.org/downloads/）。"
  read -n 1 -s -r -p "按任意键关闭……"
fi
