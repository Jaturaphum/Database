using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Media;

namespace Pro.Coin
{
    public partial class Form1 : Form
    {
        NetworkHelper con = new NetworkHelper("192.168.10.100");
        public Form1()
        {
            InitializeComponent();
        }
        

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void baht1_Click(object sender, EventArgs e)
        {
            string path = "/reset_stack_coin";
            string para = "id=1";

            var data = con.getData(path, para);
            if (data != null)
            {
                string a = data[0]["stack_coin"];
                B_1.Text = a;
            }

        }

        private void B_1_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void B_2_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void B_5_TextChanged(object sender, EventArgs e)
        {
            

        }

        private void B_10_TextChanged(object sender, EventArgs e)
        {
            

        }

        private void C_T_TextChanged(object sender, EventArgs e)
        {
            

        }

        private void M_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void baht2_Click(object sender, EventArgs e)
        {

        }

        private void baht5_Click(object sender, EventArgs e)
        {
            string path = "/reset_stack_coin";
            string para = "id=2";

            var data = con.getData(path, para);
            if (data != null)
            {
                string a = data[0]["stack_coin"];
                
                B_5.Text = a;
                
            }
        }

        private void baht10_Click(object sender, EventArgs e)
        {
            string path = "/reset_stack_coin";
            string para = "id=3";

            var data = con.getData(path, para);
            if (data != null)
            {
                string a = data[0]["stack_coin"];
                B_10.Text = a;
            }
        }

        private void bahtAll_Click(object sender, EventArgs e)
        {
            string path = "/reset_stack_coin_all";
            string para = "";

            var data = con.getData(path, para);
            if (data != null)
            {
                string a = data[0]["stack_coin"];
                B_1.Text = a;
                B_5.Text = a;
                B_10.Text = a;
                C_T.Text = a;
                M.Text = a;

            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string path = "/show_stack_all";
            string para = "";

            var data = con.getData(path, para);
            if (data != null)
            {
                string a = data[0]["stack_coin"]; // 1bath
                string b = data[1]["stack_coin"]; // 5bath
                string c = data[2]["stack_coin"]; // 10bath
                B_1.Text = a;
                B_5.Text = b;
                B_10.Text = c;
                int B1 = 1;
                int B2 = 5;
                int B3 = 10;
                int total = int.Parse(a) + int.Parse(b) + int.Parse(c);
                C_T.Text = total.ToString();
                int mtotal = int.Parse(a)*1 + int.Parse(b)*5 + int.Parse(c)*10;
                M.Text = mtotal.ToString();



            }
            for (int i = 0; i < data.Count; i++)
            {
                Console.WriteLine();
            }
        }

        private void label8_Click(object sender, EventArgs e)
        {

        }
    }
}
