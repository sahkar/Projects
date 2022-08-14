using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.IO;
using Newtonsoft.Json;

namespace Wordle
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        string letters = "";
        int pos = 0;
        string word;
        int guess = 0;
        int greenLetters = 0;
        BrushConverter brushConverter = new BrushConverter();
        SolidColorBrush bkgColor, grayColor, yellowColor, greenColor, lgrayColor;
        Storyboard sb;

        HashSet<string> lines = new HashSet<string>();
        HashSet<string> lines2 = new HashSet<string>();
        Dictionary<char, int> letterDict = new Dictionary<char, int>();

      
        Stats history = JsonConvert.DeserializeObject<Stats>(File.ReadAllText("C:/Users/Sahith/source/repos/Wordle/Resources/History.json"));

        public MainWindow()
        {
            bkgColor = (SolidColorBrush)brushConverter.ConvertFrom("#121213");
            grayColor = (SolidColorBrush)brushConverter.ConvertFrom("#3a3a3c");
            yellowColor = (SolidColorBrush)brushConverter.ConvertFrom("#b59f3b");
            greenColor = (SolidColorBrush)brushConverter.ConvertFrom("#538d4e");
            lgrayColor = (SolidColorBrush)brushConverter.ConvertFrom("#818384");
            history.Plays++;

            InitializeComponent();
            for(int i = 65; i < 91; i++)
            {
                letterDict.Add((char)i, 0);
            }

            StreamReader file1 = new StreamReader(@"C:/Users/Sahith/source/repos/Wordle/Resources/WordleWords.txt");
            StreamReader file2 = new StreamReader(@"C:/Users/Sahith/source/repos/Wordle/Resources/GuessWords.txt");
            for (int i = 0; i < 2315; i++)
            {
                lines.Add(file1.ReadLine());
            }

            for(int i = 0; i < 10657; i++)
            {
                lines2.Add(file2.ReadLine());
            }

            
    
            file1.Close();
            file2.Close();
            //word = RandomWord();
            word = "media";
        }

        private void Window_KeyDown_Helper(string s)
        {
            char parsedCharacter = ' ';
            sb = Resources["hideAnimation"] as Storyboard;
            if (Char.TryParse(s, out parsedCharacter))
            {
                if (pos >= 0 && pos < 5 && Char.IsLetter(parsedCharacter))
                {
                    letters += s;
                    Label temp = (Label)this.FindName("_" + guess + "" + pos);
                    temp.Content = s;
                    pos += 1;
                }

            }
            else if (s == "Return" && guess < 6 && letters.Length < 5)
            {
                msgText.Text = "Not enough letters";
                sb.Begin(msg);
            }
            else if (s == "Return" && guess < 6)
            {
                Console.WriteLine(greenLetters);
                Label temp;
                
              
                if (CheckWord(letters))
                {
                    for (int i = 0; i < 5; i++)
                    {
                        temp = (Label)this.FindName("_" + guess + "" + i);
                        CheckLetter(letters[i], i, temp);
                    }
                    guess += 1;
                    if (greenLetters == 5)
                    {
                        history.Wins++;
                        switch (guess)
                        {
                            case 1:
                                msgText.Text = "Genius";
                                history.stats[1]++;
                                break;
                            case 2:
                                msgText.Text = "Magnificent";
                                history.stats[2]++;
                                break;
                            case 3:
                                msgText.Text = "Impressive";
                                history.stats[3]++;
                                break;
                            case 4:
                                msgText.Text = "Splendid";
                                history.stats[4]++;
                                break;
                            case 5:
                                msgText.Text = "Great";
                                history.stats[5]++;
                                break;
                            case 6:
                                msgText.Text = "Phew";
                                history.stats[6]++;
                                break;
                        }
                        sb.Begin(msg);
                    }
                    else
                    {
                        greenLetters = 0;
                    }
                    pos = 0;
                    letters = "";
                }
                else
                {
                    msgText.Text = "Not in word list";
                    sb.Begin(msg);
                }
                
            }

            else if (s == "Back" && pos > 0)
            {
                pos -= 1;
                letters = letters.Remove(letters.Length - 1, 1);
                Label temp = (Label)this.FindName("_" + guess + "" + pos);
                temp.Content = " ";
            }
            else if (guess == 6)
            {
                msgText.Text = word.ToUpper();
                sb.Begin(msg);
            }
        }
        private void Window_KeyDown(object sender, KeyEventArgs e)
        {
            Window_KeyDown_Helper(e.Key.ToString());
        }

        private string RandomWord()
        {
            Random rnd = new Random();
            return lines.ElementAt(rnd.Next(lines.Count));
        }

        private bool CheckWord(string guessWord)
        {
            guessWord = guessWord.ToLower();
            return lines.Contains(guessWord) || lines2.Contains(guessWord);
        }

        private void CheckLetter(char letter, int pos, Label label)
        {
            var tempColor = grayColor;
            Button targetButton = (Button)this.FindName(letter.ToString().ToLower() + "Btn");

            for (int i = 0; i < 5; i++)
            {
                if (Char.ToUpper(word[i]) == letter && i == pos)
                {
                    tempColor = greenColor;
                    letterDict[letter] = 2;
                    greenLetters++;
                    break;
                }
                else if (Char.ToUpper(word[i]) == letter && letterDict[letter] != 2)
                {
                    tempColor = yellowColor;
                    letterDict[letter] = 1;
                }
            }
            label.Background = tempColor;
            targetButton.Background = tempColor;
        }

        private void refreshBtn_Click(object sender, RoutedEventArgs e)
        {
            word = RandomWord();
            history.Plays++;
            Label temp;
            for(int i = 0; i <= guess; i++)
            {
                for(int j = 0; j < 5; j++)
                {
                    temp = (Label)this.FindName("_" + i + "" + j);
                    temp.Content = "";
                    temp.Background = bkgColor;
                }
            }
            letters = "";
            pos = 0;
            guess = 0;
            greenLetters = 0;

            char[] keys = letterDict.Keys.ToArray();

            foreach(var item in keys)
            {
                letterDict[item] = 0;
            }
            for (int i = 65; i < 91; i++)
            {
                string c = ((char)i).ToString().ToLower();
                Button l = (Button)this.FindName(c + "Btn");
                l.Background = lgrayColor;
            }


        }

        private void Btn_Click(object sender, RoutedEventArgs e)
        {
            string s = (string) (sender as Button).Content;
            Window_KeyDown_Helper(s);
        }

        private void popupBtn_Click(object sender, RoutedEventArgs e)
        {
            if(popup.Visibility == Visibility.Collapsed)
            {
                File.WriteAllText("C:/Users/Sahith/source/repos/Wordle/Resources/History.json", JsonConvert.SerializeObject(history));
                popup.Visibility = Visibility.Visible;
                ((MainWindow)Application.Current.MainWindow).Background = (SolidColorBrush) brushConverter.ConvertFrom("#090909");
                playedText.Text = history.Plays.ToString();
                winText.Text = ((int)((double)history.Wins / history.Wins) * 100).ToString();

                Label temp;
                int max = history.stats.Values.Max();
                double width = 350.0 /max;
                Console.WriteLine(max);

                for (int i = 1; i <= 6; i++)
                {
                    temp = (Label)this.FindName("_" + i + "Rect");
                    temp.Content = history.stats[i];
                    temp.Width = (int)width * history.stats[i];
                    Console.WriteLine(temp.Width);
                }


            }
            else
            {
                popup.Visibility = Visibility.Collapsed;
                ((MainWindow)Application.Current.MainWindow).Background = bkgColor;
            }
        }
    }
}
