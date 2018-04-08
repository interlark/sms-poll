<?php
    include_once ('db_connect.php');
	include_once ('functions.php');
	
		//обращаемся не через фронтенд
		//вызываем из гейтвея
        if (isset($_POST['poll']) and isset($_POST['option']) and isset($_POST['number'])){
            $poll_id = intval($_POST['poll']);
            $option_id = intval($_POST['option']);
            $number = $_POST['number'];
			
            add_vote($option_id, $poll_id, $number);
            
            exit(json_encode(array('results' => results($poll_id))));
        }
?>