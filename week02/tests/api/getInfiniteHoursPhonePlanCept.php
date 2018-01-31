<?php 
$I = new ApiTester($scenario);
$I->wantTo('get a Phone Plan with infinite hours');
$I->sendGET('/', ['desiredData' => 10, 'desiredHours' => -1]);
$I->seeResponseCodeIs(\Codeception\Util\HttpCode::OK);
$I->seeResponseIsJson();
$I->seeResponseContainsJson([ 'company' => 'Oister', 'plan' => 'P4']);