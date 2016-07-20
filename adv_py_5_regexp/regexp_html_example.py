html_str = '''<a href="http://www.siue.edu"><img alt="Southern Illinois University Edwardsville Logo" height="50" src="http://www.siue.edu/_files/images/logo-edwardsville.png" width="271" /></a>
    </div><!--/Logo--> 

    <!--Begin Apply--><div class="btnApply">
    <a href="http://www.siue.edu/apply/" style="color: white; text-decoration: none;">Apply to SIUE</a></div><!--/Apply-->
'''

import re

p1 = re.compile(r'<a href="(.*?)"')
q1 = p1.search(html_str)

