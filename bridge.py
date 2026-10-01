#!/usr/bin/env python3
"""Local launcher for the birthday page's 进阶模式.

Serves the page from this folder, opens it in your browser, and lets 进阶模式 talk to the
Claude Code installed on this computer using your own Claude login. No API key is needed.

Start it by double-clicking start.bat (Windows) or start.command (Mac), or run:
    python bridge.py

Requires Python 3.8+ and Claude Code (`claude`) installed and signed in.
"""
import functools
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import urllib.request
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("BRIDGE_PORT", "8765"))
HERE = os.path.dirname(os.path.abspath(__file__))
URL = f"http://127.0.0.1:{PORT}/"

# Pages allowed to send chat requests. The first two are this launcher itself.
ALLOWED_ORIGINS = {
    f"http://127.0.0.1:{PORT}",
    f"http://localhost:{PORT}",
    "https://psytzou.github.io",
}

CLAUDE = shutil.which("claude")
# An empty working directory, so Claude Code does not pick up any project files.
WORKDIR = tempfile.mkdtemp(prefix="birthday-bridge-")


def run_claude(prompt: str) -> str:
    """Send one prompt to `claude -p` through stdin and return the reply text."""
    base = [CLAUDE, "-p", "--output-format", "json"]
    # Newer versions accept --max-turns; fall back to the bare command if this one does not.
    attempts = [base + ["--max-turns", "1"], base]
    last_error = ""
    for args in attempts:
        proc = subprocess.run(
            args,
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=WORKDIR,
            timeout=240,
        )
        out = (proc.stdout or "").strip()
        if proc.returncode == 0 and out:
            try:
                return str(json.loads(out).get("result", "")).strip()
            except json.JSONDecodeError:
                return out
        last_error = (proc.stderr or out or "").strip()
        if "unknown option" not in last_error.lower():
            break
    raise RuntimeError(last_error[:500] or "claude exited without output")


class Handler(SimpleHTTPRequestHandler):
    def _cors(self):
        origin = self.headers.get("Origin")
        if origin in ALLOWED_ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            # Lets the public GitHub Pages copy reach this local server in Chromium browsers.
            self.send_header("Access-Control-Allow-Private-Network", "true")

    def _json(self, status, body):
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204 if self.headers.get("Origin") in ALLOWED_ORIGINS else 403)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path == "/health":
            return self._json(200, {"ok": True, "claude": bool(CLAUDE)})
        super().do_GET()  # the page itself, its images and scripts

    def do_POST(self):
        if self.headers.get("Origin") not in ALLOWED_ORIGINS:
            return self._json(403, {"error": "origin not allowed"})
        if self.path != "/chat":
            return self._json(404, {"error": "not found"})
        if not CLAUDE:
            return self._json(500, {"error": "没有找到 Claude Code，请先安装并登录"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 200_000:
                return self._json(400, {"error": "bad request size"})
            prompt = str(json.loads(self.rfile.read(length)).get("prompt", "")).strip()
            if not prompt:
                return self._json(400, {"error": "empty prompt"})
            self._json(200, {"text": run_claude(prompt)})
        except subprocess.TimeoutExpired:
            self._json(504, {"error": "Claude 回复太久了"})
        except Exception as exc:  # report any failure back to the page
            self._json(500, {"error": str(exc)})

    def log_message(self, fmt, *args):
        if self.command == "POST":
            sys.stderr.write("[bridge] " + (fmt % args) + "\n")


def already_running() -> bool:
    try:
        with urllib.request.urlopen(URL + "health", timeout=1) as r:
            return r.status == 200
    except Exception:
        return False


def main():
    if already_running():
        webbrowser.open(URL)
        return
    if not CLAUDE:
        print("⚠ 没有找到 claude 命令：标准模式可以用，进阶模式需要先安装并登录 Claude Code。")
        print("  https://claude.com/claude-code\n")
    server = ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Handler, directory=HERE))
    print(f"✓ 生日茶话会已启动：{URL}")
    print("  浏览器会自动打开。聊天时请不要关闭这个窗口，按 Ctrl+C 退出。")
    threading.Timer(0.8, lambda: webbrowser.open(URL)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已退出。")


if __name__ == "__main__":
    main()
