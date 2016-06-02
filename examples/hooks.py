def remote_pdb_handler(*args, **kwargs):
    # set logging to DEBUG first, then pdb
    rootLogger = logging.getLogger()

    if rootLogger.isEnabledFor(logging.DEBUG):
        import remote_pdb
        remote_pdb.set_trace()
    else:
        rootLogger.setLevel(logging.DEBUG)
        rootLogger.debug("Changed log level to DEBUG :)")


def dump_threads(*args, **kwargs):
    print >> sys.stderr, "\nDumping threads:"

    try:
        import gevent
    except ImportError:
        HAS_GEVENT = False
    else:
        HAS_GEVENT = True
        from greenlet import greenlet

    import gc

    threads = {}
    for ob in gc.get_objects():
        if (HAS_GEVENT and isinstance(ob, greenlet) and
                gevent.getcurrent() != ob):
            print >> sys.stderr, "\nGreenlet %s:" % ob
            for fname, lineno, name, line in traceback.extract_stack(
                    ob.gr_frame):
                print >> sys.stderr, 'File "%s", line %d, in %s' % (
                    fname, lineno, name)
                if line:
                    print >> sys.stderr, "  %s" % (line.strip())
        elif isinstance(ob, threading.Thread):
            threads[ob.ident] = ob

    for threadId, stack in sys._current_frames().items():
        print >> sys.stderr, "\nThread %s:" % threads[threadId]
        for fname, lineno, name, line in traceback.extract_stack(
                stack):
            print >> sys.stderr, 'File "%s", line %d, in %s' % (
                fname, lineno, name)
            if line:
                print >> sys.stderr, "  %s" % (line.strip())

    print >> sys.stderr, "\n"


def setupLogging(**kwargs):
    """Overload this and set up fault handling as well - just so that I don't
    have to go all our packages and fix it up :)
    """
    log_cfg = os.environ.get('LOG_CFG')
    if hasattr(logging, 'captureWarnings'):
        logging.captureWarnings(True)

    if log_cfg:
        logging.config.fileConfig(log_cfg)
    else:
        defaults = {
            'level': logging.DEBUG,
            'format': "%(relativeCreated)d %(levelname)s %(name)s: %(message)s"
        }
        defaults.update(kwargs)
        logging.basicConfig(**defaults)

    # signals can only be registered in the main thread
    if threading.current_thread().name.lower() == "mainthread":
        signal.signal(signal.SIGUSR1, dump_threads)
        signal.signal(signal.SIGUSR2, remote_pdb_handler)
