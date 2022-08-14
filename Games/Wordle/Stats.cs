using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Wordle
{
    internal class Stats
    {
        int wins;
        int plays;
        public Dictionary<int, int> stats = new Dictionary<int, int>()
        {
            {1, 0},
            {2, 0},
            {3, 0},
            {4, 0},
            {5, 0},
            {6, 0},

        };

        public int Wins { get; set; }
        public int Plays { get; set; }
    }
}
