<?php
/**
 * Box packing (3D bin packing, knapsack problem).
 *
 * @author Doug Wright
 */
declare(strict_types=1);

namespace DVDoug\BoxPacker;

use DVDoug\BoxPacker\Test\TestBox;
use DVDoug\BoxPacker\Test\TestItem;
use function GuzzleHttp\Promise\all;
use PHPCoord\LatLng;
use PHPCoord\OSRef;
use PHPCoord\RefEll;
use phpDocumentor\Reflection\Types\Array_;
use phpDocumentor\Reflection\Types\Boolean;
use PHPUnit\Framework\TestCase;
use function iterator_to_array;

/**
 * @covers \DVDoug\BoxPacker\Packer
 */


class Hospital {
    private $lat;
    private $lon;
    private $med1;
    private $med2;
    private $med3;
    private $xpt;
    private $ypt;

    public function __construct(
        float $lat,
        float $lon,
        int $med1,
        int $med2,
        int $med3,
        float $xpt,
        float $ypt
    ) {
        $this->lat = $lat;
        $this->lon = $lon;
        $this->med1 = $med1;
        $this->med2 = $med2;
        $this->med3 = $med3;
        $this->xpt = $xpt;
        $this->ypt = $ypt;
    }
}

class Container {
    private $lat;
    private $lon;

    private $xpt;
    private $ypt;

    public function __construct(
        float $lat,
        float $lon,
        float $xpt,
        float $ypt
    ) {
        $this->lat = $lat;
        $this->lon = $lon;
        $this->xpt = $xpt;
        $this->ypt = $ypt;
    }
}




function remove_drone($dist, $all_drone){
    $result = array();
    foreach ($all_drone as $drone) {
        if ($drone->getFlybility() > $dist){
            array_push($result, $drone);
        }
    }
    return $result;
}


function calculate_drone_number($packedBoxes, $type){
    $myfile = fopen("testfile.txt", "a");
    foreach ($packedBoxes as $packedBox) {
        $boxType = $packedBox->getBox(); // your own box object, in this case TestBox
        $packedItems = $packedBox->getItems();
        foreach ($packedItems as $packedItem) { // $packedItem->getItem() is your own item object, in this case TestItem
            echo $packedItem->getItem()->getDescription() ;
            fwrite($myfile, $packedItem->getItem()->getDescription());
        }

        echo "\n";
        fwrite($myfile, " ");

    }
    if ($type==1){
        fwrite($myfile, "\t");
    }
    elseif ($type==2){
        fwrite($myfile, "\n");
    }
    fclose($myfile);
}


function pack_stretgey($dist, $all_drone, $all_item, $require_item)
{
    $useful_drone = remove_drone($dist, $all_drone);
    $arrlength = count($useful_drone);

//    for($x = 0; $x < $arrlength; $x++) {
//        echo $useful_drone[$x]->getFlybility();
//        echo "\n";
//    }

    $packer = new Packer();
    $index = 0;
    foreach ($require_item as $require) {
        for ($i=0; $i<$require; $i++){
            $packer->addItem($all_item[$index]);
        }
        $index++;
    }
    foreach ($useful_drone as $drone){
        $packer->addBox($drone);
    }

    $packedBoxes = $packer->pack();
//    print  count($packedBoxes). PHP_EOL;

    $flag = true;
    foreach ($packedBoxes as $packedBox) {
        $boxType = $packedBox->getBox(); // your own box object, in this case TestBox
//        if ( $boxType->getReference()=="F" and $flag){
//            $container1->addItem($drone_b);
//            $flag = false;
//        }
//        if ( $boxType->getReference() == "F" && $flag){
//            $packedBoxes->insert(new TestBox('B', 30, 30, 22, 0, 8, 10, 14, 8,52.67));
//            $flag = false;
//        }
        echo "This box is a {$boxType->getReference()}, it is {$boxType->getOuterWidth()}mm wide, {$boxType->getOuterLength()}mm long and {$boxType->getOuterDepth()}mm high" . PHP_EOL;
        echo "The combined weight of this box and the items inside it is {$packedBox->getWeight()}g" . PHP_EOL;

        echo "The items in this box are:" . PHP_EOL;
        $packedItems = $packedBox->getItems();
        foreach ($packedItems as $packedItem) { // $packedItem->getItem() is your own item object, in this case TestItem
            echo $packedItem->getItem()->getDescription() . PHP_EOL;
        }
    }

    return $packedBoxes;
}

