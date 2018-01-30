<?php

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
        $aPhonePlan = new PhonePlan;
        $this->assertInstanceOf(
            PhonePlan::class,
            $aPhonePlan
        );
    }
}