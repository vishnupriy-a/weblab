<html>
	<body>
		<form method="post" action="logintchr.php">
			<label>USERNAME</label><br>
			<input type="text" name="user"><br>
			<label>PASWWORD</label><br>
			<input type="password" name="pword"><br>
			<input type="submit" value="login" name="a">
		</form>
	</body>
<html>
<?php
include("connection.php");
SESSION_start();
if(isset($_POST['a']))
{


	$c=$_POST['user'];
	$_SESSION['user']=$c;
	$b=$_POST['pword'];
	$r=mysqli_query($conn,"SELECT * FROM `login` WHERE name='$c' and password='$b'");
	if(mysqli_num_rows($r)>0)
	{
		header("Location:home.php");
	}
	else
	{
		echo ("login failed");
	}
}
?>
