<?php
$conn=@mysql_connect('localhost','admin','') or die(mysql_error());
@mysql_select_db("polls", $conn);
@mysql_set_charset('utf8');
?>