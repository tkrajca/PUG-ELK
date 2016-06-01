import logging
logging.basicConfig(level=logging.DEBUG)

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

DEBUG:root:About to do some magic with 0
ERROR:root:Got an exception MagicException :(
Traceback (most recent call last):
  File "/tmp/bla.py", line 8, in <module>
    raise ValueError('MagicException')
ValueError: MagicException
DEBUG:root:About to do some magic with 1
DEBUG:root:About to do some magic with 2
INFO:root:Magic done: 1
INFO:root:Magic done: 2
"""
