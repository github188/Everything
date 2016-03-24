#!/usr/bin/env perl
use Digest::MD5 qw(md5 md5_hex md5_base64);
###################################################
@msg1 = (0x28, 0x02, 0x00, 0x34,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x01, 0x0d,
0x31, 0x35, 0x38, 0x30, 0x31, 0x35, 0x33, 0x34,
0x31, 0x31, 0x38, 0x2c, 0x13, 0x35, 0x36, 0x39,
0x33, 0x44, 0x31, 0x41, 0x44, 0x2d, 0x30, 0x30,
0x30, 0x36, 0x37, 0x34, 0x45, 0x31
);
$msg_pack1 = pack("C*", @msg1);
$password1 = "cmedia";
###################################################
@msg2 = (0x28, 0x01, 0x00, 0x17,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x01, 0x03, 0x31
);
$msg_pack2 = pack("C*", @msg2);
$password2 = "123456";
###################################################
@msg3 = (0x28, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
);
$msg_pack3 = pack("C*", @msg3);
$password3 = "cmedia";
###################################################

$msg = $msg_pack3;
$password = $password3;
print "msg:  ";
print unpack("H*", $msg);

print "\n";
print "password: ", $password;

$all = $msg;
$all .= $password;
$authenticator = md5($all);

print "\n";
print "authenticator:  ";
print unpack("H*", $authenticator);
