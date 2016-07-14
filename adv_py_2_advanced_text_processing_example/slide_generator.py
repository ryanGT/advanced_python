pres_header = """=============================================
%TITLE%
=============================================


%SUBTITLE%
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: Dr. Ryan Krauss

.. include:: /Users/rkrauss/git/report_generation/beamer_header.rst

.. role:: blue

.. role:: green
"""

import os, shutil
lectures_root = '/Users/rkrauss/raspi_lectures/020_advanced_python'
gitroot = 'https://github.com/ryanGT/advanced_python'

def gen_underline(str_in, symbol='='):
    N = len(str_in)
    return symbol*N


class slide(object):
    """Class for a slide with arbitrary lines as content."""
    def __init__(self, title, lines=[]):
        self.title = title
        self.lines = lines


    def _append_title(self):
        out = self.outlist.append
        out(self.title)
        under = gen_underline(self.title)
        out(under)#append underline
        out('')#append blank line


    def gen_rst(self):
        self.outlist = []
        self._append_title()
        
        for line in self.lines:
            self.outlist.append(line)

        self.outlist.append('')#append blank line
        return self.outlist

class bullet_slide(slide):
    def __init__(self, title, bullet_points=[], header='', footer=''):
        self.title = title
        self.bullet_points = bullet_points
        self.header = header
        self.footer = footer


    def gen_rst(self):
        self.outlist = []
        self._append_title()

        if self.header:
            self.outlist.append(self.header)
            self.outlist.append('')
            
        for bp in self.bullet_points:
            curline = '- %s' % bp
            self.outlist.append(curline)

        self.outlist.append('')#blank line

        if self.footer:
            self.outlist.append(self.footer)
            self.outlist.append('')#blank line
        
        return self.outlist
    

class presentation(object):
    def __init__(self, presnum, title, slides=[]):
        self.presnum = presnum
        self.title = title
        self.subtitle = 'Advanced Python %i' % self.presnum
        temp_header = pres_header.replace('%TITLE%',self.title)
        self.pres_header = temp_header.replace('%SUBTITLE%', self.subtitle)
        self.slides = slides


    def append_bullet_slide(self, title, bullets):
        new_slide = bullet_slide(title, bullets)
        self.slides.append(new_slide)


    def append_overview(self, bullets):
        self.append_bullet_slide('Overview',bullets)


    def append_topics(self, bullets):
        self.append_bullet_slide('Topics',bullets)


    def append_gen_slide(self, title, lines):
        new_slide = slide(title, lines)
        self.slides.append(new_slide)
        
        
    def append_github(self, link, folder='', main_file='', files=[]):
        link_line = '`<%s>`_' % link
        outlist = ['link:','',link_line]
        if folder:
            outlist.append('\nfolder:\n\n%s' % folder)
        if main_file:
            outlist.append('\nmain file:\n\n%s' %  main_file)
        if files:
            outlist.append('')
            if main_file:
                outlist.append('other files:')
            else:
                outlist.append('files:')

            outlist.append('')
            for curfile in files:
                outlist.append('- :code:`%s`' % cufile)
        outlist.append('')
        self.append_gen_slide('Github',outlist)

        
    def gen_rst_str(self):
        slide_list = []
        for slide in self.slides:
            curlist = slide.gen_rst()
            if curlist[-1] != '':
                curlist.append('')#force each slide to end with a blank line
            slide_list.extend(curlist)

        slides_str = '\n'.join(slide_list)
        out_str = self.pres_header + '\n' + slides_str
        self.out_str = out_str
        return self.out_str


    def build_filename(self):
        fn = 'adv_py_%0.2i_%s.rst' % (self.presnum, self.title)
        replace_list = [' ','/','\\',':']
        for item in replace_list:
            fn = fn.replace(item,'_')
        self.fn = fn
        return self.fn


    def make_folder(self):
        """Make a folder underneath lectures root to save the rst to"""
        if not hasattr(self,'fn'):
            self.build_filename()

        fno, ext = os.path.splitext(self.fn)
        self.folder = fno
        self.folder_path = os.path.join(lectures_root, self.folder)
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)


    def copy(self):
        """Copy to the lectures root subfolder"""
        self.dst_path = os.path.join(self.folder_path, self.fn)
        print('copying to %s' % self.dst_path)
        shutil.copy(self.fn, self.dst_path)


    def go(self):
        self.gen_rst_str()
        self.build_filename()
        f = open(self.fn, 'w')
        f.write(self.out_str)
        f.close()

        if os.getlogin() == 'rkrauss':
            self.make_folder()
            self.copy()


pres_num = 1

# first presentation
# try/except

pres1 = presentation(pres_num, 'Try/Except and Raise')

bullets2a = ['using try/except to catch and handle errors', \
             'using raise to cause errors when bad things might happen']
pres1.append_overview(bullets2a)

# link 1: http://www.tutorialspoint.com/python/assertions_in_python.htm
# link 2: http://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python
links1 = '`<http://www.tutorialspoint.com/python/assertions_in_python.htm>`_'
links2 = '`<http://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python>`_'
line2 = 'I took my assertion example idea from here:'
pres1.append_gen_slide('Good Tutorial',[links1])
pres1.append_gen_slide('Citation',[line2,'',links2])



pres1.append_github(gitroot, 'adv_py_1_try_accept_raise')
pres1.go()


# Adv. Text Processing Example
pres_num += 1

pres2 = presentation(pres_num, 'Advanced Text Processing Example')

bullets1 = ['motivate advanced Python with object-oriented text processing example', \
            'show how I would use Python with all the bells and whistles to automate my workflow', \
            'I hate repentative tasks', \
            'I would rather write Python code than create documents "by hand"', \
            'Programming is more fun than writing', \
            'Remembering what presentation I was on got annoying for intermediate Python', \
            'This guarantees consistent formatting', \
            'I think this is a cool example of the power of automated text processing']

pres2.append_overview(bullets1)

bullets2 = ['object-oriented programming','advanced text processing', \
            'work flow automation']

pres2.append_topics(bullets2)
pres2.append_github(gitroot, 'adv_py_2_advanced_text_processing_example', \
                    'slide_generator.py')
pres2.go()


