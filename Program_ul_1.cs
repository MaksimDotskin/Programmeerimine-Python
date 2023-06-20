using System;

class Programm
{
    static void Main()
    {
      
        int[] numbers = new int[9];

        Random random = new Random();

        for (int i = 0; i < numbers.Length; i++)
        {
            numbers[i] = random.Next(0,101); 
        }

        Console.WriteLine("Arvad:");

        for (int i = 0; i < numbers.Length; i++)
        {
            Console.WriteLine(numbers[i]); 
        }




        bool isAscending = true;
        bool isDescending = true;

        for (int i = 1; i < numbers.Length; i++)
        {
            if (numbers[i] < numbers[i - 1])
            {
                isAscending = false;
            }
            if (numbers[i] > numbers[i - 1])
            {
                isDescending = false;
            }
        }

        if (isAscending)
        {
            Console.WriteLine("Massiiv on tõusvas järjekorras.");
        }
        else if (isDescending)
        {
            Console.WriteLine("Massiiv on kahanevas järjekorras.");
        }
        else
        {
            Console.WriteLine("Massiiv ei ole järjestatud.");
        }
    }
}

