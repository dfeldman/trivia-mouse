import json

questions = open("questions-from-chatgpt.txt").read().split("\n\n")
output=[]
seen=set()
for q in questions:
    q_lines = q.split("\n")
    if len(q_lines) != 6:
        print("Invalid question: ", q)
        continue
    q_text = q_lines[1].strip()
    if q_text in seen:
        print("Duplicate question:",q_text)
        continue
    seen.add(q_text)
    q_formatted = {"category": q_lines[0].strip(),
                   "question": q_lines[1].strip(),
                   "answers": [q_lines[2].strip(), q_lines[3].strip(), q_lines[4].strip(), q_lines[5].strip()],
                   "seen": 0
    }
    output += [q_formatted]

f=open("questions.json","w")
f.write("questions=")
f.write(json.dumps(output, indent=2))
f.close()
print ("Converted ", len(output), " questions")
