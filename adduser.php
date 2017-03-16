<!DOCTYPE html>
<html>
<body>
<h2>Add User </h2>
<hr>
<body background='bg.jpg'>
<form action="" method="post" id="form" >

<?php
    $streams="add";
?>

list the streams:<br><input type="text" name="streams"><br><br> 

<form form="form" action="" ><input type="submit" value="post" /></form>

<?php
if(isset($_GET["username"])){
$username = $_GET["username"];

}
?>


<?php
if(isset($_POST["streams"])){
$streams = $_POST["streams"];

}
?>

<?php
if(isset($_POST["streams"])){
      $status = (exec("./addauthor $streams $username "));
      header("Location: choose.php? username=$username&streams=$streams&status=$status");
}
?>


</body>
</html>
