import glob, os, shutil, re

p = re.compile(r'^([a-f0-9]+)_(.*)')

folder = 'files'
pat = os.path.join(folder,'*.py')
all_files = glob.glob(pat)

bool_list = []
big_list = []

just_test  = 1
for curpath in all_files:
    folder, curfile = os.path.split(curpath)
    q = p.match(curfile)
    if q:
        print('group(1) = ' + q.group(1))
        print('group(2) = ' + q.group(2))

        if len(q.group(1)) > 20:
            old_path = os.path.join(folder, curfile)
            new_path = os.path.join(folder, q.group(2))
            print('%s --> %s' % (old_path, new_path))
            if not just_test:
                shutil.move(old_path, new_path)
    else:
        print('no match: ' + curfile)

