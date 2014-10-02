Title: Polyglot Programming
Date: 2009-07-09 08:06:00+00:00
Category: programming

[Polyglot](http://en.wikipedia.org/wiki/Polyglot_%28computing%29) programs are
those for which a single program is valid in two or more languages. I read
about them some time ago and think they are pretty cool, and last night while
being unable to sleep, I came up with this simple example:

  
  
  

  

    
    #include   
      
      
      
    #ifdef RUBY  
      
    def main  
      
      yield  
      
    end  
      
    #endif  
      
    main(){  
      
      printf("%s","Hello World!n");  
      
    }

  

  
  

  
  
  
It will produce the same output in C or Ruby, neat! If you are not immediately
familiar with C or Ruby, the lines which begin with a hash are parsed as
comments by Ruby. The #ifdef block will not be true, so it is ignored by the c
compiler. In the ifdef block I simply define "main" as a Ruby function.
Thankfully the c-style syntax of calling functions is valid in Ruby as well,
and printf works exactly the same. It's not as impressive as this [8 language
example](http://ideology.com.au/polyglot/polyglot.txt), but its a start.

