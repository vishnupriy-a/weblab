<?php
include "connection.php";
// echo $_POST['Username'];
session_start();
$error=false;
if(isset($_POST['Username'])&&isset($_POST['Password']))
{
$uname=$_POST['Username'];
$password=$_POST['Password'];
$q="select * from _user where _username='".$uname."'";
// echo $q;
$res='';
$res=mysqli_query($c,$q);
$res_ar=mysqli_fetch_array($res,MYSQLI_ASSOC);
// print(mysqli_num_rows($res))
// foreach($res_ar as $r)
// print($r);
// print($res_ar["_username"]);
if($res_ar["_username"]==$uname && $res_ar["_password"]==$password)
{
  $_SESSION['_username']=$res_ar["_username"];
  $_SESSION['_password']=$res_ar["_password"];
header("location:profile.php");
// echo $_SESSION['_username'];
}
else
$error=true;
$res='';
$res_ar='';
}
?>
<!DOCTYPE html>
<html>

<head>
  <title>Login Form </title>
  <style type="text/css">
    body {
      background-color: #c5d4d0;
      background-image: url('') !important;
    }

    section {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    form {
      width: 30%;
      background-color: #ecf0f1;
      padding: 25px;
      border-radius: 25px;
    }
  </style>
</head>

<body>
  <section>
    <form method="post" action="login.php">
      <div>
        <div>
        </div>
        <div></div>
        <div align=center>
          <P><b> LOGIN </b></P>
        </div>
        <div></div>
      </div>
      <div align=center>
        <label>Username</label>&nbsp;&nbsp;
        <input type="text" placeholder="Username" required name="Username" style="border-radius: 25px;">
      </div>
      <br>
      <div align=center>
        <label>Password</label>&nbsp;&nbsp;
        <input type="password" placeholder="Password" required name="Password" style="border-radius: 25px;">
      </div>
      <br>
      <div>
        <div></div>
        <div align=center>
          <button type="submit" name="login" id="login" style="border-radius: 25px;">Submit</button>
        </div>

      </div>

      <div> <?php if ($error) {
              echo "<h3 style='color:red'>Invalid username or password !</h3>";
            } ?></div>

    </form>

  </section>
</body>

</html>