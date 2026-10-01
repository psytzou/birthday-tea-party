#!/usr/bin/env python3
"""Local bridge for the birthday page's 进阶模式.

Lets the page talk to the Claude Code installed on this computer, using your own
Claude login. No API key is needed.

Usage:
    python bridge.py

Then open the page and switch to 进阶模式. Keep this window open while chatting.
Requires Python 3.8+ and Claude Code (`claude`) installed and signed in.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("BRIDGE_PORT", "8765"))

# Only these pages may use the bridge. "null" is a page opened from a local file.
ALLOWED_ORIGINS = {
    "https://psytzou.github.io",
    "http://localhost:8724",
    "http://127.0.0.1:8724",
    "null",
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
                data = json.loads(out)
                return str(data.get("result", "")).strip()
            except json.JSONDecodeError:
                return out
        last_error = (proc.stderr or out or "").strip()
        if "unknown option" not in last_error.lower():
            break
    raise RuntimeError(last_error[:500] or "claude exited without output")


class Handler(BaseHTTPRequestHandler):
    def _origin_ok(self):
        return self.headers.get("Origin") in ALLOWED_ORIGINS

    def _cors(self):
        origin = self.headers.get("Origin")
        if origin in ALLOWED_ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            # Lets a public https page reach this local server in Chromium browsers.
            self.send_header("Access-Control-Allow-Private-Network", "true")

    def _json(self, status, body):
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_OPTIONS(self):
        self.send_response(204 if self._origin_ok() else 403)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if not self._origin_ok():
            return self._json(403, {"error": "origin not allowed"})
        if self.path == "/health":
            return self._json(200, {"ok": True})
        self._json(404, {"error": "not found"})

    def do_POST(self):
        if not self._origin_ok():
            return self._json(403, {"error": "origin not allowed"})
        if self.path != "/chat":
            return self._json(404, {"error": "not found"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 200_000:
                return self._json(400, {"error": "bad request size"})
            prompt = str(json.loads(self.rfile.read(length)).get("prompt", "")).strip()
            if not prompt:
                return self._json(400, {"error": "empty prompt"})
            self._json(200, {"text": run_claude(prompt)})
        except subprocess.TimeoutExpired:
            self._json(504, {"error": "Claude took too long to reply"})
        except Exception as exc:  # report any failure back to the page
            self._json(500, {"error": str(exc)})

    def log_message(self, fmt, *args):
        sys.stderr.write("[bridge] " + (fmt % args) + "\n")


def main():
    if not CLAUDE:
        sys.exit("找不到 claude 命令。请先安装 Claude Code 并登录：https://claude.com/claude-code")
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"✓ 生日茶话会桥接已启动：http://127.0.0.1:{PORT}")
    print("  现在打开网页，切换到「进阶模式」就可以聊天了。聊天时请不要关闭这个窗口。")
    print("  按 Ctrl+C 退出。")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已退出。")


if __name__ == "__main__":
    main()
