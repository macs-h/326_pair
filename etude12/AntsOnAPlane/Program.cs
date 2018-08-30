using System;
using System.Collections.Generic;

namespace AntsOnAPlane
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<char, (string dir, string nState)> dnaDict = new Dictionary<char, (string, string)>();
            string input =  Console.ReadLine();
            //--------need to do reading input etc----------
            //check the input first
            string[] parsedIn = input.Split(' '); //seperates input into 3 parts, symbol, direction to go, what symbol to change
            dnaDict.Add(char.Parse(parsedIn[0]),(parsedIn[1], parsedIn[2]));
            int maxSteps= 5;



            Ant ant = new Ant(dnaDict, 'x');
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
