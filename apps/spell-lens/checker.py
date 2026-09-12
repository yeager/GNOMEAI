import subprocess

def check(text, language='en_US'):
    run=subprocess.run(['hunspell','-a','-d',language],input=text,text=True,capture_output=True,check=False)
    if run.returncode != 0: raise RuntimeError(run.stderr.strip() or 'Hunspell failed')
    issues=[]
    for line in run.stdout.splitlines()[1:]:
        if line.startswith('& ') or line.startswith('# '):
            word=line.split()[1]; issues.append(word)
    return issues
