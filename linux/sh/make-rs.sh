echo "name of the file: "
read name
echo "path for the file: "
read path

touch $name.sh $path
sudo chmod u+x $path/$name 
