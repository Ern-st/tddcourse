<?php
declare(strict_types=1);

//NameSpace week02;

final class PhonePlan
{
    public function __construct()
    {
        
    }

    public function setPreferences($values)
    {
        $this->desiredData = $values["data"];
        $this->desiredHours = $values["hours"];
    }
}
