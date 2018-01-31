<?php 
$I = new ApiTester($scenario);
$I->wantTo('get a small Phone Plan');
$I->sendGET('/', ['desiredData' => 1, 'desiredHours' => 1]);
$I->seeResponseCodeIs(\Codeception\Util\HttpCode::OK);
$I->seeResponseIsJson();
$I->seeResponseContainsJson([ 'company' => 'Oister', 'plan' => 'P1']);