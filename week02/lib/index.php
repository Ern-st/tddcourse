<?php
require __DIR__.'/../vendor/autoload.php';

use week02\PhonePlan as PhonePlan;

$phonePlan = new PhonePlan();
$allPlans = $phonePlan->getAllPlans();
$bestPlanId = null;

if (isset($_POST)){
    $input = [
        "data" => (int) filter_input(INPUT_POST, 'desiredData', FILTER_SANITIZE_NUMBER_INT),
        "hours" => (int) filter_input(INPUT_POST, 'desiredHours', FILTER_SANITIZE_NUMBER_INT)
    ];
    $phonePlan->setPreferences($input);
    $bestPlanId = $phonePlan->getBestPlan()["id"];
}

function html_table($data = array())
{
    global $bestPlanId;
    $rows = array();
    foreach ($data as $row) {
        $cells = array();
        $id = $row["id"];
        $class = $bestPlanId === $row["id"] ? "bestPlan" : "";
        unset($row["id"]);
        foreach ($row as $cell) {
            if ($cell === -1) {
                $cell = "∞";
            }
            $cells[] = "<td>{$cell}</td>";
        }
        $rows[] = "<tr id='{$id}' class='{$class}'>" . implode('', $cells) . "</tr>";
    }
    $tableHeader = "<tr><th>Company</th><th>Plan</th><th>Data</th><th>Hours</th><th>Price</th></tr>";
    return "<table class='hci-table'>" . $tableHeader . implode('', $rows) . "</table>";
}

function render_form($values = ["desiredData" => "", "desiredHours" => ""]){
?>
    <form method="post">
        <input type="number" name="desiredData" placeholder="data" value="<?php echo $values['desiredData'] ?>">
        <input type="number" name="desiredHours" placeholder="hours" value="<?php echo $values['desiredHours'] ?>">
        <input type="submit" name="submit" value="🤑">
    </form>
<?php
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        body {
            font-family: sans-serif;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            padding: 0;
            margin: 0;
            justify-content: center;
            align-items: center;
        }
        input[type=number]::-webkit-inner-spin-button, 
        input[type=number]::-webkit-outer-spin-button { 
            -webkit-appearance: none; 
            -moz-appearance: none;
            margin: 0; 
        }
        input[type=number]::-webkit-input-placeholder {
            color: #FFF;
        }
        input[type="number"] {
            -webkit-appearance: none;
            outline: none;
            border: none;
            background: #0000ff80;
            display: inline-block;
            width: 100px;
            height: 100px;
            color: #FFF;
            font-size: 2rem;
            text-align: center;
            border-radius: 50%;
            position: relative;
        }
        input[name="desiredData"] {
            right: -10px;
        }
        input[name="desiredHours"] {
            left: -10px;
            background: #ff000080;
        }
        input[type="submit"] {
            background: transparent;
            display: block;
            margin: 0 auto;
            font-size: 80px;
            cursor: pointer;
            -webkit-appearance: none;
            -moz-appearance: none;
            appearance: none;
            border: none;
            outline: none;
            transition: all .3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        input[type="submit"]:hover {
            transform: scale(1.2);
        }
        table {
            border-radius: 3px;
            border-collapse: collapse;
            border: 2px solid #CCC;
            display: block;
        }
        th, td {
            padding: 5px;
        }
        th {
            background: #ccc;
            color: #777;
        }
        .bestPlan{
            background: #7cea7c;
            font-weight: bold;
            animation: ShineAnimation 5s forwards cubic-bezier(.12,.89,.98,.47);
        }

        @keyframes ShineAnimation{
            from {
                background-repeat:no-repeat;
                background-image:-webkit-linear-gradient(
                    top left,
                    rgba(255, 255, 255, 0.0) 0%,
                    rgba(255, 255, 255, 0.0) 45%,
                    rgba(255, 255, 255, 0.5) 48%,
                    rgba(255, 255, 255, 0.8) 50%,
                    rgba(255, 255, 255, 0.5) 52%,
                    rgba(255, 255, 255, 0.0) 57%,
                    rgba(255, 255, 255, 0.0) 100%
                );
                background-position:-250px -250px;
                background-size: 600px 600px
            }
            to {
                background-repeat:no-repeat;
                background-position:250px 250px;
            }
        }
    </style>
</head>
<body>  
    <h1>HELLO HUMAN!</h1>
    Input some values and I will fetch the bestests phoneplan for you!
    <?php render_form($_POST); ?>

    <h2>All Plans</h2>
    <?php
    echo html_table($allPlans);
    ?>
</body>
</html>