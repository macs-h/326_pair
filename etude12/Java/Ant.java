import System;
import System.Collections.Generic;
public class Tuple<X, Y> { 
    public final X x; 
    public final Y y; 
    public Tuple(X x, Y y) { 
      this.x = x; 
      this.y = y; 
    } 
  } 
    public class Ant
    {
        private Dictionary<char, (string dir, string nState)> dna = new Dictionary<char, (string dir, string nState)>();
        private Dictionary< Tuple<X, Y>, char> plane = new Dictionary<Tuple<X, Y>, char>(); //key: position, vlaue: if it has been visited the state

        private int lastPos = 0; 
        private char defaultSym;


        //Constructor
        public Ant(Dictionary<char, (string dir, string nState)> dna, char defaultSym)
        {
            this.dna = dna;
            this.defaultSym = defaultSym;
        }

        public Tuple<X,Y> move(Tuple<X, Y> currentPos){
            char nextpos = 'S';
            if(plane.ContainsKey(currentPos)){
                //has already been walked over
                (string dir, string nState) dnaResult = dna[plane[currentPos]]; //dont need to check because plane[currentpos] will only return valid symbol coz it was set

                
                nextpos = dnaResult.dir[lastPos]; //where to go next
                plane[currentPos] = dnaResult.nState[lastPos]; //changes plane state accordingly
            }else{
                //state hasn't been visited before
                (string dir, string nState) dnaResult = dna[defaultSym];
                nextpos = dnaResult.dir[lastPos]; //where to go next
                plane.Add(currentPos,dnaResult.nState[lastPos]); //changes plane state accordingly
            }
            

            return getNewPos(nextpos, currentPos);
        }

        private (int, int) getNewPos(char dir, (int x, int y) currentPos){
            (int x,int y) newPos = (0,0);
            switch (dir)
            {
                case 'N':
                    //moving north
                    newPos.x = currentPos.x;
                    newPos.y = currentPos.y+1;
                    lastPos = 0;
                    break;
                case 'E':
                    //moving east
                    newPos.x = currentPos.x+1;
                    newPos.y = currentPos.y;
                    lastPos = 1;
                    break;
                case 'S':
                    //moving south
                    newPos.x = currentPos.x;
                    newPos.y = currentPos.y-1;
                    lastPos = 2;
                    break;
                case 'W':
                    //moving north
                    newPos.x = currentPos.x-1;
                    newPos.y = currentPos.y;
                    lastPos = 3;
                    break;
                default:
                    Console.WriteLine("Direction not valid");
                    break;
            }
            return newPos;
        }
    }
}