class PackerTest extends TestCase
{
    /**
     * Test used width calculations on a case where it used to fail.
     */
    public function testPackThreeItemsOneDoesntFitInAnyBox(): void
    {
        ob_end_flush();

//        print 123;
        $box1 = new TestBox('A', 45, 45, 25, 0, 8, 10, 14, 3,23.33);
        $box2 = new TestBox('B', 30, 30, 22, 0, 8, 10, 14, 8,52.67);
        $box3 = new TestBox('C', 60, 50, 30, 0, 24, 20, 20, 14,37.33);
        $box4 = new TestBox('D', 25, 20, 25, 0, 8, 10, 14, 11, 18);
        $box5 = new TestBox('E', 25, 20, 27, 0, 24, 20, 20, 15, 15);
        $box6 = new TestBox('F', 40, 40, 25, 0, 24, 20, 20, 22, 31.6);
        $box7 = new TestBox('G', 32, 32, 17, 0, 24, 20, 20, 20,17.07);

        $c1 = new TestBox('container1', 231, 92, 94, 0, 231, 92, 94, 2000,17.07);

        $item1 = new TestItem('Item 1', 14, 7, 5, 2, false);
        $item2 = new TestItem('Item 2', 5, 8, 5, 2, false);
        $item3 = new TestItem('Item 3', 12, 7, 4, 3, false);
        $drone_b = new TestItem('B', 30, 30, 22, 0, false);


        $all_drone = array($box1, $box2, $box3, $box4, $box5, $box6, $box7);
        $all_item = array($item1, $item2, $item3);
        $requirement = array($item1, $item2, $item3);

        $all_data = array(
            array(33.186,1,2,0,1,"Hospital HIMA",1), array(23.717,1,1,1,0, "Hospital PS",1), array(12.896,1,2,1,2,"Children’s Hospital",1), array(51.677,3,1,0,0,"Hospital PA",1),
            array(16.032,2,2,0,1, "Hospital HIMA",2), array(14.943,2,1,1,0, "Hospital PS",2), array(21.205,2,2,1,2, "Children’s Hospital",2), array(36.474,3,1,0,1, "CMC",2)
        );


        for($x =14; $x < 60; $x++) {
            $number_of_drone = array();
            $container1 = new Packer();
            $container2 = new Packer();
            $container1->addBox($c1);
            $container2->addBox($c1);

            echo "N=".$x . "\n";

//            echo "Today is day " . $x . "\n";
            foreach ( $all_data as $d ){
                echo "Container".$d[6]." to ".$d[5].". Distance is ".$d[0]."\n";
                $result = pack_stretgey($d[0], $all_drone, $all_item, array($d[2]*$x*$d[1],$d[3]*$x*$d[1],$d[4]*$x*$d[1]));

                if ( $d[6] == 1 ) {
                    $flag = true;
                    foreach ($result as $packedBox) {
                        $boxType = $packedBox->getBox(); // your own box object, in this case TestBox
//                        echo $boxType->getReference();
                        $container1->addItem( new TestItem($boxType->getReference(), $boxType->getOuterWidth(), $boxType->getOuterLength(), $boxType->getOuterDepth(), 0, false));
                        $string1 = $boxType->getReference();
//                        echo $string1;
                        if ( $boxType->getReference()=="F" and $flag){
                            $container1->addItem($drone_b);
                            $flag = false;
                        }
                    }
                }
                elseif ( $d[6] == 2 ){
                    $flag = true;
                    foreach ($result as $packedBox) {
                        $boxType = $packedBox->getBox(); // your own box object, in this case TestBox
//                        echo $boxType->getReference();
                        $container2->addItem( new TestItem($boxType->getReference(), $boxType->getOuterWidth(), $boxType->getOuterLength(), $boxType->getOuterDepth(), 0, false));
                        if ( $boxType->getReference()=="F" and $flag){
                            $container2->addItem($drone_b);
                            $flag = false;
                        }
                        //                        echo 7897970;
//                        echo "\n";
//                        echo $boxType->getOuterWidth();
//                        echo $boxType->getOuterWidth();
//                        echo "\n";

                    }
                }
            }

            $packedBoxes1 = $container1->pack() ;
            $packedBoxes2 = $container2->pack() ;
//            foreach ($packedBoxes1 as $packedBoxes1) {
//                $test_boxes = $packedBoxes1->getbox();
//                $packedItems = $packedBoxes1->getItems();
//                foreach ($packedItems as $packedItem) { // $packedItem->getItem() is your own item object, in this case TestItem
//                    echo $packedItem->getItem()->getDescription() . PHP_EOL;
//                }
//            }

//            echo "this is the most important";
            if (count($packedBoxes1) > 1 || count($packedBoxes2) > 2) {
//                echo "this is final n=> ".$x;
                break;
            }

            calculate_drone_number($packedBoxes1, 1);
            calculate_drone_number($packedBoxes2, 2);


        }
        echo "\n";
    }



//        $container1->addBox($c1);
//        $packedBoxes = $container1->pack();
//
//        foreach ($packedBoxes as $packedBox) {
//            $boxType = $packedBox->getBox(); // your own box object, in this case TestBox
//            echo "This box is a {$boxType->getReference()}, it is {$boxType->getOuterWidth()}mm wide, {$boxType->getOuterLength()}mm long and {$boxType->getOuterDepth()}mm high" . PHP_EOL;
//            echo "The combined weight of this box and the items inside it is {$packedBox->getWeight()}g" . PHP_EOL;
//
//            echo "The items in this box are:" . PHP_EOL;
//            $packedItems = $packedBox->getItems();
//            foreach ($packedItems as $packedItem) { // $packedItem->getItem() is your own item object, in this case TestItem
//                echo $packedItem->getItem()->getDescription() . PHP_EOL;
//            }
//        }

//        $boxType = $packedBoxes->getBox(); // your own box object, in this case TestBox
//
//        $packedItems = $boxType->getItems();
//        foreach ($packedItems as $packedItem) { // $packedItem->getItem() is your own item object, in this case TestItem
//            echo $packedItem->getItem()->getDescription() . PHP_EOL;
//            echo 111111;
//        }




//        $packer = new Packer();
//
//        $packer->addBox($box1);
//        $packer->addBox($box1);
//
//        $packer->addBox($box2);
//        $packer->addBox($box3);
//
//        $packer->addItem($item2);
//        $packer->addItem($item2);



//        $packer->addItem($item2);
//        $packer->addItem($item3);


//        print 12345667;

//        $packedBoxes = $packer->pack();
//
//        print  count($packedBoxes). PHP_EOL;
//
//        echo "These items fitted into " . count($packedBoxes) . " box(es)" . PHP_EOL;
//        foreach ($packedBoxes as $packedBox) {
//            $boxType = $packedBox->getBox(); // your own box object, in this case TestBox
//            echo "This box is a {$boxType->getReference()}, it is {$boxType->getOuterWidth()}mm wide, {$boxType->getOuterLength()}mm long and {$boxType->getOuterDepth()}mm high" . PHP_EOL;
//            echo "The combined weight of this box and the items inside it is {$packedBox->getWeight()}g" . PHP_EOL;
//
//            echo "The items in this box are:" . PHP_EOL;
//            $packedItems = $packedBox->getItems();
//            foreach ($packedItems as $packedItem) { // $packedItem->getItem() is your own item object, in this case TestItem
//                echo $packedItem->getItem()->getDescription() . PHP_EOL;
//            }
//        }
//    }

