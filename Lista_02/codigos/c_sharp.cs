using System;

// O(n)
// Programa q itera pela variavel n e retorna todos os numeros pares. 
class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("digite um valor para n");
        int n = Int32.Parse(Console.ReadLine());
        int i = 0;
        while (i < n)
        {
            i++;
            if (i % 2 == 0)
                continue;
            Console.WriteLine(i);
        }
    }
}