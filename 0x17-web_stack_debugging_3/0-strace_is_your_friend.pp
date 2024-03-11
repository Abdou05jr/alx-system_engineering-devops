#!/usr/bin/bash
# code

exec { 'fix code':
  command   => "/bin/sed -i  's/phpp/php/g' /var/www/html/wp-settings.php",
}
