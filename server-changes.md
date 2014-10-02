Title: Server Changes
Date: 2009-07-24 09:36:00+00:00
Category: computing

Last night, while attempting to install php5-mgsql, I managed to hose php and
apache. Sometimes apt-get just will not work.

  
  
  
I've been wanting to switch from Apache to Nginx anyhow, so I figured now
would be the best time. It took a few hours, but this machine now serves web
pages via Nginx and PHP5.3. In addition I installed APC to speed up php sites.

  
  
  
This page is now server with a Fast-CGI wrapper, I think it might actually be
a bit slower than the old Apache/Mod_Ruby setup, but mod_ruby is rarely used,
so it's not a horrible idea to work on getting the site workable with other
methods.

