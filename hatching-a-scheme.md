Title: Hatching a Scheme
Date: 2009-09-28 12:39:00+00:00
Category: programming

I've been writing a fair amount of Scheme lately. Of the different lisps I've
used (Various versions of common lisp, arc, and emacs lisp) I find that Scheme
is a good fit for me. I especially like PLT Scheme as it runs great on all the
platforms I use (x86 Linux and PPC OSX) and has a fantastic standard library
as well as a painless third party module system.

  
  
  
I've started out by working some of the [Project
Euler](http://projecteuler.net/) problems. Having nearly no built-in iterators
has been challenging has forced me to really think recursively. It initially
felt like I was writing an awful lot of code I wouldn't have to write in other
languages. Generating a list of consecutive numbers for a given range is one
of them. In Ruby it would be a simple matter of:

  

  

    
    (1..100).to_a

  

  
  
  
to get an array of all numbers from 1 to 100. I could find no such function in
Scheme, and ended up having to write it like this:

  

  

    
    (define (buildlist start n l)  
      
        (cond  
      
         ((> start n) l)  
      
         (else (buildlist  start (- n 1) (cons n l)))))  
      
      
      
    (define (list-from-range start end)  
      
      (buildlist start end '()))

  

  
  

  
  
  
Once that was done however, I had a very compact way to accomplish what I
needed, and it could be reused for several other problems. Problem #1 is "Find
the sim of all the multiple of 3 or 5 below 1000".

  
  
  
My solution was this:

  

  

    
    (display  
      
       (apply +  
      
              (filter  
      
               (lambda (n)  
      
                 (cond  
      
                  ((= 0 (modulo n 3)) #t)  
      
                  ((= 0 (modulo n 5)) #t)  
      
                  (else #f)))  
      
               (list-from-range 1 999))))

  

  
Once you can wrap your head around the look of the language, the solution is
quite readable.

  
  
  
Skipping ahead a bit, problem 6 reads "Find the difference between the sum of
the squares of the first one hundred natural numbers and the square of the
sum."

  

    
    (define (sqr n) (* n n))  
      
      
      
    (define l (list-from-range 1 100))  
      
    (display (-  
      
     (sqr (apply + l))  
      
     (apply + (map sqr l))))

  

  
  
  
While I am certainly new to the language, I'm pleased with how elegant these
solutions can be.

  
  
  
From a more practical standpoint, today on [Hacker
News](http://news.ycombinator.com/) a members posted a link to a [Python
library](http://www.catonmat.net/blog/python-library-for-google-translate/) to
interface with Google Translate. I decided to try my hand a Scheme version:

  
  
  

  

    
    (require net/url)  
      
    (define (gtranslate txt from to)  
      
      (define url (string-append "http://translate.google.com/translate_t?prev=hp&hl=en&js=y&text=" txt "&file=&sl=" from" &tl=" to "&history_state0=#"))  
      
      (last (regexp-match #rx"
    
    (.*)
    
    " (read-string 50000(get-pure-port (string->url url))))))

  

  
It's not as robust as the python version, but it does the same basic job with
very little code. Neat!

