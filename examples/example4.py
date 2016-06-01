import logging.config
logging.config.fileConfig("logging.ini")

@app.route('/magic/<number>/')
def do_magic(number):
    try:
        logging.debug("About to do some magic with {0}".format(number))
        response = magic(number)
    except Exception as e:
        logging.exception("Got an exception {0} :(".format(e))
        abort(500, "Oops :(")
    else:
        logging.info("Magic done: {0}".format(response))
        return response

"""
Output:

2016-06-01 22:23:41,549 DEBUG example4 root PID: 7179  About to do some magic with 0
2016-06-01 22:23:41,549 ERROR example4 root PID: 7179  Got an exception MagicException :(
Traceback (most recent call last):
  File "/tmp/bla.py", line 8, in <module>
    raise ValueError('MagicException')
ValueError: MagicException
2016-06-01 22:23:41,549 DEBUG example4 root PID: 7179  About to do some magic with 1
2016-06-01 22:23:41,550 DEBUG example4 root PID: 7179  About to do some magic with 2
2016-06-01 22:23:41,549 INFO example4 root PID: 7179  Magic done: 1
2016-06-01 22:23:41,550 INFO example4 root PID: 7179  Magic done: 2
"""