    /**
     * @expectedException \DVDoug\BoxPacker\ItemTooLargeException
     */
    public function testPackWithoutBox(): void
    {
        $item1 = new TestItem('Item 1', 2500, 2500, 20, 2000, true);
        $item2 = new TestItem('Item 2', 25000, 2500, 20, 2000, true);
        $item3 = new TestItem('Item 3', 2500, 2500, 20, 2000, true);

        $packer = new Packer();
        $packer->addItem($item1);
        $packer->addItem($item2);
        $packer->addItem($item3);
        $packer->pack();
        $packedBoxes = $packer->pack();

    }

    /**
     * Test weight distribution getter/setter.
     */
    public function testCanSetMaxBoxesToWeightBalance(): void
    {
        $packer = new Packer();
        $packer->setMaxBoxesToBalanceWeight(3);
        self::assertEquals(3, $packer->getMaxBoxesToBalanceWeight());
    }

    /**
     * Test that weight redistribution activates (or not) correctly based on the current limit.
     */
    public function testWeightRedistributionActivatesOrNot(): void
    {
        // first pack normally - expecting 2+2 after balancing

        $packer = new Packer();
        $packer->addBox(new TestBox('Box', 1, 1, 4, 0, 1, 1, 2, 3,1));
        $packer->addItem(new TestItem('Item', 1, 1, 1, 1, true), 4);

        /** @var PackedBox[] $packedBoxes */
        $packedBoxes = iterator_to_array($packer->pack(), false);

        self::assertCount(2, $packedBoxes[0]->getItems());
        self::assertCount(2, $packedBoxes[1]->getItems());

        // same items, but with redistribution turned off - expecting 3+1 based on pure fit
        $packer = new Packer();
        $packer->addBox(new TestBox('Box', 1, 1, 3, 0, 1, 1, 3, 3,1));
        $packer->addItem(new TestItem('Item', 1, 1, 1, 1, false), 4);
        $packer->setMaxBoxesToBalanceWeight(1);

        /** @var PackedBox[] $packedBoxes */
        $packedBoxes = iterator_to_array($packer->pack(), false);

        self::assertCount(3, $packedBoxes[0]->getItems());
        self::assertCount(1, $packedBoxes[1]->getItems());
    }

