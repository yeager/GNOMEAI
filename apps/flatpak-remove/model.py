from dataclasses import dataclass
@dataclass(frozen=True)
class App: app_id:str; name:str
def parse_list(text):
 out=[]
 for line in text.splitlines():
  fields=line.split('\t')
  if len(fields)>=2 and fields[0].strip(): out.append(App(fields[0].strip(), fields[1].strip() or fields[0].strip()))
 return out
