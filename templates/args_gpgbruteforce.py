## Nozzlr template : Commandline arguments bruteforcer (PoC: breaking GpG .gpg encrypted files)
# @author intrd - http://dann.com.br/ 
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

# Make a copy of this template and adapt to your task!

from subprocess import Popen, PIPE, STDOUT

def nozz_module(payload, self=False, founds=False):
	payloads=':'.join(str(v) for v in payload.values())

	## Configs
	commandline="gpg --batch --yes --passphrase "+payload[0]+" -d test.txt.gpg"

	## Engine
	out={}
	out["code"]=""
	out["result"]=""
	code="null"
	try:
		process = Popen(commandline, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False)
		(output, err) = process.communicate()
	except Exception as e:
		#print " "
		out["result"]=format(str(e)).strip()
		out["code"]="error"
		return out
	if "decryption failed" in output or "system error" in output or "usage:" in output or "missing" in output or "error:" in output or "such" in output:
		out["code"]="NEXT"
	else:
		print output
		out["code"]="found: \""+payloads+"\""
	return out
		