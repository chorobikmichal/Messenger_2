<!DOCTYPE html>
<html>
<body>
<h2>Choose an Option</h2>
<hr>
<body background='bg.jpg'>

<?php
exec("./textfile.txt");
?>

<br>

<?php
if(isset($_GET["username"])){
$username = $_GET["username"];

}
?>


<?php
 $username = str_replace(' ','~',$username);
?>

<form action="" method="post" id ="form1">
<input type="hidden" name="choice1" value="set1"></form>
<button type="submit" form="form1" value="add author">add author</button>


<form action="" method="post" id ="form2">
<input type="hidden" name="choice2" value="set2"></form>
<button type="submit" form="form2" value="remove author">remove author</button>


<form action="" method="post" id ="form3">
<input type="hidden" name="choice3" value="set3"></form>
<button type="submit" form="form3" value="post message">post message</button>


<form action="" method="post" id ="form4">
<input type="hidden" name="choice4" value="set4"></form>
<button type="submit" form="form4" value="view stream">view stream</button>


<form action="" method="post" id ="form5">
<input type="hidden" name="choice5" value="set5"></form>
<button type="submit" form="form5" value="log in as a different user">log in as a different user</button>

<br>
<?php
if(isset($_POST["choice1"])){
      $status = (exec("./a3 adduser"));
      header("Location: adduser.php?username=$username");
}
?>


<?php
if(isset($_POST["choice2"])){
      $status = (exec("./a3 removeuser"));
      header("Location: removeuser.php?username=$username");
}
?>


<?php
if(isset($_POST["choice3"])){
      $status = (exec("./a3 postmessage"));
      header("Location: postmessage.php?username=$username");
}
?>


<?php
if(isset($_POST["choice4"])){
      $status = (exec("./a3 view"));
      header("Location: view.php?username=$username");
}
?>


<?php
if(isset($_POST["choice5"])){
      $status = (exec(""));
      header("Location: index.php");
}
?>


<br>

<?php
    echo ($_GET["status"]);
?>

</body>
</html>
