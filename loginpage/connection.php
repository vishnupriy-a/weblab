<?php
$c=mysqli_connect("localhost","root","","lab");
if(!$c)
{
    echo "connect failed".mysqli_connect_error();
    exit();
}
// echo "successfully connected";
?>