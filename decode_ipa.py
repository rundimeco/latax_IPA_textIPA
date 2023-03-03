import json

def transform_str(s, verbose = False):
  with open("dic_ipa.json") as f:
    dic_ipa = json.load(f)
  out = ""
  miss = []
  for car in s:
    if car in dic_ipa:
      if "{" in car:#uses simple latex tricks
        out += dic_ipa[car]
      else:#uses the tipa package
        out += "\\textipa{%s}"%dic_ipa[car]
    else:
      miss.append(car)
      out+= car
  if verbose == True:
    print("Missing:", miss)
  return out


if __name__=="__main__":
  import sys
  s = sys.argv[1]
  print(transform_str(s, True))
