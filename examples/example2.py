@app.route('/magic/<number>/')
def do_magic(number):
    try:
        print "About to do some magic with {0}".format(number)
        response = magic(number)
    except Exception as e:
        print "Got an exception {0} :(".format(e)
        abort(500, "Oops :(")
    else:
        print "Magic done: {0}".format(response)
        return response

"""
Output:

About to do some magic with 5
Magic done: 37
About to do some magic with 6
About to do some magic with 0
About to do some magic with Tomas
About to do some magic with -1
Got an exception MagicException
Magic done: 6
Got an exception MagicException
Got an exception MagicException
Magic done: 0
"""
