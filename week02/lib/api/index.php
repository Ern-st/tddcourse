<?php
require __DIR__.'/../../vendor/autoload.php';

use week02\PhonePlan as PhonePlan;

$input = [
    "data" => (int) filter_input(INPUT_GET, 'desiredData', FILTER_SANITIZE_NUMBER_INT),
    "hours" => (int) filter_input(INPUT_GET, 'desiredHours', FILTER_SANITIZE_NUMBER_INT)
];

try {
    $aPhonePlan = new PhonePlan($input);
    $bestPlan = $aPhonePlan->getBestPlan();
    $response = json_encode($bestPlan);
    echo $response;
    die();
} catch (Exception $e) {
    echo("FAILED!");
    echo $e->getMessage();
}