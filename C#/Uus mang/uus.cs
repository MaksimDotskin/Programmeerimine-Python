using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Uss_mang

class uss
{
    public int 

        
    



}



class ekraan
{





}


















    class Program
    {
        static void Main(string[] args)
        {
            int ekr_laius = 40;
            int ekr_korgus = 20;
            int skoor = 0;
            int mangu_kiir = 100;
            int suunas = 0; 

            Random Random_arv = new Random();
            Position toit = new Position(Random_arv.Next(0, ekr_laius), Random_arv.Next(0, ekr_korgus));
            if (toit.x == 0)
                toit.x++;
            if (toit.y == 0)
                toit.y++;
            List<int> snakeX = new List<int>() { 0 };
            List<int> snakeY = new List<int>() { 0 };
            int uss_pikkus = 1;

            while (true)
            {
                if (Console.KeyAvailable)
                {
                    ConsoleKeyInfo userInput = Console.ReadKey();
                    switch (userInput.Key)
                    {
                        case ConsoleKey.RightArrow:
                            if (suunas != 2) suunas = 0;
                            break;
                        case ConsoleKey.DownArrow:
                            if (suunas != 3) suunas = 1;
                            break;
                        case ConsoleKey.LeftArrow:
                            if (suunas != 0) suunas = 2;
                            break;
                        case ConsoleKey.UpArrow:
                            if (suunas != 1) suunas = 3;
                            break;
                    }
                }

                Position uss_pea = new Position(snakeX[0], snakeY[0]);
                if (suunas == 0) uss_pea.x++;
                if (suunas == 1) uss_pea.y++;
                if (suunas == 2) uss_pea.x--;
                if (suunas == 3) uss_pea.y--;

                if (uss_pea.x < 0 || uss_pea.x >= ekr_laius || uss_pea.y < 0 || uss_pea.y >= ekr_korgus)
                {
                    break;
                }

                if (snakeX.Contains(uss_pea.x) && snakeY.Contains(uss_pea.y))
                {
                    break;
                }

                if (uss_pea.x == toit.x && uss_pea.y == toit.y)
                {
                    skoor++;
                    uss_pikkus++;
                    mangu_kiir--;

                    toit = new Position(Random_arv.Next(0, ekr_laius), Random_arv.Next(0, ekr_korgus));
                    if (toit.x == 0)
                        toit.x++;
                    if (toit.y == 0)
                        toit.y++;
                }

                snakeX.Insert(0, uss_pea.x);
                snakeY.Insert(0, uss_pea.y);

                if (snakeX.Count > uss_pikkus)
                {
                    snakeX.RemoveAt(snakeX.Count - 1);
                    snakeY.RemoveAt(snakeY.Count - 1);
                }

                Console.Clear();
                for (int i = 0; i < snakeX.Count; i++)
                {
                    Console.SetCursorPosition(snakeX[i], snakeY[i]);
                    Console.Write("*");
                }

                Console.SetCursorPosition(toit.x, toit.y);
                Console.Write("@");

                Console.SetCursorPosition(ekr_laius / 2 - 4, 0);
                Console.Write("Snake Game");

                Console.SetCursorPosition(ekr_laius / 2 - 4, 1);
                Console.Write("Score: " + skoor);

                Thread.Sleep(mangu_kiir);
            }
        }
    }

    struct Position
    {
        public int x;
        public int y;
        public Position(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
    }
}
