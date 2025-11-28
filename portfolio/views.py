from django.shortcuts import render

def index(request):
    # Proyectos Web - Bootcamp Full Stack Python
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
            'titulo': 'Gestor de Tareas',
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
    
    # Proyectos Gamedev - Videojuegos Indie
    proyectos_gamedev = [
        {
            'titulo': 'Antes todo esto era campo',
            'descripcion': 'Videojuego que invita a reflexionar sobre el extractivismo y el territorio. Selección oficial en Chile Game Showcase e Indie Fest Chile.',
            'tipo': 'Videojuego',
            'tecnologias': ['Godot', 'GDScript', 'Diseño Sonoro', 'Pixel Art'],
            'link_github': 'https://github.com/Linwi-V',
            'link_demo': 'https://antestodoestoeracampo.itch.io/ateec',
            'imagen': 'img/ateec.jpg'
        },
        {
            'titulo': 'La Tirana: El tiempo baila',
            'descripcion': '2.5D RPG sobre identidad y territorio chileno. Desarrollado con Expropiación Digital. Selección oficial en Chile Game Showcase e Indie Fest Chile.',
            'tipo': 'Videojuego',
            'tecnologias': ['Godot', 'GDScript', 'Pixel Art', 'Sound Design'],
            'link_github': 'https://github.com/Linwi-V',
            'link_demo': '#',
            'imagen': 'img/latirana.jpg'
        },
    ]
    
    # Habilidades organizadas por categoría
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
            'Producción de Videojuegos',
            'Godot Engine',
            'Unity',
            "Ren'Py",
            'Documentación de Proyectos',
            'Trackeo de Equipo',
            'Gestión de Workflows'
        ],
        'audiovisual': [
            'Creación Sonora',
            'Sonido Directo',
            'Dirección de Arte',
            'Montaje',
            'Adobe Suite',
            'Documentales',
            'Producción Audiovisual'

        ],
        'organizacion': [
            'Trello',
            'Miro',
            'Notion',
            'Discord',
            'Google Workspace',
            'Canva',
            'Inglés Intermedio'
        ]
    }
    
    # Lo que hago - Enfocado en áreas de trabajo, no servicios técnicos
    servicios = [
        {
            'titulo': 'Producción de Juegos Indie',
            'descripcion': 'Coordino proyectos desde el pitch hasta el lanzamiento. Gestiono equipos remotos, organizo workflows y me aseguro de que las cosas avancen sin que el equipo se queme en el intento.',
            'icono': 'bi-controller'
        },
        {
            'titulo': 'Coordinación de Equipos Distribuidos',
            'descripcion': 'Manejo equipos en múltiples zonas horarias usando Notion, Discord y Trello. Organizo sprints, documentación y comunicación para que todos estén sincronizados.',
            'icono': 'bi-people'
        },
        {
            'titulo': 'Desarrollo de Herramientas Web',
            'descripcion': 'Construyo aplicaciones web con Django para resolver problemas reales de producción. Si necesitas un sistema de gestión, pipeline tracker o herramienta custom, lo hacemos.',
            'icono': 'bi-code-slash'
        },
        {
            'titulo': 'Diseño de Experiencias Inclusivas',
            'descripcion': 'Creo narrativas que visibilizan identidades diversas y diseño con enfoque en accesibilidad. Los juegos son un medio político y deben representar a todes.',
            'icono': 'bi-heart'
        }
    ]
    
    # Información de contacto
    contacto = {
        'email': 'tu-email@ejemplo.com',  # Cambia por tu email real
        'github': 'https://github.com/Linwi-V',
        'linkedin': 'https://www.linkedin.com/in/linwi-vargas-campos/',
        'itch': 'https://antestodoestoeracampo.itch.io/ateec',
        'behance': 'https://www.behance.net/linwivargas'
    }
    
    context = {
        'proyectos_web': proyectos_web,
        'proyectos_gamedev': proyectos_gamedev,
        'habilidades': habilidades,
        'servicios': servicios,
        'contacto': contacto,
    }
    
    return render(request, 'portfolio/index.html', context)