import wsgiref.simple_server
import urllib.parse
import sqlite3
import http.cookies
import random

connection = sqlite3.connect('users.db')
stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
cursor = connection.cursor()
result = cursor.execute(stmt)
r = result.fetchall()
if (r == []):
    exp = 'CREATE TABLE users (username,password)'
    connection.execute(exp)


def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    un = params['username'][0] if 'username' in params else None
    pw = params['password'][0] if 'password' in params else None

    if path == '/register' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ?', [un]).fetchall()
        if user:
            start_response('200 OK', headers)
            return ['Sorry, username {} is taken'.format(un).encode()]
        else:
            start_response('200 OK', headers)
            connection.execute('INSERT INTO users VALUES (?, ?)', [un, pw])
            connection.commit()
            return ['''
            Username Registered
            <!DOCTYPE html><a href="/account">Account</a>'''.encode()]

    elif path == '/login' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()
        if user:
            headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
            start_response('200 OK', headers)
            return ['User {} successfully logged in. <a href="/account">Account</a>'.format(un).encode()]
        else:
            start_response('200 OK', headers)
            return ['Incorrect username or password'.encode()]

    elif path == '/logout':
        headers.append(('Set-Cookie', 'session=0; expires=Thu, 01 Jan 1970 00:00:00 GMT'))
        start_response('200 OK', headers)
        return ['Logged out. <a href="/">Login</a>'.encode()]

    elif path == '/account':
        start_response('200 OK', headers)

        if 'HTTP_COOKIE' not in environ:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])
        if 'session' not in cookies:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        [un, pw] = cookies['session'].value.split(':')
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()

        #This is where the game begins. This section of is code only executed if the login form works, and if the user is successfully logged in
        if user:
            correct = 0
            wrong = 0

            cookies = http.cookies.SimpleCookie()
            if 'HTTP_COOKIE' in environ:
                cookies.load(environ['HTTP_COOKIE'])
                if 'score' in cookies:
                    [correct, wrong] = cookies['score'].value.split(':')
                    correct = int(correct)
                    wrong = int(wrong)


            page = '<!DOCTYPE html><html><head><title>Multiply with Score</title></head><body>'
            if 'factor1' in params and 'factor2' in params and 'answer' in params:
                factor1 = params['factor1'][0]
                factor2 = params['factor2'][0]
                answer = params['answer'][0]
                correct_answer = int(factor1)*int(factor2)

                if (answer==str(correct_answer)):
                    page=page+'<h1 style="background-color: lightgreen">Correct, {} x {} = {}'.format(factor1, factor2, answer)
                    correct+=1
                else:
                    page=page+'<h1 style="background-color: red">Wrong, {} x {} = {}'.format(factor1, factor2, correct_answer)
                    wrong+=1

            elif 'reset' in params:
                correct = 0
                wrong = 0

            headers.append(('Set-Cookie', 'score={}:{}'.format(correct, wrong)))

            f1 = random.randrange(10) + 1
            f2 = random.randrange(10) + 1

            page = page + '<h1>What is {} x {}</h1>'.format(f1, f2)

            answer = [f1*f2, random.randrange(100), random.randrange(100), random.randrange(100)]
            options = ['A', 'B', 'C', 'D']
            random.shuffle(answer)

            #   [INSERT CODE HERE. Create the 4 answer hyperlinks here using string formatting.]
            for i in range(len(answer)):
                hyperlink = f'<a href="/account?username={un}&amp;password={pw}&amp;factor1={f1}&amp;factor2={f2}&amp;answer={answer[i]}">{options[i]}: {answer[i]}</a><br>'
                page = page + hyperlink

            page += '''<h2>Score</h2>
            Correct: {}<br>
            Wrong: {}<br>
            <a href="/account?reset=true">Reset</a></br>
            <h2><a href="/logout?reset=true">Logout</a></h2>
            </body></html>'''.format(correct, wrong)

            return [page.encode()]
        else:
            return ['Not logged in. <a href="/">Login</a>'.encode()]

    elif path == '/':
        start_response('200 OK', headers)
        page = ''' <!DOCTYPE html>
                        <html>
                         <form action="/login" style="background-color:gold">
                            <h1>Login</h1>
                            Username <input type="text" name="username"><br>
                            Password <input type="password" name="password"><br>
                            <input type="submit" value="Log in">
                        </form>
                        <form action="/register" style="background-color:gold">
                            <h1>Register</h1>
                            Username <input type="text" name="username"><br>
                            Password <input type="password" name="password"><br>
                            <input type="submit" value="Register">
                        </form>
                        </html>'''

        return [page.encode()]

    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 5999, application)
httpd.serve_forever()