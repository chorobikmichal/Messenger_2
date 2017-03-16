<!DOCTYPE html>
<html>
<body>
<h2>View Program</h2>
<hr>
<body background='bg.jpg'>
<form action="" method="post" id="form" >

choose the stream you want to view:<br><input type="text" name="stream"><br><br> 

<form form="form" action="" ><input type="submit" value="post" /></form>

<?php
if(isset($_GET["username"])){
$username = $_GET["username"];

}
?>


<?php
if(isset($_POST["stream"])){
$stream = $_POST["stream"];

}
?>

<?php
if(isset($_POST["stream"])){
      $status = (exec(""));
      header("Location: view2.php? username=$username&stream=$stream&status=$status&next=0&sort=0");
}
?>


</body>
</html>
