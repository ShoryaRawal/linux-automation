echo "installing budgie automation"
echo "created by Shorya Rawal"
echo "please enter your password where-ever asked,"
echo "Your PC will not get damaged.(press any key to start)"
read any

echo ""
echo "if nothing is happening, wait and do not panic"
echo ""

sudo add-apt-repository ppa:budgie-remix/ppa

sudo apt update
echo ""
echo "This can take some time"
echo ""
sudo apt install budgie-desktop-enviroment

echo "________________________________________________"
echo ""
echo "now, restart your computer"
echo "at the log-in screen, click on the icon at the top right corner of the password box."
echo "then you will have budgie desktop.(press any key to end)"
read any1
echo ""
echo "________________________________________________"
