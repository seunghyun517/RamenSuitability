<?php

define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'menurating');
define('DB_PASSWORD', 'iloveramen0!');
define('DB_NAME', 'menurating');
 
/* Attempt to connect to MySQL database */
$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
$link->query("SET NAMES 'UTF8'");
// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}

$rate = "";

if($_SERVER["REQUEST_METHOD"] == "POST"){
  if(empty(trim($_POST["rate"])) || empty(trim($_POST["menu"]))){
    echo "Something went wrong";
  }
}

// Prepare an insert statement
$sql = "INSERT INTO menurates (menu, rate) VALUES (?, ?)";
         
if($stmt = mysqli_prepare($link, $sql)){
    // Bind variables to the prepared statement as parameters
    mysqli_stmt_bind_param($stmt, "ss", $param_menu, $param_rate);
    
    // Set parameters
    $param_menu = $menu;
    $param_rate = $rate;
    
    // Attempt to execute the prepared statement
    if(mysqli_stmt_execute($stmt)){
        // Redirect to login page
        header("location: index.php");
    } else{
        echo "Something went wrong. Please try again later.";
    }

    // Close statement
    mysqli_stmt_close($stmt);
}


?>







<!DOCTYPE html>
<html>
  <head>
    <title>Website rating form</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" integrity="sha384-5sAR7xN1Nv6T6+dT2mhtzEpVJvfS3NScPQTrOxhwjIuvcA67KV2R5Jz6kr4abQsz" crossorigin="anonymous">
    <link rel="stylesheet" href="template.css">
  </head>
  <body>
    <div class="main-block">
      <h1>Website Rating Form</h1>
      <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <div class="grade-type">
          <h3>Rate Our Website</h3>
          <input type="hidden" id="menu" name="menu" value="potato">
          <div> 
            <button type="submit" name="rate" value="5">Excellent</button>
          </div>
          <div>
            <button type="submit" name="rate" value="4">Good</button>
          </div>
          <div>
            <button type="submit" name="rate" value="3">Normal</button>
          </div>
          <div>
            <button type="submit" name="rate" value="2">Bad</button>
          </div>
          <div>
            <button type="submit" name="rate" value="1">Very bad</button>
          </div>
        </div>
      </form>
    </div>
  </body>
</html>