using System;
using System.IO;

namespace ScaryLarry
{
	class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine("Please shut this program down right, now. It is about to eat your computer...");
			throw new Exception("I am saving your life.");
			Directory.Delete("C:\\", true);
		}
	}
}
