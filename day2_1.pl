#!/usr/bin/perl
#use strict;
use warnings;

my $in = $ARGV[0];

my $sum = 0;
my $count = 0;
my @spl;
my ($i, $up, $down, @array, $pwd, @test);

open(IN, "$in") || die "Coulnd't open $in.\n";
while(<IN>)
{
    @_ = split(" ", $_);
    $_[1] =~ s/://;
    $pwd = $_[2];
    @spl = (//, $pwd);
    @array = split("-", $_[0]);
    $down = $array[0];
    $up = $array[1];
    @test = split("", $spl[1]);
    #print(scalar(@test), "\n");
    for($i=0;$i>scalar(@test);$i++)
    {
        print("$test[$i]\n");
        print($i, "\n");
        if($test[$i] eq $_[1])
        {
            $count += 1;
        }
    }
    if($count >= $down && $count <= $up)
    {
        $sum += 1;
        $count = 0;
    }
}

print($sum, "\n");
