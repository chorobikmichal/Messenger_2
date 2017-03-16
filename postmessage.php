<!DOCTYPE html>
<html>
<body>
<h2>Write your message</h2>
<hr>
<body background='bg.jpg'>
<form action="" method="post" id="form" >

stream:<br><input type="text" name="stream"><br><br> 

message:<br><textarea name="message" rows="7" cols="50"></textarea><br>

<form form="form" action="" ><input type="submit" value="post" /></form>

<?php
if(isset($_GET["username"])){
$username = $_GET["username"];

}
?>


<?php
if(isset($_POST["message"])){
$message = $_POST["message"];
$message = str_replace("\n",'"<br/>"',$message);
$message = str_replace("\r",'',$message);
}
?>


<?php
if(isset($_POST["stream"])){
$stream = $_POST["stream"];

}
?>

<?php
if(isset($_POST["stream"])){
      $status = (exec("./post $username $stream $message"));
      header("Location: choose.php? username=$username&streamname=$stream&message=$message&status=$status");
}
?>


</body>
</html>
