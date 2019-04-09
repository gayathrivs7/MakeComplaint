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
    "    return"
   ]
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