    /**
     * Test used width calculations on a case where it used to fail.
     */
    public function testIssue52A(): void
    {
        $packer = new Packer();
        $packer->addBox(new TestBox('Box', 100, 50, 50, 0, 100, 50, 50, 5000));
        $packer->addItem(new TestItem('Item', 15, 13, 8, 407, true), 2);
        $packedBoxes = $packer->pack();

        self::assertCount(1, $packedBoxes);
        self::assertEquals(26, $packedBoxes->top()->getUsedWidth());
        self::assertEquals(15, $packedBoxes->top()->getUsedLength());
        self::assertEquals(8, $packedBoxes->top()->getUsedDepth());
    }

    /**
     * Test used width calculations on a case where it used to fail.
     */
    public function testIssue52B(): void
    {
        $packer = new Packer();
        $packer->addBox(new TestBox('Box', 370, 375, 60, 140, 364, 374, 40, 3000));
        $packer->addItem(new TestItem('Item 1', 220, 310, 12, 679, true));
        $packer->addItem(new TestItem('Item 2', 210, 297, 11, 648, true));
        $packer->addItem(new TestItem('Item 3', 210, 297, 5, 187, true));
        $packer->addItem(new TestItem('Item 4', 148, 210, 32, 880, true));
        $packedBoxes = $packer->pack();

        self::assertCount(1, $packedBoxes);
        self::assertEquals(310, $packedBoxes->top()->getUsedWidth());
        self::assertEquals(368, $packedBoxes->top()->getUsedLength());
        self::assertEquals(32, $packedBoxes->top()->getUsedDepth());
    }

