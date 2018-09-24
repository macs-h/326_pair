using System;
using System.Collections.Generic;

namespace AntsOnAPlane
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<char, (string dir, string nState)> dnaDict = new Dictionary<char, (string, string)>();
            string input = "start";
            int maxSteps= 0;
            bool firstLine = true;
            char defaultSym = ' ';
            while (input != ""){
                input = Console.ReadLine();
                if(input.Length == 1){
                    //the final int showing steps
                    maxSteps = int.Parse(input);
                    input = ""; //so will end input (count is the last thing they give)
                }else if(input[0] != '#'){
                    //# comments will be skipped over
                    string[] parsedIn = input.Split(' '); //seperates input into 3 parts, symbol, direction to go, what symbol to change
                    dnaDict.Add(char.Parse(parsedIn[0]),(parsedIn[1], parsedIn[2]));
                    if(firstLine){
                        defaultSym = char.Parse(parsedIn[0]);
                        firstLine = false;
                    }
                }
            }

            Ant ant = new Ant(dnaDict, defaultSym);
            int currentStep = 0;
            (int x, int y) currentPos = (0,0);
            while(currentStep < maxSteps){
                currentPos = ant.move(currentPos);
                currentStep+=1;
            }
            Console.WriteLine("CurrentPos = x: {0} y: {1}", currentPos.x, currentPos.y);
        }
    }
}
