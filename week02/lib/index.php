<?php
require __DIR__.'/../vendor/autoload.php';

use week02\PhonePlan as PhonePlan;

$phonePlan = new PhonePlan();
echo($phonePlan->getAllPlans());