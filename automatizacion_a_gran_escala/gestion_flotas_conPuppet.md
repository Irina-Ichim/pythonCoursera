## Gestión de Flotas de Computadoras con Puppet

Cuando gestionamos flotas de computadoras, es común aplicar reglas diferentes a varios sistemas según sus roles. En Puppet, los nodos representan sistemas donde puede ejecutarse un agente de Puppet, como estaciones de trabajo, servidores, máquinas virtuales o enrutadores de red. Puppet nos permite definir reglas predeterminadas para todos los nodos y reglas específicas para subconjuntos de sistemas.

### Definiciones de Nodos en Puppet

1. **Definición Predeterminada de Nodo:**
   - Por lo general, hay una definición predeterminada de nodo que especifica las clases para todos los nodos.
   - Ejemplo de fragmento de `site.pp`:
     ```puppet
     node default {
       include sudo
       include ntp
     }
     ```

2. **Definiciones Condicionales de Nodo:**
   - Los nodos específicos se identifican por sus Nombres de Dominio Completamente Calificados (FQDN).
   - Se pueden agregar definiciones adicionales para roles específicos.
   - Ejemplo:
     ```puppet
     node 'webserver.example.com' {
       include sudo
       include ntp
       include apache
     }
     ```

### Organización del Código

- **Evitar Repetición:**
  - Para evitar la repetición, se puede definir una clase base para incluir clases comunes.
  - Ejemplo:
    ```puppet
    class base {
      include sudo
      include ntp
    }

    node 'webserver.example.com' {
      include base
      include apache
    }
    ```

### Almacenamiento de Archivos

- Las definiciones de nodos se almacenan típicamente en un archivo llamado `site.pp`.
- `site.pp` no forma parte de ningún módulo; define qué clases se aplican a qué nodos.
- Esta separación ayuda a organizar el código para facilitar el mantenimiento.

### Infraestructura de Puppet

- Puppet utiliza infraestructura para verificar si un nodo realmente tiene el nombre que afirma tener.
- Esto garantiza que se apliquen las reglas correctas a cada nodo según su definición.

Al utilizar definiciones de nodos en Puppet, los administradores pueden gestionar eficientemente diversas flotas de computadoras, aplicando reglas personalizadas a sistemas específicos mientras mantienen un conjunto común de reglas para otros.