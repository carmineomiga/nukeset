#coding:utf8
import nuke
import os
import nukescripts
import sys
import subprocess

# 생각해야 할 경우의 수
# 1. linux, mac, windows
# 2. 노드 선택, 노드 다중 선택, 노드 선택X, 파일X

# node = nuke.selectedNode()
# path = node["file"].value()
# os.system("nautilus %s" % os.path.dirname(path))

def checkBrws(path):
	brws = ""
	if sys.platform == "linux2":
		brws = "nautilus"
	elif sys.platform == "win32":
		brws = "start"
	elif sys.platform == "darwin":
		brws = "open"
	p = subprocess.Popen([brws, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = p.communicate()
	if stderr:
		nuke.tprint(stderr, file=sys.stderr)
	if stdout:
		nuke.tprint(stdout)

def main():
	node = nuke.selectedNode()
	path = node["file"].value()
	dirname = os.path.dirname(path)
	checkBrws(dirname)
