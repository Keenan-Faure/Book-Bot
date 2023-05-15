<?php

class Test
{
    const META_ON_HOLD = 'on_hold';
    const META_ON_HOLD_MSG = 'on_hold_msg';

    public function Test_print()
    {
        print_r(Test::META_ON_HOLD);
        print_r(Test::META_ON_HOLD_MSG);
    }
}
?>