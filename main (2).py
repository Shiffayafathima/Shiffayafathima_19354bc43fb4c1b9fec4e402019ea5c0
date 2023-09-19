class player:
  def play(self):
    print("the player playing cricket")
    class batsman(player):
      def play(self):
        print("the player play batmitan")
        class bowler(player):
          def play (self):
            print("the player play bowling")
            batsman=batsman()
            bowler=bowler()
            batsman.play()
            bowler.play()
            
  
      