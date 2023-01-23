<?php
$conn=mysqli_connect("localhost","root","cetmca","vp");
if(!$conn)
{
    echo "connect failed".mysqli_connect_error();
    exit();
}
// echo "successfully connected";
?>