    /**
     * Test used width calculations on a case where it used to fail.
     */
    public function testIssue52C(): void
    {
        $packer = new Packer();
        $packer->addBox(new TestBox('Box', 230, 300, 240, 160, 230, 300, 240, 15000));
        $packer->addItem(new TestItem('Item 1', 210, 297, 4, 213, true));
        $packer->addItem(new TestItem('Item 2', 80, 285, 70, 199, true));
        $packer->addItem(new TestItem('Item 3', 80, 285, 70, 199, true));

        /** @var PackedBox[] $packedBoxes */
        $packedBoxes = iterator_to_array($packer->pack(), false);

        self::assertCount(1, $packedBoxes);
        self::assertEquals(210, $packedBoxes[0]->getUsedWidth());
        self::assertEquals(297, $packedBoxes[0]->getUsedLength());
        self::assertEquals(74, $packedBoxes[0]->getUsedDepth());
    }

    /**
     * Test case where last item algorithm picks a slightly inefficient box.
     */
    public function testIssue117(): void
    {
        $packer = new Packer();
        $packer->addBox(new TestBox('Box A', 36, 8, 3, 0, 36, 8, 3, 2));
        $packer->addBox(new TestBox('Box B', 36, 8, 8, 0, 36, 8, 8, 2));
        $packer->addItem(new TestItem('Item 1', 35, 7, 2, 1, false));
        $packer->addItem(new TestItem('Item 2', 6, 5, 1, 1, false));
        /** @var PackedBox[] $packedBoxes */
        $packedBoxes = iterator_to_array($packer->pack(), false);
        self::assertCount(1, $packedBoxes);
        self::assertEquals('Box A', $packedBoxes[0]->getBox()->getReference());
    }

    /**
     * Where 2 perfectly filled boxes are a choice, need to ensure we pick the larger one or there is a cascading
     * failure of many small boxes instead of a few larger ones.
     */
    public function testIssue38(): void
    {
        $packer = new Packer();
        $packer->addBox(new TestBox('Box1', 2, 2, 2, 0, 2, 2, 2, 1000,1));
        $packer->addBox(new TestBox('Box2', 4, 4, 4, 0, 4, 4, 4, 1000,1));

        $packer->addItem(new TestItem('Item 9', 4, 4, 4, 100, false));
        $packer->addItem(new TestItem('Item 9', 4, 4, 4, 100, false));

        $packer->addItem(new TestItem('Item 9', 4, 4, 4, 100, false));

        $packer->addItem(new TestItem('Item 9', 4, 4, 4, 100, false));
        $packer->addItem(new TestItem('Item 9', 4, 4, 4, 100, false));

        /** @var PackedBox[] $packedBoxes */
        $packedBoxes = iterator_to_array($packer->pack(), false);

        self::assertCount(2, $packedBoxes);
    }
}


//        y = np.array( [ 1.27358e+07, 1.26935e+07,     1.26891e+07,     1.2679e+07,     1.26156e+07] )
//        x = np.array( [ 8.61409e+06, 8.62274e+06, 8.60544e+06, 8.60859e+06, 8.60308e+06 ] )
//        $OSRef = new OSRef(500000, 200000); //Easting, Northing
//        $LatLng = $OSRef->toLatLng();
//        $GPSLatLng = $LatLng->toWGS84(); //optional, for GPS compatibility
//        $lat =  $LatLng->getLat();
//        $long = $LatLng->getLng();
//        $LatLng = new LatLng(50.12345, 1.23456, 0, RefEll::wgs84()); //Latitude, Long, height
//        $OSRef = $LatLng->toOSRef();
//        $easting = $OSRef->getX();
//        $northing = $OSRef->getY();
//        echo $easting;
//        echo $northing;