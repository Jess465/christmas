#!/usr/bin/perl
use strict;
use warnings;

my $input = $ARGV[0];

my(@group, %answer2count, $i, $j, $k, $line, @split, @input, %group2group, $count, @keys);
$count = 0;

open(IN, "$input");
@input = <IN>;

for($i=0;$i<scalar(@input);$i++)
{
    if($input[$i] =~ /[a-z]/)
    {
        chomp($input[$i]);
        push(@group, $input[$i]);
        #print($input[$i], "\n");
    }
    else
    {
        $count += 1;
        $group2group{"group_$count"} = @group;
    }
}

$count += 1;
$group2group{"group_$count"} = @group;

@keys = keys(%group2group);

foreach my $key (@keys)
{
    print($group2group{$key}, "\n");
}
