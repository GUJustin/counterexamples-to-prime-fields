import json,os,pathlib,signal,subprocess,sys,time
base=pathlib.Path(__file__).resolve().parent
prefix=sys.argv[1]; command=sys.argv[2:]
start=time.monotonic();peak=0;reason=None
with (base/(prefix+'.json')).open('w') as out,(base/(prefix+'.resources.txt')).open('w') as err:
    proc=subprocess.Popen(['/usr/bin/time','-l']+command,cwd=base,stdout=out,stderr=err,start_new_session=True)
    while proc.poll() is None:
        rows=subprocess.check_output(['ps','-axo','pgid=,rss='],text=True).splitlines()
        rss=sum(int(row.split()[1]) for row in rows if len(row.split())==2 and int(row.split()[0])==proc.pid)
        peak=max(peak,rss)
        if rss>384*1024 or time.monotonic()-start>60:
            reason='memory' if rss>384*1024 else 'time'
            os.killpg(proc.pid,signal.SIGKILL);proc.wait();break
        time.sleep(.2)
receipt={'command':command,'exit':proc.returncode,'wall_seconds':time.monotonic()-start,'sampled_peak_process_group_kib':peak,'limit_seconds':60,'limit_mib':384,'termination_reason':reason}
(base/(prefix+'.watchdog.json')).write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
if proc.returncode:sys.exit(proc.returncode)
