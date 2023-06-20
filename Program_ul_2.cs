using System;

class Programm
{
    static void Main()
    {
        Random random = new Random();
        int[] numbers = new int[100];

        int count = 0;

        for (int i = 0; i < numbers.Length; i++)
        {
            numbers[i] = random.Next(-20, 21);

            if (numbers[i] < -10 || numbers[i] > 10)
            {
                count++;
            }
        }

        Console.WriteLine($"Väljaspool vahemikku [-10, 10] on {count} elementi.");
    }
}

