# In-depth pytest 
Notes and practices used for more in-depth pytest understanding 

Notes from book: 
"Python Testing with pytest: Simple, Rapid, Effective, and Scalable, 2nd Edition" by Brian Okken

Pytest is a command line tool; a testing framework that can find written tests, run those tests, and report the results. 
- Can be extended by writing custom plugins and installing 3rd party plugins.

To practice these exercises, a sample application will be used called 'Cards.'
- Cards is meant to model the components of a modern application (API, TinyDB)


## Objectives 
Ch 1 Topics 
- virtual environment setup 
- installing pytest 
- run pytest in different ways  
- test discovery naming conventions 
- pytest all possible test outcomes  
    -> PASSED (.), FAILED (F), SKIPPED (s), XFAIL (x), XPASS (X), and ERROR (E).
- "-v" command line flag for more verbose output of your test results 
- "--tb=no" flag used to turn off tracebacks


Ch 2 Topics 
- assert rewriting allows use to use python assert expressions 
- assertion failures from fail()
- pytest.raises() test for expected exceptions
- arrange-act-assert or given-when-then structure 
- classes used to group tests 
- run small subsets of tests
- -vv and -k flags 


Ch 3 Topics
- pytest helper functions called Fixtures  
- using Fixtures for Setup and Teardown
- tracing Fixture Execution with '-setup-show'
- specifying Scope 
- sharing Fixtures through conftest.py 
- finding Where Fixtures are Defined 
- multiple Fixture Levels 
- multiple Fixtures per Test or Fixture
- deciding Fixture Scope Dynamically 
- using autouse for recurring Fixtures 
- renaming Fixtures
