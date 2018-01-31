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
        $db = new \SQLite3('lib/database.db');
        $db_results = $db->query($query);
        $result = array();
        while ($res = $db_results->fetchArray(1)) {
            array_push($result, $res);
        }
        $db = null;

        return $result;
    }

    public function setPreferences($values)
    {
        $this->desiredData = $values['data'];
        $this->desiredHours = $values['hours'];
    }

    public function getAllPlans()
    {
        return $this->querydb('SELECT * FROM phoneplans');
    }

    public function getBestPlan()
    {
        if ($this->desiredHours == -1) {
            return $this->querydb("SELECT * FROM phoneplans WHERE data >= {$this->desiredData} AND hours == {$this->desiredHours} ORDER BY price, data DESC limit 1")[0];
        } else {
            return $this->querydb("SELECT * FROM phoneplans WHERE data >= {$this->desiredData} AND (hours >= {$this->desiredHours} OR hours == -1) ORDER BY price, data DESC limit 1")[0];
        }
    }
}
