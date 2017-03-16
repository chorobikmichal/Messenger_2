<!DOCTYPE html>
<html>
<body>
<h2>View</h2>
<hr>
<body background="bg.jpg">

<form action="" method="post" id="form3" >
<input type="hidden" name="choice3" value="set"></form>
<button type="submit" form="form3" value="go back to the user menu">go back to the user menu</button>

<form action="" method="post" id="form" >
<input type="hidden" name="choice" value="set"></form>
<button type="submit" form="form" value="next">next</button>

<form action="" method="post" id="form2" >
<input type="hidden" name="choice2" value="set2"></form>
<button type="submit" form="form2" value="prev">previous</button>

<br>

<?php
	$username= $_GET["username"];
	$stream= $_GET["stream"];
	$next= $_GET["next"];
	$sort= $_GET["sort"];
	echo (exec("./view.py $username $stream $next 0 0 $sort"));
?>

<?php if(isset($_POST["choice2"])){
	$prev= $_GET["next"]-1;}
?>

<?php if(isset($_POST["choice"])){
	$next= $_GET["next"]+1;}
?>

<?php
if(isset($_POST["choice2"])){
	header("Location: view2.php? username=$username&stream=$stream&status=$status&next=$prev&sort=$sort");
}
if(isset($_POST["choice"])){
	header("Location: view2.php? username=$username&stream=$stream&status=$status&next=$next&sort=$sort");
}
if(isset($_POST["choice3"])){
	exec("./view.py $username $stream $next 100 0 $sort");
	header("Location: choose.php? username=$username&stream=$stream&status=$status&next=$next&sort=$sort");
}
if(isset($_POST["choice4"])){
	exec("./view.py $username $stream $next 100 1 $sort");
}
if(isset($_POST["choice6"])){
	header("Location: view.php? username=$username&stream=$stream&status=$status&next=$next&sort=$sort");
}
if(isset($_POST["choice7"])){
	if($sort==0){
		$sort=1;
	}else{
		$sort=0;
	}
	header("Location: view2.php? username=$username&stream=$stream&status=$status&next=$next&sort=$sort");
}
?>

<br>
<br>

<form action="" method="post" id="form7" >
<input type="hidden" name="choice7" value="set7"></form>
<button type="submit" form="form7" value="sort">sort</button>

<form action="" method="post" id="form4" >
<input type="hidden" name="choice4" value="set4"></form>
<button type="submit" form="form4" value="mark all read">mark all read</button>

<form action="" method="post" id="form5" >
<input type="hidden" name="choice5" value="set5"></form>
<button type="submit" form="form5" value="check for new posts">check for new posts</button>

<form action="" method="post" id="form6" >
<input type="hidden" name="choice6" value="set6"></form>
<button type="submit" form="form6" value="select new stream">select new stream</button>



</body>
</html>
