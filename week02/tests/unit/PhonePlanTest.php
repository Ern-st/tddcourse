<?php

use week02\PhonePlan as PhonePlan;

class PhonePlanTest extends \Codeception\Test\Unit
{
    /**
     * @var \UnitTester
     */
    protected $tester;
    
    protected function _before()
    {
    }

    protected function _after()
    {
    }

    // tests
    public function testWeCanCreateAPhonePlanObject()
    {
        $aPhonePlan = new PhonePlan();
        $this->assertInstanceOf(
            PhonePlan::class,
            $aPhonePlan
        );
    }

    public function testWeCanSetPreferences()
    {
        $aPhonePlan = new PhonePlan();
        $aPhonePlan->setPreferences(['data' => 20, 'hours' => 5]);
    }

    public function testThatWeCanGetAllPhonePlans()
    {
        $aPhonePlan = new PhonePlan();
        $allPlans = $aPhonePlan->getAllPlans();
        //codecept_debug(print_r($allPlans, true));
        $this->assertCount(9, $allPlans);
    }
}