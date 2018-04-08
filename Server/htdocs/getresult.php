<?php
    include_once ('db_connect.php');
	include_once ('functions.php');
	
    exit(json_encode(array('results' => results2(1))));
?>