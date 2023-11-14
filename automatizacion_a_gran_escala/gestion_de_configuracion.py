"""
Gestión de Configuración en IT

En este script, exploraremos el concepto de gestión de configuración en el ámbito de la tecnología de la información (IT).
Explicaremos la diferencia entre configuración administrada y no administrada, así como la importancia de las herramientas de gestión de configuración.

Configuración no administrada:
Cuando un equipo instala manualmente un sistema operativo, configura aplicaciones y servicios, y realiza la configuración necesaria,
consideramos que la configuración es no administrada. Esto puede funcionar para un pequeño número de servidores, pero no es escalable.

Configuración administrada:
Implica el uso de un sistema de gestión de configuración para manejar automáticamente la configuración de los dispositivos en una flota (nodos).
Algunas herramientas populares incluyen Puppet, Chef, Ansible y CFEngine. En este curso, nos centraremos en Puppet.

Beneficios de la gestión de configuración:
1. Escalabilidad: Facilita el despliegue y la gestión de configuraciones en grandes flotas de dispositivos.
2. Eficiencia: Permite realizar cambios de manera eficiente y consistente en toda la infraestructura.
3. Coherencia: Asegura que la configuración sea coherente en todos los dispositivos administrados.
4. Corrección automática de errores: Algunas herramientas tienen capacidades integradas para corregir automáticamente ciertos errores.

Integración con la nube:
Estas herramientas también pueden integrarse con entornos en la nube como Amazon EC2, Microsoft Azure o Google Cloud Platform.

Selección de herramientas:
La elección de una herramienta de gestión de configuración debe basarse en las necesidades específicas de la infraestructura.
Cada herramienta tiene sus propias fortalezas y debilidades.

¡La gestión de configuración es esencial para mantener una infraestructura creciente y asegurar cambios eficientes y consistentes!
"""

def main():
    print("¡Bienvenido a la gestión de configuración en IT!")

if __name__ == "__main__":
    main()


    
# Este es un archivo de ejemplo que explica el concepto de Infrastructure as Code (IaC) en Python.

# Configuración inicial del servidor
server_config = {
    "operating_system": "Linux",
    "applications": ["Web Server", "Database"],
    "networking": {"firewall": "enabled", "ports": [80, 443]},
    # Otros detalles de configuración...
}

# Definición de un archivo de configuración en formato IaC (Infrastructure as Code)
iac_config_file = """
# Archivo de configuración IaC

# Configuración del servidor
server_config = {
    "operating_system": "Linux",
    "applications": ["Web Server", "Database"],
    "networking": {"firewall": "enabled", "ports": [80, 443]},
    # Otros detalles de configuración...
}
"""

# Función para aplicar la configuración en un servidor
def apply_configuration(config):
    # Lógica para aplicar la configuración a un servidor
    print("Aplicando configuración:", config)

# Aplicar la configuración definida inicialmente
apply_configuration(server_config)

# Mostrar el contenido del archivo de configuración IaC
print("Contenido del archivo IaC:")
print(iac_config_file)

# Simulación de almacenamiento en un sistema de control de versiones (VCS)
# (En la práctica, esto se haría con un sistema como Git)
vcs_commit = """
# Commit en el sistema de control de versiones
# Se agregó la configuración inicial del servidor
"""

# Mostrar el commit en el VCS
print("Commit en el sistema de control de versiones:")
print(vcs_commit)
    
# La importancia de la gestión de configuración y cómo se aplica el concepto de "Infrastructure as Code" (IaC). Aquí tienes un resumen:

# 1. **Configuración Gestionada vs. No Gestionada:**
#    - Configuración no gestionada: Instalación manual del sistema operativo, configuración de aplicaciones y servicios.
#    - Configuración gestionada: Uso de un sistema de gestión de configuración (como Puppet) para automatizar la configuración y mantener
# un estado deseado.

# 2. **Infrastructure as Code (IaC):**
#    - Paradigma donde toda la configuración necesaria para implementar y gestionar un nodo en la infraestructura se almacena en archivos 
# controlados por versiones.
#    - Los archivos IaC pueden ser rastreados en un sistema de control de versiones (VCS) para auditar cambios, revertir cambios incorrectos
# y mejorar la colaboración.

# 3. **Tratamiento de los Computadores:**
#    - En entornos IaC, los computadores se tratan como "cattle" (ganado) en lugar de "pets" (mascotas).
#    - Implica cuidarlos como un grupo en lugar de forma individual, ideal para entornos en la nube donde las máquinas son recursos 
# intercambiables.

# 4. **Ventajas de IaC:**
#    - Consistencia: La configuración es coherente en todos los dispositivos.
#    - Versionado: Permite realizar un seguimiento de los cambios y revertirlos si es necesario.
#    - Confiabilidad: Las implementaciones son repetibles y consistentes.

# 5. **Pruebas Automatizadas:**
#    - Los archivos de configuración almacenados como código permiten la ejecución de pruebas automatizadas para identificar errores 
# antes de la implementación.

# 6. **Escalabilidad:**
#    - La gestión de configuración y la implementación automatizada permiten escalar la infraestructura de manera eficiente y consistente.

# 7. **Adaptabilidad:**
#    - El enfoque IaC ayuda a los equipos de IT a adaptarse y mantenerse flexibles en un entorno tecnológico que cambia constantemente.

# Este resumen destaca la importancia de tratar la infraestructura como código, lo que facilita la gestión, escalabilidad y adaptabilidad d
# e la infraestructura de IT.