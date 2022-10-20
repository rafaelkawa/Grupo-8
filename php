<?php
function bubble_Sort($my_array1 )
{
do
{
$swapped1 = false;
for( $i1 = 0, $c1 = count( $my_array1 ) - 1; $i1 < $c1; $i1++ )
{
if( $my_array1[$i1] > $my_array1[$i1 + 1] )
{
list( $my_array1[$i1 + 1], $my_array1[$i1] ) =
array( $my_array1[$i1], $my_array1[$i1 + 1] );
$swapped1 = true;
}
}
}
while( $swapped1 );
return $my_array1;
}
$test_array1 = array(3, 21, 0, -6, 2, 45, 5, 4, -1, 8, 4, 23, 1);
echo "Array original :\n";
echo implode(', ',$test_array1 );
echo "\nArray ordenado: \n:";
echo implode(', ',bubble_Sort($test_array1)). PHP_EOL;
?>
