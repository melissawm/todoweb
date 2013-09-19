import subprocess

p = subprocess.Popen('todo.sh -d /home/melissa/Dropbox/todo/todo.cfg lsp', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
retval = p.wait()

lines = p.stdout.readlines();

web = open('todoweb.html','w')
print >> web, '<!DOCTYPE html><html><body>'
print >> web, '<style type="text/css"> p.A { color: red; margin-left: 40px; margin-top: 30px; } </style>'
print >> web, '<h1>todo.web</h1>'
print >> web, '<center><table>'
for line in lines[0:-2]:
    if line[10:13] == '(A)':
        print >> web, '<tr style=color:red>'
    elif line[10:13] == '(B)':
        print >> web, '<tr style=color:green>'
    elif line[10:13] == '(C)':
        print >> web, '<tr style=color:blue>'
    print >> web, '<td>', line[10:13], '</td>','<td>', line[13:-5], '</td>'
    print >> web, '</tr>'
print >> web, '</table></center>'
print >> web, '</body></html>'
web.close()
