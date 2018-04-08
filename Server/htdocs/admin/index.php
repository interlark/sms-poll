<!doctype html>
<html>
<head>
<meta charset="utf-8">

<title>Админка</title>
<link rel="stylesheet" type="text/css" href="css/sanstyle.css">
</head>

<body>
<div class="head">
<form name="clear_members" method="post" action="" >
<input type="submit" name="clear_members" value="Очистить данные участников" style="margin-top: 15px; margin-left: 20px;"></form><br>
<form name="clear_votes" method="post" action="" >
<input type="submit" name="clear_votes" value="Очистить данные голосования" style="margin-left: 20px;"></form>
</div>
<div class="frm">
<div class="san">
<h3 style="text-decoration:underline;">Администрирование БД</h3>
<form name="insert" method="post" action="" >
<label>Код :</label>
<input type="text" name="id" style="margin-left:75px;"  class="txt" ><br><br>
<label>Имя :</label>
<input type="text" name="title"  style="margin-left:70px;" class="txt"><br><br>
<input type="submit" name="submit" value="Вставить" class="sub">
</form>
    
  <?php
if (isset($_POST['submit']))
	{	   
		include 'db.php';
		
		$id=$_POST['id'];
		$title= $_POST['title'];
												
		 mysql_query("INSERT INTO poll_options(id,poll_id,title) 
		 VALUES ('$id',1,'$title')");
	}
?>

<?php
if (isset($_POST['clear_votes']))
	{	   
		include 'db.php';
												
		mysql_query("DELETE FROM poll_votes");
		echo "<script>alert('Голоса были очищены!')</script>";
	}
?>

  <?php
if (isset($_POST['clear_members']))
	{	   
		include 'db.php';
					
		mysql_query("DELETE FROM poll_options");
	}
?>	


<br><br>
<table border="1" cellpadding="10" width="750">
	<?php
	include("db.php");
	$result=mysql_query("SELECT * FROM poll_options");
	
	while($test = mysql_fetch_array($result))
	{
		$id = $test['id'];	
		echo "<tr align='center'>";	
		echo"<td><font color='black'>" .$test['id']."</font></td>";
		echo"<td><font color='black'>" .$test['title']."</font></td>";
		echo"<td> <a href ='view.php?id=$id'>Редактировать</a>";
		echo"<td> <a href ='del.php?id=$id'><center>Удалить</center></a>";
		echo "</tr>";
	}
	mysql_close($conn);
	?>
</table>

</div>
</div>

</body>
</html>