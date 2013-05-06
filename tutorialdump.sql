PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

INSERT INTO "users" VALUES(1,'gulnara@gulnara.me','Mylife$33');

INSERT INTO "tutorials" VALUES(1,1,'1','Hi! 

Let''s try to print "Hello World!"

In the input field type:

`show "Hello World!"`');
INSERT INTO "tutorials" VALUES(2,NULL,'2','Let''s do some math!

In the input field type:

`a <- 6`  

`b <- 2`  

`c <- a / b`  

`show a`  

`show b`  

`show c` ');
INSERT INTO "tutorials" VALUES(12,NULL,'3','Let''s try our first conditional!  

In the input field type:  

`a <- 10`  

`is a < 20 ? then:`  

`show ''Yes, a is less than 20''`  

`end`
');
INSERT INTO "tutorials" VALUES(13,NULL,'4','Let''s try some loops!
');
COMMIT;
