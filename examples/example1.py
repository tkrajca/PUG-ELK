@app.route('/magic/<number>/')
def do_magic(number):
    try:
        response = magic(number)
    except:
        abort(500, "Oops :(")
    else:
        return response

"""
Output:
"""
