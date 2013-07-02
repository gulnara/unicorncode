Unicorncode webb app - http://www.unicorncode.com/ :

I built this webb app over the weekend to showcase the capabilities of the unicorn language - https://github.com/gulnara/unicorn . 

*The web app is built with python using Flask.

*Tutorials are stored in posgresql database and accessed and modified via sqlalchemy.

*Authentication is built manually and sign in form is handled with wtforms.

*The tutorial text is input using markdown technique that allows styling in the front end.

*Interface is built with CSS, HTML, JS and AJAX. 

In order to make the web app interactive I used AJAX requests. The script is represented in layout.html (https://github.com/gulnara/unicorncode/blob/master/templates/layout.html#L111-L134). 

Parsing function has been modified in file parser.py (https://github.com/gulnara/unicorncode/blob/master/parser.py#L7). I had to add stdin and stdout along with StringIO (https://github.com/gulnara/unicorncode/blob/master/parser.py#L8) to let the app take the input from the user and execute code.

Going forward I will add more tutorials along with modifying them to be more educational. Also, I need to fix browser and operating system compatibility issues (you can find bugs in the bugs.txt files)