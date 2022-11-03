# In depth pytest 
Notes from book: 
"Python Testing with pytest: Simple, Rapid, Effective, and Scalable, 2nd Edition" by Brian Okken

Pytest is a command line tool; a testing framework that can find written tests, run those tests, and report the results. 
- Can be extended by writing custom plugins and installing 3rd party plugins.

To practice these exercises, a sample application will be used called 'Cards.'
- Cards is meant to model the components of a modern application (API, TinyDB)


Ch 1 Review 
- virtual environment setup 
- installing pytest 
- run pytest in different ways  
- test discovery naming conventions 
- pytest all possible test outcomes  
    -> PASSED (.), FAILED (F), SKIPPED (s), XFAIL (x), XPASS (X), and ERROR (E).
- "-v" command line flag for more verbose output of your test results 
- "--tb=no" flag used to turn off tracebacks