import os, sys, contextlib

os.environ["PYTHONWARNINGS"] = "ignore"
real_stdout = sys.stdout
with open(os.devnull, "w") as devnull, contextlib.redirect_stdout(devnull):
    from fle.env.protocols._mcp import mcp, tools, resources, prompts, unix_tools, version_control

sys.stdout = real_stdout
mcp.run()
