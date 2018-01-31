<?php
require __DIR__.'/../vendor/autoload.php';

use week02\PhonePlan as PhonePlan;

$phonePlan = new PhonePlan();
$allPlans = $phonePlan->getAllPlans();
?>

HELLO HUMAN!
Input some values and I will fetch the bestets phoneplan for you!
<form action="/" method="POST">
    <input type="number" name="desiredData" placeholder="data in GB">
    <input type="number" name="desiredHours" placeholder="hours in hours">
</form>