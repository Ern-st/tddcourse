<?php

declare(strict_types=1);

namespace week02;

final class PhonePlan
{
    public function __construct($values = null)
    {
        if (!is_null($values)) {
            $this->setPreferences($values);
        }
    }

    private function querydb($query)
    {
        $db = new \SQLite3(__DIR__ . '/database.db');
        $db_results = $db->query($query);
        $result = array();
        while ($res = $db_results->fetchArray(1)) {
            array_push($result, $res);
        }
        $db = null;

        return $result;
    }

    private function validatePreferences($values){
        foreach ($values as $key => $value) {
            if (!is_int($value)) {
                throw new \Exception("You can only use Integers for your preferences, use -1 for infinite");
            }
        }
    }

    private function checkPreferences(){
        if (!isset($this->desiredData) OR !isset($this->desiredHours)) {
            throw new \Exception("You need to set the preferences before calling getBestPlan");
        }
    }

    public function setPreferences($values)
    {
        $this->validatePreferences($values);
        $this->desiredData = $values['data'];
        $this->desiredHours = $values['hours'];
    }

    public function getAllPlans()
    {
        return $this->querydb('SELECT * FROM phoneplans ORDER BY price');
    }

    public function getBestPlan()
    {
        $this->checkPreferences();
        if ($this->desiredHours == -1) {
            return $this->querydb("SELECT * FROM phoneplans WHERE data >= {$this->desiredData} AND hours == {$this->desiredHours} ORDER BY price, data DESC limit 1")[0];
        } else {
            return $this->querydb("SELECT * FROM phoneplans WHERE data >= {$this->desiredData} AND (hours >= {$this->desiredHours} OR hours == -1) ORDER BY price, data DESC limit 1")[0];
        }
    }
}
