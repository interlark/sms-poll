<?php
    include_once ('db_connect.php');
	include_once ('functions.php');
    
    if (!@mysql_ping()) 
    {
        if (isset($_GET['check'])){
            $resp = array ('dbconn'=>false);
            header('Content-Type: application/json');
            exit(json_encode($resp));
        }
        else {
            exit('db not connected');
        }
    }

    if (isset($_GET['check'])){
            $resp = array ('dbconn'=>true);
            header('Content-Type: application/json');
            exit(json_encode($resp));
    }

    $id = (isset($_GET['id'])) ? intval($_GET['id']) : 1;

    if(!$row = get_poll($id)){
        exit('not found');
    }
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru">

<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title>Голосование ПГНИУ</title>
    <script type="text/javascript" src="lib/jquery.min.js"></script>
    <script type="text/javascript" src="lib/awcore.polls.js"></script>
    <!-- delete this if you have the jquery ui -->
    <script type="text/javascript" src="lib/backgroundColor.js"></script>

    <link href="lib/polls.css" rel="stylesheet" type="text/css" />
</head>

<body>

<div id="<?php echo $row['poll_id'];?>" class="polls">
    <!-- <h2><?php echo $row['title'];?></h2> -->
	<form method="post" id="poll_form">
        <table>
		
		<tr>
		
		<!--code-->
		<td width="80px">№</td>
		
		<!--name-->
		<td width="255px">Участница</td>
		
		<!--votes-->
		<td width="80px">Голоса</td>
		
		<!--bar-->
		<td width="310px"></td>
		</tr>
		<?php
            foreach (poll_options($id) as $option) {
        ?>
		<tr>
		
		<!--code-->
		<td width="80px">
		<?php echo $option['id'];?>
		</td>
		
		<!--name-->
		<td width="255px">
		<?php echo $option['title'];?>
		</td>
		
		<!--votes-->
		<td width="80px" id="vote_<?php echo $option['id'];?>">
		<?php echo $option['rates'];?>
		</td>
		
		<!--bar-->
		<td width="310px">
        	<p id="option_<?php echo $option['id'];?>" class="rounded dark_shadow">
        		<span class="option rounded dark_shadow" style="width:<?php echo $option['percent'];?>%;" title="<?php echo $option['percent'];?>"></span>
        	</p>
		</td>
		</tr>
        <?php
            }
        ?>
		</table>
	</form>
</div>

<div class="info">
<div id="rotate">
<div>Номер телефона: +7 952 645 36 56</div>
<div>С одного телефона не более 1 голоса!</div>
</div>
</div>

<!--<div class="footer">&#169; Трофимов А. &#040;ПМИ-1, 3к&#041;, 2016 г. \ ICQ: 471188</div>-->

</body>
</html>