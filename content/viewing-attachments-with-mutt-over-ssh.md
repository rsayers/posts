Title: Viewing attachments with Mutt over ssh
Date: 2008-11-04 18:38:00+00:00
Category: programming

Mutt is my mailreader of choice. Its fast, simple, and very powerful. One
problem I had however is the fact that I view my mail exclusively from a shell
connected via ssh and this prevents me from easily viewing attachments. After
Googling the problem and not being 100% satisfied with what I found, I came up
with my own solution.

  
  
  
I have a very specific setup, so I doubt this will be of much use to anyone
else, but it might be a good place to start. I'm also not filling in a ton of
details, I assume if the reader is running mutt over ssh as their primary
client, they should be able to figure most of this out without much
explanation, but if something isn't clear, feel free to ask any questions.

  
  
  
And also, this falls within the "dirty hack" realm, I threw this together in
about 15 mintues after a friend sent me about 30 pictures via email, so I'm
aware there are better ways of doing some of the things presented here.

  
  
  
To make this work you need to be able to write to a web accessable folder and
access a database of some sort. The first bit is a script which Mutt will call
when you try to view an attachment, this will copy the file to the public
folder, and create a record in a mysql db to indicate it has not been viewed.
I named this sa.rb and made it executable from my home dir.

  
  
  

  

    
    #!/usr/local/bin/ruby                                                                                                                                          
      
    require 'rubygems'  
      
    require 'ftools'  
      
    require 'mysql'  
      
      
      
    filename=File.basename(ARGV[0]);  
      
    File.copy(ARGV[0],"/web/folder/#{filename}");  
      
    File.chmod(0777,"/web/folder/#{filename}");  
      
    my=Mysql::new("localhost","username","password","attachments")  
      
    res=my.query("INSERT into files (filename, viewed) values ('www.mysite.com/folder/#{filename}',0)")

  

  
  

  
  
  
You will also need to tell mutt to run this script for selected attachment
types, you will need to put something like this in your .mailcap file:

  
  
  

  

    
    text/*; ~/sa.rb %s  
      
    application/*; ~/sa.rb %s  
      
    image/*; ~/sa.rb %s  
      
    audio/*; ~/sa.rb %s

  

  
  

  
  
  
As you will also need to create a table in a mysql db, the schema should be
obvious from the above example however.

  
  
  
The second part is a php script which lists unviewed attachments as spits out
the list for later use:

  
  
  

  

    
    $db=mysql_connect("localhost","username","password");  
      
    mysql_select_db("attachments");  
      
    $query="SELECT * from files where viewed =0";  
      
    $rs=mysql_query($query);  
      
    if (mysql_num_rows($rs)){  
      
      while ($foo=mysql_fetch_assoc($rs)){  
      
        echo $foo['filename']."n";  
      
      }  
      
    }  
      
    mysql_query("UPDATE files set viewed=1");

  

  
  

  
  
  
This simply fetches new attachments, displays them, and them marks them as
viewed so they wont show up again.

  
  
  
And finally, the last bit runs on your client machine, it simply fetches the
above php script and feeds each url to firefox for viewing.

  
  
  

  

    
    #!/bin/bash  
      
    curl www.mysite.com/folder/index.php | xargs firefox

  

  
  

  
  
  
I saved this to a bash script which I execute from a launcher in my gnome
panel. After selecting "view attachment" in mutt, i run the script and the
image opens right up in Firefox. This obviously should work for nearly any
type of file that firefox knows how to handle.

