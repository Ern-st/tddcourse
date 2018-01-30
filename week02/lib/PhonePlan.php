<?php
declare(strict_types=1);

//NameSpace week02;

final class PhonePlan
{
    public function __construct()
    {
        
    }

    private function querydb($query)
    {
        $db = new SQLite3('lib/database.db');
        $db_results = $db->query($query);
        $result = array();
        while ($res = $db_results->fetchArray(1))
        {
            array_push($result, $res);
        }
        $db = null;
        return $result;
    }

    public function setPreferences($values)
    {
        $this->desiredData = $values["data"];
        $this->desiredHours = $values["hours"];
    }

    public function getAllPlans()
    {
        return $this->querydb("SELECT * FROM phoneplans");
    }
}
