Title: How I do blog deployments
Date: 2015-07-30 21:00:00+00:00
Category: programming

## The Problem

Static site generators are pretty sweet.  If you're not familiar, they are more or less content management systems, but instead of generating pages on the fly like Wordpress would do, they allow you to generate a static website of your content so it can be served very quickly and with no special server software needed.  I personally use [Pelican](http://blog.getpelican.com/),  but there are others out there like the very popular [Jekyll](http://jekyllrb.com/)

The main problem I run into is that in order to write a post, I edit the post in whatever editor I choose, then regenerate the site, then deploy it.  In an effort to write more, I decided that removing resistance would be a big step in that direction.  While I like the ability to edit a post in [my editor of choice](https://www.gnu.org/software/emacs/emacs.html),  sometimes I miss the days when I ran Wordpress and could login from anywhere and start writing.  So adding a web interface to write posts is part of this.  The second part is to automate deployments.

### Ease of editing

Thankfully this one was easy. [Prose.io](http://prose.io/) is a web based editor that connects to your Github account and allows you to create or edit files in any of your repos.  Since I do use Github for my blog's repo, this part was cake.  Prose.io also provides a really nice markdown editor, which is my format of choice for writing.  Once I decide to save it, the file is added and committed in one step.  Nice!

### Deployments

This is where things get a little tricky for me.  I host this site with the wonderful folks at [Nearly Free Speech](http://www.nearlyfreespeech.net).  And while they do PHP as well other languages and frameworks,  I'm using them as a static webhost in this instance.  The problem is that I can't host my git repo there so post commit hooks are out of the question.  I might have other options here,  but in the end I would need to make sure I could install Pelican and all its dependencies as well which might be a no go.

The solution I came up with is perhaps a little convoluted, but works well given what I have at hand.  

1. I perform a push to github after writing and committing a post
2. Github fires a web-hook to another machine I have access to
3. The script the web-hook accesses drops a file in a directory
4. A cron job runs another script, and if that script finds the file created in step 3, it proceeds, and otherwise exits.
5. The script will rebuild my site, and then upload it to my webhost.

**The web-hook**

Webhooks allow you to hit a specified URL when a certain action occurs.  I won't get into detail here, as Github already has some [excellent documentation on this feature](https://developer.github.com/webhooks/). I setup mine to hit a small php script on a machine where I can more or less run and install what I like,  I set it to run on the "push" event only,  and set a secret value.  This secret allows you to make sure no one else can hit that url.  In my case however,  even if someone got the url and spammed it,  it would just cause my site to regenerate every 30 minutes.  Even so,  It's good practice to secure this stuff, so I used a random string here.  You'll need this on the next step.

**The web-hook target**

Even though I avoid PHP as much as possible,  it's great for little one off tasks like this.  This is the script I set as the target for my web-hook in the previous step:

<script src="https://gist.github.com/rsayers/0e9020f685e9c1c0dadc.js"></script>

You will of course replace "MY_SECRET_KEY" with the sercret you specified in the previous step.  Once this validates that the key is legit,  it simply creates a file, the contents are not important.

**The deployment script** 

I use cron to schedule a script that will check for the existance of that file created in the previous step, and then do a deployment when it is found

<script src="https://gist.github.com/rsayers/48fcf1136da1bb8ad38c.js"></script>

I had some issues setting up ssh keys with my host, so I'm using FTP instead.  This is dumb and you shouldn't do it... but it works so I am.  In a perfect world I would just use rsync as to not upload the entire site every time.  Most of what is in here is pretty specific to me, as you can see I use a virtual environment to keep Pelican and all its dependencies together,  but really the meat of the script is just the steps I would go through if I was doing a deployment by hand.

### The Result

In the end, I end up with a nice system that doesn't require me to do much beyond typing up a post and saving it, just like I would in a full fledged CMS.  I looked at other solutions for doing git-based deployments, and none of them worked with my exact setup, so hopefully this will be of some use if you are wreslting with the same issue.
