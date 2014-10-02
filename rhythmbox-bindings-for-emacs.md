Title: Rhythmbox Bindings for Emacs
Date: 2008-11-06 14:40:00+00:00
Category: emacs

Some quick bindings I threw together for controlling RhythmBox from within
Emacs. I bound them to the nav keys since I use the normal emacs bindings for
these functions anyhow.

  
  
  

  

    
    (defun rhythmbox-next ()   
      
      (interactive)  
      
      (shell-command "rhythmbox-client --next"))  
      
      
      
    (defun rhythmbox-prev ()   
      
      (interactive)  
      
      (shell-command "rhythmbox-client --prev"))  
      
      
      
    (defun rhythmbox-play-pause ()   
      
      (interactive)  
      
      (shell-command "rhythmbox-client --play-pause"))  
      
      
      
    (defun rhythmbox-vol-up ()   
      
      (interactive)  
      
      (shell-command "rhythmbox-client --volume-up"))  
      
      
      
    (defun rhythmbox-vol-down ()   
      
      (interactive)  
      
      (shell-command "rhythmbox-client --volume-down"))  
      
      
      
    (global-set-key [insert] 'rhythmbox-play-pause)  
      
    (global-set-key [delete] 'rhythmbox-prev)  
      
    (global-set-key [end] 'rhythmbox-next)  
      
    (global-set-key [prior] 'rhythmbox-vol-up)  
      
    (global-set-key [next] 'rhythmbox-vol-down)

  

