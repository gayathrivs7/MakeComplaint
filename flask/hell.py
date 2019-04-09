{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "\n",
    "\n",
    "app =  Flask(__name__)\n",
    "\n",
    "@app.route('/hell/<name>')#route,filename,variable\n",
    "def hello_name(name):\n",
    "    return 'Hello %s' % name\n",
    "if __name__=='__main__':\n",
    "    app.run()\n",
    "    \n",
    "    #open the browser and type http://localhost:5000/hell/TutorialsPoint."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/flask')\n",
    "def show_f():\n",
    "    return 'hello flask'\n",
    "\n",
    "@app.route('/python/')\n",
    "def show_p():\n",
    "    return 'hello python'\n",
    "if __name__=='__main__':\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: Do not use the development server in a production environment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [09/Apr/2019 13:04:07] \"GET /user/gayathri HTTP/1.1\" 302 -\n",
      "127.0.0.1 - - [09/Apr/2019 13:04:07] \"GET /guest/gayathri HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [09/Apr/2019 13:04:17] \"GET /user/gayathri HTTP/1.1\" 302 -\n",
      "127.0.0.1 - - [09/Apr/2019 13:04:17] \"GET /guest/gayathri HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [09/Apr/2019 13:04:23] \"GET /user/admin HTTP/1.1\" 302 -\n",
      "127.0.0.1 - - [09/Apr/2019 13:04:23] \"GET /admin HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "\n",
    "#redirecting\n",
    "\n",
    "from flask import Flask,redirect,url_for\n",
    "\n",
    "app =Flask(__name__)\n",
    "\n",
    "@app.route('/admin')\n",
    "def hello_admin():\n",
    "    return 'hello admin'\n",
    "\n",
    "@app.route('/guest/<guest>')\n",
    "def hello_guest(guest):\n",
    "    return 'hello %s as guest' % guest\n",
    "\n",
    "@app.route('/user/<name>')\n",
    "def hello_user(name):\n",
    "    if name=='admin':\n",
    "        return redirect(url_for('hello_admin'))\n",
    "    else:\n",
    "        return redirect(url_for('hello_guest',guest=name))\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
