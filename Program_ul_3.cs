using System;
using System.Collections.Generic;

class Resident
{
    public string Name { get; set; }
    public string Address { get; set; }
    public DateTime DateOfBirth { get; set; }
}

class Programm
{
    static void Main()
    {
        Resident[] residents = new Resident[5];

        residents[0] = new Resident
        {
            Name = "Maksim Dotskin",
            Address = "kivila 4",
            DateOfBirth = new DateTime(1990, 1, 1)
        };

        residents[1] = new Resident
        {
            Name = "Artur Linder",
            Address = "kivila 5",
            DateOfBirth = new DateTime(1985, 5, 10)
        };

        residents[2] = new Resident
        {
            Name = "Bogdan Vibliy",
            Address = "kivila 4",
            DateOfBirth = new DateTime(2015, 12, 20)
        };

        residents[3] = new Resident
        {
            Name = "Olga Kyrychenko",
            Address = "kivila 10",
            DateOfBirth = new DateTime(1988, 7, 15)
        };

        residents[4] = new Resident
        {
            Name = "Marina Oleinik",
            Address = "kivila 19",
            DateOfBirth = new DateTime(2000, 3, 5)
        };

        Console.WriteLine("Sisestahe aadress:");
        string searchAddress = Console.ReadLine();
        searchAddress = searchAddress.ToLower();

        List<string> eligibleVoters = new List<string>();

        foreach (Resident resident in residents)
        {
            if (resident.Address == searchAddress && CalculateAge(resident.DateOfBirth) >= 18)
            {
                eligibleVoters.Add(resident.Name);
            }
        }

        eligibleVoters.Sort();



        bool hasResidents = false;

        foreach (string name in eligibleVoters)
        {
            hasResidents = true;
            Console.WriteLine("Ibiraatleid, kes elavad aadressil {0} ja on valimisõiguslikud:", searchAddress);
            Console.WriteLine(name);
        }

        if (!hasResidents)
        {
            Console.WriteLine("Pole Ibiraatleid, kes elavad aadressil {0}", searchAddress);
        }

    }

    static int CalculateAge(DateTime dateOfBirth)
    {
        int age = DateTime.Today.Year - dateOfBirth.Year;

        if (DateTime.Today < dateOfBirth.AddYears(age))
        {
            age--;
        }

        return age;
    }
}
