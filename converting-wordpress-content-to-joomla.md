Title: Converting Wordpress content to Joomla
Date: 2010-04-21 15:05:00+00:00
Category: programming

I'm in the middle of working on a client's site. Most of their site

is static html, but certain sections are separate Wordpress

installations so that they can manage content here.

We are building the site using Joomla and I needed to move their

existing content over. I searched a bit looking for an automated way

to do this but couldn't find exactly what I wanted. I finally did it

with a query which worked well:

  

    
    INSERT into jos_content (title,  
    alias,   
    title_alias,   
    introtext,   
    `fulltext`,   
    state,   
    sectionid,   
    mask,  
    catid,   
    created,   
    created_by,   
    created_by_alias,   
    modified,   
    modified_by,   
    checked_out,   
    checked_out_time,   
    publish_up,   
    publish_down,   
    images,   
    urls,   
    attribs,  
    version,   
    parentid,   
    ordering,   
    metakey,   
    metadesc,  
    access,   
    hits,   
    metadata)  
      
      
      
    SELECT post_title, post_name,'',replace(post_content,'  
      
    ',''),  
    '',  
    1,  
    2,  
    0,  
    2,   
    post_date,   
    62,   
    '',   
    '0000-00-00 00:00:00',  
     0,   
    0,   
    '0000-00-00 00:00:00',   
    post_date,  
     '0000-00-00 00:00:00',  
     '',  
    '',  
    'show_title=  
      
    link_titles=  
      
    show_intro=  
      
    show_section=  
      
    link_section=  
      
    show_category=  
      
    link_category=  
      
    show_vote=  
      
    show_author=  
      
    show_create_date=  
      
    show_modify_date=  
      
    show_pdf_icon=  
      
    show_print_icon=  
      
    show_email_icon=  
      
    language=  
      
    keyref=  
      
    readmore=',1,0,1,'','',0,0,'robots=' from wp_posts

  

  
  

  
A couple notes if you plan to use this: obviously the database is the

same (in this case I did an export/import on wp_posts since it was on

another server entirely) and the author, section, categories are

hard-coded. Note that it also imports the content into the introtext column,

not fulltext, so change that if needed.

It's not perfect, but it's a good 95% solution which worked pretty

well for me.

