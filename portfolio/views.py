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
        'programacion': ['Python', 'Django', 'GDScript', 'JavaScript', 'HTML/CSS', 'PostgreSQL'],
        'gamedev': ['Godot Engine', 'Game Design', 'Producción', 'Level Design', 'Narrative Design'],
        'audio': ['Diseño de Sonido', 'Edición de Audio', 'Implementación de SFX', 'Ambientes Sonoros'],
        'herramientas': ['Notion', 'Discord', 'Trello', 'Git/GitHub', 'Adobe Suite', 'Canva', 'Figma']
    }
    
    # Servicios ofrecidos
    servicios = [
        {
            'titulo': 'Producción de Videojuegos',
            'descripcion': 'Gestión de proyectos indie desde el pitch hasta el lanzamiento. Coordino equipos remotos, manejo cronogramas y me aseguro de que las cosas sucedan.',
            'icono': 'bi-controller'
        },
        {
            'titulo': 'Diseño de Sonido',
            'descripcion': 'Creación de paisajes sonoros y efectos que hacen que tus juegos suenen tan bien como se ven. Desde ambientes sutiles hasta SFX que dan feedback claro.',
            'icono': 'bi-soundwave'
        },
        {
            'titulo': 'Desarrollo Web',
            'descripcion': 'Aplicaciones web con Django para resolver problemas reales. Si necesitas un sistema de gestión, un portafolio o una herramienta custom, hablemos.',
            'icono': 'bi-code-slash'
        },
        {
            'titulo': 'Narrativa y Diseño Inclusivo',
            'descripcion': 'Narrativas que visibilizan identidades diversas y diseño con enfoque en accesibilidad. Porque los juegos son para todes.',
            'icono': 'bi-people'
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