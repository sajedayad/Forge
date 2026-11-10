"""Builds index.html (one self-contained file) from src/. Run: python3 build.py"""
import os
d = os.path.dirname(os.path.abspath(__file__))
r = lambda n: open(os.path.join(d, "src", n), encoding="utf8").read()
HEAD = open(os.path.join(d, "src", "head.html"), encoding="utf8").read()
out = HEAD + "<style>\n" + r("app.css") + "</style>\n</head>\n<body>\n" + r("shell.html") + "\n<script>\n" + r("app.js") + "</script>\n</body>\n</html>\n"
open(os.path.join(d, "index.html"), "w", encoding="utf8").write(out)
print("built index.html,", len(out), "bytes")
