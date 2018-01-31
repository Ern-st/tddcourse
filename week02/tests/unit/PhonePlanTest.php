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
        $aPhonePlan = new PhonePlan(['data' => 20, 'hours' => 5]);
    }

    public function testThatWeCanGetAllPhonePlans()
    {
        $aPhonePlan = new PhonePlan();
        $allPlans = $aPhonePlan->getAllPlans();
        //codecept_debug(print_r($allPlans, true));
        $this->assertCount(9, $allPlans);
    }

    public function testThatIGetTheCheapestPlan()
    {
        $aPhonePlan = new PhonePlan();
        $aPhonePlan->setPreferences(['data' => 20, 'hours' => 20]);
        $bestplan = $aPhonePlan->getBestPlan();
        //codecept_debug(print_r($bestplan, true));
        $this->assertArraySubset(
            array(
                'company' => 'Oister',
                'plan' => 'P4',
            ),
            $bestplan
        );

        $aPhonePlan->setPreferences(['data' => 2, 'hours' => -1]);
        $bestplan = $aPhonePlan->getBestPlan();
        //codecept_debug(print_r($bestplan, true));
        $this->assertArraySubset(
            array(
                'company' => 'Oister',
                'plan' => 'P4',
            ),
            $bestplan
        );
    }

    /**
     * @expectedException           Exception
     * @expectedExceptionMessage    You need to set the preferences before calling getBestPlan
     */
    public function testThatIGetAnExceptionIfIHaveNotSetAnyPreferences()
    {
        $aPhonePlan = new PhonePlan();
        $bestplan = $aPhonePlan->getBestPlan();
    }

    /**
     * @expectedException           Exception
     * @expectedExceptionMessage    You can only use Integers for your preferences, use -1 for infinite
     */
    public function testThatIGetAnExceptionIfITryToSetPreferencesWithAnythingButIntegers()
    {
        $aPhonePlan = new PhonePlan(['data' => 2.45, 'hours' => "mange"]);
    }
}
