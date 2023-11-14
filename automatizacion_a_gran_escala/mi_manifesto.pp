# Archivo: mi_manifesto.pp

# Configuración del Maestro Puppet
class { 'main':
  autosign => true,
}

# Configuración del Cliente Puppet (Asumiendo un sistema Debian/Ubuntu)
class { 'main':
  server => 'ubuntu.example.com',
}

# Verificación de Conexión desde el Cliente al Maestro
exec { 'test_puppet_connection':
  command     => 'puppet agent -v --test',
  refreshonly => true,
}

# Configuración del Maestro (site.pp)
file { '/etc/puppet/code/environments/production/manifests/site.pp':
  ensure  => present,
  content => '
    node "webserver.example.com" {
      include apache
    }

    node default {
      # Definición vacía por ahora
    }
  ',
}

# Ejecución del Agente Puppet en el Cliente
exec { 'run_puppet_agent':
  command => 'puppet agent -v --test',
}

# Habilitar y Arrancar el Servicio Puppet en el Cliente
service { 'puppet':
  ensure  => running,
  enable  => true,
  require => Exec['run_puppet_agent'],
}





