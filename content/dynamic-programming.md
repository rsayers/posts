Title: Dynamic Programming
Date: 2011-04-22 02:51:00+00:00
Category: programming
Tags: scheme, programming
Tonight my roommate mentioned dynamic programming to me.  For those who can't
be bothered the click the link, the gist of the concept is that recursive
functions, or functions that otherwise may have to compute the same arguments
over and over can use their arguments as a key to cache the results so they
don't have to compute it multiple times.  Simple and useful.

I decided to hack out a quick implmentation in scheme:

    
    (define lambda-cache (make-hash-table))
    
    (define (add-to-cache args)
      (let ((fn (car args))
            (a (cadr args)))
        (hash-table-set! lambda-cache args (fn a))
        (hash-table-ref lambda-cache args)))
    
    (define (dynamic-call . args)
      (cond ((hash-table-exists? lambda-cache args) (hash-table-ref lambda-cache  args))
            (#t (add-to-cache args))))
    
    
    
    ; Normal naive fibonacci sequence
    (define (fib n)
      (cond ((< n 2) n)
            (#t (+ (fib (- n 1)) (fib (- n 2))))))
    
    
    
    ; using dynamic-call
    (define (fib n)
      (cond ((< n 2) n)
            (#t (+ (dynamic-call fib (- n 1)) (dynamic-call fib (- n 2))))))
  

As you can see it's super simple, it keeps a global cache which uses a list of
a function and it's arguments as the key, and the return value as the value.
The nice this is you can wrap pretty much any function and it just works.  I
timed the first 35 terms of the fibonacci sequence.  The normal version took
19 seconds, the dynamic version? 23ms!  Quite the difference.

