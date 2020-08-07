echo "File name: "
read name
echo "File Type(txt, py): "
read Type
echo "Path: "
read Path

touch $name.$Type $Path
