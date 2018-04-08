<?php
require("db.php");
$id =$_REQUEST['id'];

$result = mysql_query("SELECT * FROM poll_options WHERE id  = '$id'");
$test = mysql_fetch_array($result);
if (!$result) 
		{
		die("Error: Data not found..");
		}
				$id=$test['id'] ;
				$title= $test['title'];

if(isset($_POST['save']))
{	
	$id_save = $_POST['id'];
	$title_save = $_POST['title'];
	$id=$_GET['id'];

	mysql_query("UPDATE poll_options SET id ='$id_save', poll_id=1, title='$title_save' WHERE id='$id'")
				or die(mysql_error()); 
	
	header("Location: index.php");			
}
mysql_close($conn);
?>

<!doctype html>
<html>
<head>
<meta charset="utf-8">

<title>Админка</title>
<link rel="stylesheet" type="text/css" href="css/sanstyle.css">
</head>

<body>
<div class="head"></div>
<div class="frm">
<div class="san">
<h3 style="text-decoration:underline;">Администрирование БД</h3>
<form name="insert" method="post" action="" >
<label>Код :</label>
<input type="text" name="id" style="margin-left:75px;"  class="txt"  value="<?php echo $id ?>"><br><br>
<label>Имя :</label>
<input type="text" name="title"  style="margin-left:70px;" class="txt" value="<?php echo $title ?>"><br><br>
<input type="submit" name="save" value="Обновить" class="sub">
</form>
</div>
</div>

<div class="foot"><br></div>
</body>
</html>