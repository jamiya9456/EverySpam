<?php
	$code = $_POST["code"];
	$lastNum = file_get_contents("processes.txt");

	file_put_contents("processes.txt", $lastNum + 1);
	exec("python tweetyDis.py \"$code\"");
?>
Done! Now you spammed this account even more!