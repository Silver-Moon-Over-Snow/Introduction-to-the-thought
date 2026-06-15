with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the QUESTIONS array
start = content.find('const QUESTIONS = [')
end = content.find('];', start) + 2
arr = content[start:end]

lines = arr.split('\n')
for i in range(len(lines) - 1):
    line = lines[i].rstrip()
    next_line = lines[i+1].lstrip()
    if line.endswith('}') and next_line.startswith('{') and not line.endswith('},'):
        print(f"Line {i+1} missing comma: ...{line[-40:]}")
