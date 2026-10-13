"""将 loomis.glb 转为 base64，输出到 loomis.txt"""
import base64
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GLB_PATH = os.path.join(BASE_DIR, "loomis.glb")
TXT_PATH = os.path.join(BASE_DIR, "loomis.txt")

with open(GLB_PATH, "rb") as f:
    raw = f.read()

b64 = base64.b64encode(raw).decode("ascii")

with open(TXT_PATH, "w", encoding="ascii") as f:
    f.write(b64)

print(f"glb: {len(raw)} bytes -> base64: {len(b64)} chars")
print(f"written: {TXT_PATH}")
