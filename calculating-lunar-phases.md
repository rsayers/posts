Title: Calculating Lunar Phases
Date: 2007-12-13 20:32:00+00:00
Category: programming

I've always been curious about how lunar phases are calculated and finally got
around to looking it up. I found a great guide
[here](http://ruyeyama.best.vwh.net/rage/auspice.html)

  
  
  
There is a period of time called a Synodic Month, which is the period of time
the moon takes to complete all phases (i.e. the time it takes for one new moon
to the next), this period is 29.5306 days. Knowing this, all one needs to do
is find a date where a new moon has occurred as a reference. Next, take your
target date, subtract this from your reference date. The remainder of the
absolute value of this is what we need. You will need to calculate the amount
of days from this, this is done by simply multiplying the value by 29.5306 and
subtract the product from 29.5306. The result will tell you what you want to
know.

  
  
  
  
  
New - 0

  
Crescent (waxing) - 3.69

  
Half (waxing) - 7.38

  
Gibbous (waxing) - 11.07

  
Full - 14.77

  
Gibbous (waning) - 18.46

  
Half (waning) - 22.15

  
Crescent (waning) - 25.84

  
New - 29.53

  
  
  
Below is a ruby program I wrote which does this calculation for you. It seems
to be accurate from spot checks I've done, but I've read that it may have
inaccuracies due to not taking the moons elliptical orbit into account.

  
  
  
  
  

  

    
    require 'date'  
      
      
      
    # Enter a target date, this will print the current moon phase  
      
    target_date = DateTime.parse('December 13 2007')  
      
      
      
    class Phase  
      
      attr_accessor :name, :index  
      
      def initialize(name,index)  
      
        @name=name  
      
        @index=index  
      
      end  
      
    end  
      
      
      
    class Numeric  
      
      def between?(x,y)  
      
        self > x && self < y  
      
      end  
      
    end  
      
      
      
    phases = Array.new  
      
    phases << Phase.new('New',0)  
      
    phases << Phase.new('Crescent (waxing)',3.69)  
      
    phases << Phase.new('Half (waxing)',7.38)  
      
    phases << Phase.new('Gibbous (waxing)',11.07)  
      
    phases << Phase.new('Full',14.77)  
      
    phases << Phase.new('Gibbous (waning)',18.46)  
      
    phases << Phase.new('Half (waning)',22.15)  
      
    phases << Phase.new('Crescent (waning)',25.84)  
      
    phases << Phase.new('New',29.53)  
      
      
      
      
      
    Synodic_month = 29.5306  
      
    nm_date = DateTime.parse('January 8 2008')  
      
    difference = (target_date - nm_date).abs  
      
    hours,minutes,seconds,frac = DateTime.day_fraction_to_time(difference)  
      
    days_diff=hours/24  
      
    m,r=days_diff.divmod(Synodic_month)  
      
    x=Synodic_month-r  
      
      
      
    last_phase=phases[0]  
      
    phases.each do |phase|  
      
      if x.between?(last_phase.index,phase.index) then  
      
        if x-last_phase.index < phase.index-x then  
      
          puts last_phase.name  
      
        else  
      
          puts phase.name  
      
        end  
      
      end  
      
      last_phase = phase  
      
    end

  

