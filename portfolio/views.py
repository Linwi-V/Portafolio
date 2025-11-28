from django.shortcuts import render

def index(request):
    # Proyectos Web 
    proyectos_web = [
        {
            'titulo': 'Game Production Manager',
            'descripcion': 'Sistema web para gestión de producción de videojuegos indie. Incluye seguimiento de tareas, cronogramas y coordinación de equipos remotos.',
            'tipo': 'Web App',
            'tecnologias': ['Django', 'Python', 'PostgreSQL', 'Bootstrap'],
            'link_github': 'https://github.com/Linwi-V/GameProductionManager',
            'link_demo': '#',
            'imagen': 'img/gpm.jpg'
        },
        {
            'titulo': 'Gestor de Tareas con sesiones',
            'descripcion': 'Sistema de gestión de tareas con autenticación completa. Cada usuario puede crear, visualizar y gestionar sus tareas personales de forma privada.',
            'tipo': 'Web App',
            'tecnologias': ['Django', 'Python', 'Bootstrap', 'Autenticación'],
            'link_github': 'https://github.com/Linwi-V/Evaluacion_PortafolioM6',
            'link_demo': '#',
            'imagen': 'img/gestor-tareas.jpg'
        },
        {
            'titulo': 'Gestor de Productos',
            'descripcion': 'Sistema CRUD completo para gestión de productos con categorías, etiquetas y detalles. Incluye relaciones complejas de base de datos y validación de formularios.',
            'tipo': 'Web App',
            'tecnologias': ['Django', 'PostgreSQL', 'Bootstrap', 'CRUD'],
            'link_github': 'https://github.com/Linwi-V/Evaluacion_Modulo7',
            'link_demo': '#',
            'imagen': 'img/gestor-productos.jpg'
        },
    ]
    
    # Proyectos Gamedev 
    proyectos_gamedev = [
        {
            'titulo': 'Antes todo esto era campo',
            'descripcion': 'En un pueblo donde las leyendas dictan la realidad, unx joven tiene la opción de desaprender prejuicios para enfrentar corporaciones extractivistas que manejan todo desde las sombras.',
            'tipo': 'Videojuego',
            'tecnologias': ['Renpy', 'Novela Visual'],
            'link_demo': 'https://antestodoestoeracampo.itch.io/ateec',
            'imagen': 'img/ateec.jpg'
        },
        {
            'titulo': 'La Tirana: El tiempo baila',
            'descripcion': 'Katari descubre que su abuelo es un guardián del tiempo-espacio. Cuando es secuestrado, ella debe atravesar épocas y lugares para recuperar objetos robados y detener a un enemigo ancestral.',
            'tipo': 'Videojuego',
            'tecnologias': ['Godot', 'Pixel Art', '2.5D', 'RPG'],
            'link_demo': '#',
            'imagen': 'img/latirana.jpg'
        },
    ]
    
    # Habilidades 
    habilidades = {
        'frontend': [
            'HTML',
            'CSS',
            'Bootstrap',
            'JavaScript',
            'UI/UX',
            'Diseño Responsivo'
        ],
        'backend': [
            'Python',
            'Django',
            'MySQL',
            'SQLite',
            'PostgreSQL',
            'Git/GitHub'
        ],
        'gameproducer': [
            'Unity',
            "Ren'Py",
            'Trabajo en Equipo',
            'Godot',
            'Documentación de Proyectos',
        ],
        'audiovisual': [
            'Creación Sonora',
            'Dirección de Arte',
            'Montaje',
            'Adobe Suite',
            'Documentales'

        ],
        'organizacion': [
            'Trello',
            'Miro',
            'Notion',
            'Discord',
            'Google Workspace',
            'RRSS',
            'Canva',
            'Inglés Intermedio'
        ]
    }
    
    # Lo que hago 
    servicios = [
        {
            'titulo': 'Producción de Videojuegos',
            'descripcion': 'Coordino proyectos desde la idea inicial hasta el lanzamiento y mas allá. Organizo personas y me aseguro de que las cosas avancen sin que el equipo se queme en el intento.',
            'icono': 'bi-controller'
        },
        {
            'titulo': 'Desarrollo Web',
            'descripcion': 'Diseño y construyo aplicaciones web con Python y Django. Desde sistemas de gestión hasta herramientas custom que resuelven problemas reales, especial enfoque en la parte frontend.',
            'icono': 'bi-code-slash'
        },
        {
            'titulo': 'Gestión de Proyectos',
            'descripcion': 'Organizo equipos de manera remota. Diseño pipelines de trabajo, documentación y comunicación para mantener proyectos vivos y sincronizados.',
            'icono': 'bi-diagram-3'
        },
        {
            'titulo': 'Realización Audiovisual',
            'descripcion': 'Me especializo en creación sonora, montaje y dirección de arte. Me motiva particularmente el cine documental y los videoclips. Tambien creo contenido para redes sociales y canales de YouTube.',
            'icono': 'bi-film'
        }
    ]
    
    # Información de contacto
    contacto = {
        'email': 'linwi.vargas@gmail.com',  
        'github': 'https://github.com/Linwi-V',
        'linkedin': 'https://www.linkedin.com/in/linwi-vargas-campos/',
        'itch': 'https://linwi.itch.io/',
        'behance': 'https://www.behance.net/linwi1'
    }
    
    context = {
        'proyectos_web': proyectos_web,
        'proyectos_gamedev': proyectos_gamedev,
        'habilidades': habilidades,
        'servicios': servicios,
        'contacto': contacto,
    }
    
    return render(request, 'portfolio/index.html', context)