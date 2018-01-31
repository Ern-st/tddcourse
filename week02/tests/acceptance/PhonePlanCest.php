<?php


class PhonePlanCest
{
    public function _before(AcceptanceTester $I)
    {
    }

    public function _after(AcceptanceTester $I)
    {
    }

    // tests
    public function GetAPhonePlan(AcceptanceTester $I)
    {
        $I->amOnPage('/');
        $I->see('HELLO HUMAN');
        $I->fillField('desiredData', '20');
        $I->fillField('desiredHours', '20');
        $I->click('GOGOGO!');
        $I->see('Oister', '.bestPlan');
        $I->see('P4', '.bestPlan');
    }
}
