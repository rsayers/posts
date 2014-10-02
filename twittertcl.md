Title: Twitter.tcl
Date: 2008-07-05 15:40:00+00:00
Category: programming

So as an exercise to learn Tcl, I wrote a quick and dirty Twitter client. It
does require that you have Tcllib installed. Running with no arguments will
fetch your friends timeline, and running it with arguments will post said
arguments as a status update.

  
  
  
It's not polished by any means, but as I said, it was a quick exercise to get
familiar with the language before diving into a fairly large project with Sir
Havard. Anywho, here is the code.

  
  
  

  

    
    set username "YOUR_USERNAME"  
      
    set passwd "YOUR_PASSWORD"  
      
      
      
    package require base64  
      
    package require http  
      
    package require json  
      
      
      
      
      
    # Just generates the HTTP auth header we will need  
      
    proc autheader {username passwd} {  
      
        return [list "Authorization"   
      
                    [concat "Basic" [base64::encode $username:$passwd]]]  
      
    }  
      
      
      
      
      
    # post command line arguments as an update  
      
    if { $::argc > 0 } {  
      
      
      
        set postdata [::http::formatQuery status [concat $::argv]]  
      
        set req [http::geturl "http://www.twitter.com/statuses/update.xml" -headers [autheader $username $passwd] -query $postdata]  
      
        #in case you want to see the result of your post  
      
        #puts [http::data $req]  
      
        puts "Thou hast tweeted"  
      
      
      
    } else {  
      
    # otherwise, show the most recent update from your friends  
      
      
      
        set req [http::geturl "http://www.twitter.com/statuses/friends_timeline.json" -headers [autheader $username $passwd]]  
      
        set data [http::data $req]  
      
        set tweets [lreverse [json::json2dict $data]]  
      
      
      
        foreach tweet $tweets {  
      
            set user [dict get $tweet user]  
      
            set uname [dict get $user screen_name]  
      
            set text [dict get $tweet text]  
      
            puts "<$uname> $textn"  
      
        }  
      
      
      
    }

  

  
  

  
  
  
And as a side note, I've discovered that writing a twitter client is actually
a great way to get familiar with any language, especially if you intend to use
that language with any sort of web services. It forces you to pick up a few
very useful skills in whatever language you are using.

