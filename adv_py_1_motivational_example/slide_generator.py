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
        fn = fn.replace(' ','_')
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
pres1 = presentation(pres_num, 'Motivational Example')

bullets1 = ['motivate advanced Python with object-oriented text processing example', \
            'show how I would use Python with all the bells and whistles to automate my workflow', \
            'I hate repentative tasks', \
            'I would rather write Python code than create documents "by hand"', \
            'Programming is more fun than writing', \
            'Remembering what presentation I was on got annoying for intermediate Python', \
            'This guarantees consistent formatting', \
            'I think this is a cool example of the power of automated text processing']

pres1.append_overview(bullets1)

bullets2 = ['object-oriented programming','advanced text processing', \
            'work flow automation']

pres1.append_topics(bullets2)
pres1.go()


# try/except
pres_num += 1

