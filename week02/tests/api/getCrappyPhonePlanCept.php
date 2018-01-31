<?php 
$I = new ApiTester($scenario);
$I->wantTo('get a crappy Phone Plan');
$I->sendGET('/', ['desiredData' => 25, 'desiredHours' => 5]);
$I->seeResponseCodeIs(\Codeception\Util\HttpCode::OK);
$I->seeResponseIsJson();
$I->seeResponseContainsJson([ 'company' => 'Callme', 'plan' => 'P1']);