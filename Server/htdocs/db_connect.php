<?php
    $db = @mysql_connect('localhost', 'admin', '') or die(mysql_error());
    @mysql_select_db('polls', $db) or die(mysql_error());
    @mysql_set_charset('utf8');
?>