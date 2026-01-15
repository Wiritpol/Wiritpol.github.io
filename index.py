from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wiritpol Nukhongkha | AI Engineer Portfolio</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #6366f1;
            --secondary: #8b5cf6;
            --accent: #ec4899;
            --dark: #0f172a;
            --light: #f8fafc;
            --gray: #64748b;
            --success: #10b981;
        }

        body {
            font-family: 'Poppins', sans-serif;
            line-height: 1.6;
            color: var(--dark);
            background: var(--dark);
            overflow-x: hidden;
        }

        /* Animated Background */
        .animated-bg {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .animated-bg::before {
            content: '';
            position: absolute;
            width: 200%;
            height: 200%;
            top: -50%;
            left: -50%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(99, 102, 241, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(236, 72, 153, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 40% 20%, rgba(139, 92, 246, 0.3) 0%, transparent 50%);
            animation: rotate 20s linear infinite;
        }

        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* Floating particles */
        .particles {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
        }

        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            animation: float 15s infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0) translateX(0); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100vh) translateX(100px); opacity: 0; }
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(10px);
            z-index: 1000;
            padding: 20px 0;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }

        nav.scrolled {
            padding: 15px 0;
            background: rgba(15, 23, 42, 0.98);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5em;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            cursor: pointer;
        }

        .nav-links {
            display: flex;
            gap: 30px;
            list-style: none;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s;
            position: relative;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            transition: width 0.3s;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 100px 40px 60px;
            position: relative;
        }

        .hero-content {
            max-width: 1200px;
            text-align: center;
            color: white;
            z-index: 1;
        }

        .hero-badge {
            display: inline-block;
            padding: 8px 20px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 50px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            margin-bottom: 20px;
            animation: fadeInDown 1s ease;
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero h1 {
            font-size: 4.5em;
            font-weight: 800;
            margin-bottom: 20px;
            animation: fadeInUp 1s ease 0.2s both;
            line-height: 1.2;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero .subtitle {
            font-size: 1.8em;
            margin-bottom: 15px;
            opacity: 0.9;
            animation: fadeInUp 1s ease 0.4s both;
        }

        .hero .description {
            font-size: 1.2em;
            opacity: 0.8;
            margin-bottom: 40px;
            animation: fadeInUp 1s ease 0.6s both;
        }

        .hero-buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
            animation: fadeInUp 1s ease 0.8s both;
        }

        .btn {
            padding: 15px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            border: none;
            cursor: pointer;
            font-size: 1.05em;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.4);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(99, 102, 241, 0.6);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            color: white;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-3px);
        }

        .social-links {
            margin-top: 40px;
            display: flex;
            gap: 20px;
            justify-content: center;
            animation: fadeInUp 1s ease 1s both;
        }

        .social-link {
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 50%;
            color: white;
            font-size: 1.3em;
            transition: all 0.3s;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .social-link:hover {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            transform: translateY(-5px) scale(1.1);
            box-shadow: 0 10px 25px rgba(99, 102, 241, 0.4);
        }

        /* Sections */
        section {
            padding: 100px 40px;
            position: relative;
        }

        .section-light {
            background: var(--light);
        }

        .section-dark {
            background: var(--dark);
            color: white;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-header {
            text-align: center;
            margin-bottom: 60px;
        }

        .section-badge {
            display: inline-block;
            padding: 8px 20px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: white;
            border-radius: 50px;
            font-size: 0.9em;
            font-weight: 600;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .section-title {
            font-size: 3em;
            font-weight: 800;
            margin-bottom: 20px;
        }

        .section-light .section-title {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .section-subtitle {
            font-size: 1.2em;
            opacity: 0.8;
            max-width: 600px;
            margin: 0 auto;
        }

        /* About Section */
        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
        }

        .about-image {
            position: relative;
        }

        .profile-placeholder {
            width: 100%;
            aspect-ratio: 1;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 8em;
            color: white;
            box-shadow: 0 20px 60px rgba(99, 102, 241, 0.4);
            animation: float-slow 6s ease-in-out infinite;
            overflow: hidden;
            position: relative;
        }

        .profile-placeholder img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            position: absolute;
            top: 0;
            left: 0;
        }

        @keyframes float-slow {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }

        .about-content h3 {
            font-size: 2em;
            margin-bottom: 20px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .about-content p {
            font-size: 1.1em;
            line-height: 1.8;
            color: var(--gray);
            margin-bottom: 20px;
        }

        .highlight-box {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(236, 72, 153, 0.1));
            padding: 30px;
            border-radius: 20px;
            border-left: 4px solid var(--primary);
            margin: 30px 0;
        }

        .highlight-box h4 {
            color: var(--primary);
            margin-bottom: 15px;
            font-size: 1.3em;
        }

        .highlight-item {
            display: flex;
            align-items: start;
            gap: 15px;
            margin-bottom: 15px;
        }

        .highlight-item i {
            color: var(--primary);
            font-size: 1.2em;
            margin-top: 5px;
        }

        /* Skills Section */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
        }

        .skill-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 25px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s;
            cursor: pointer;
        }

        .skill-card:hover {
            transform: translateY(-10px);
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 60px rgba(99, 102, 241, 0.3);
            border-color: var(--primary);
        }

        .skill-icon {
            width: 70px;
            height: 70px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2em;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3);
        }

        .skill-card h3 {
            font-size: 1.5em;
            margin-bottom: 15px;
            color: white;
        }

        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 20px;
        }

        .tag {
            padding: 8px 16px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            font-size: 0.9em;
            color: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s;
        }

        .tag:hover {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-color: transparent;
            transform: scale(1.05);
        }

        /* Projects Section */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 40px;
        }

        .project-card {
            background: white;
            border-radius: 25px;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            transition: all 0.4s;
            cursor: pointer;
        }

        .project-card:hover {
            transform: translateY(-15px);
            box-shadow: 0 25px 60px rgba(99, 102, 241, 0.3);
        }

        .project-image {
            height: 200px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4em;
            color: white;
            position: relative;
            overflow: hidden;
        }

        .project-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            position: absolute;
            top: 0;
            left: 0;
        }

        .project-image::before {
            content: '';
            position: absolute;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
            animation: rotate 10s linear infinite;
            z-index: 0;
        }

        .project-image .emoji {
            position: relative;
            z-index: 1;
        }

        .project-content {
            padding: 30px;
        }

        .project-title {
            font-size: 1.5em;
            font-weight: 700;
            margin-bottom: 15px;
            color: var(--dark);
        }

        .project-desc {
            color: var(--gray);
            line-height: 1.7;
            margin-bottom: 20px;
        }

        .project-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 20px;
        }

        .tech-tag {
            padding: 6px 12px;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(236, 72, 153, 0.1));
            border-radius: 15px;
            font-size: 0.85em;
            color: var(--primary);
            font-weight: 500;
        }

        .project-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--primary);
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s;
        }

        .project-link:hover {
            gap: 12px;
        }

        /* Education Section */
        .timeline {
            position: relative;
            padding: 40px 0;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(180deg, var(--primary), var(--accent));
        }

        .timeline-item {
            display: flex;
            margin-bottom: 50px;
            position: relative;
        }

        .timeline-content {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 25px;
            width: 45%;
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
        }

        .timeline-item:nth-child(odd) .timeline-content {
            margin-right: auto;
        }

        .timeline-item:nth-child(even) .timeline-content {
            margin-left: auto;
        }

        .timeline-dot {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            width: 20px;
            height: 20px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 50%;
            border: 4px solid var(--dark);
            z-index: 1;
        }

        .timeline-content h3 {
            color: white;
            font-size: 1.8em;
            margin-bottom: 10px;
        }

        .timeline-content .year {
            color: var(--accent);
            font-weight: 600;
            margin-bottom: 15px;
        }

        /* Contact Section */
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-top: 60px;
        }

        .contact-card {
            background: white;
            padding: 40px;
            border-radius: 25px;
            text-align: center;
            transition: all 0.3s;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        }

        .contact-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 60px rgba(99, 102, 241, 0.3);
        }

        .contact-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            font-size: 2em;
            color: white;
        }

        .contact-card h3 {
            font-size: 1.3em;
            margin-bottom: 10px;
            color: var(--dark);
        }

        .contact-card a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s;
        }

        .contact-card a:hover {
            color: var(--accent);
        }

        /* Footer */
        footer {
            background: #000;
            color: white;
            padding: 60px 40px 30px;
            text-align: center;
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
        }

        .footer-logo {
            font-size: 2em;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }

        .footer-text {
            opacity: 0.7;
            margin-top: 30px;
            padding-top: 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Back to Top */
        .back-to-top {
            position: fixed;
            bottom: 40px;
            right: 40px;
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5em;
            cursor: pointer;
            opacity: 0;
            pointer-events: none;
            transition: all 0.3s;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.4);
            z-index: 999;
        }

        .back-to-top.visible {
            opacity: 1;
            pointer-events: all;
        }

        .back-to-top:hover {
            transform: translateY(-5px) scale(1.1);
            box-shadow: 0 15px 40px rgba(99, 102, 241, 0.6);
        }

        /* Responsive */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .hero h1 {
                font-size: 2.5em;
            }

            .hero .subtitle {
                font-size: 1.3em;
            }

            .about-grid {
                grid-template-columns: 1fr;
            }

            .timeline::before {
                left: 20px;
            }

            .timeline-content {
                width: calc(100% - 60px);
                margin-left: 60px !important;
            }

            .timeline-dot {
                left: 20px;
            }

            .section-title {
                font-size: 2em;
            }
        }

        /* Loading Animation */
        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.5;
            }
        }

        .animate-on-scroll {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.6s ease;
        }

        .animate-on-scroll.animated {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>
    <div class="animated-bg"></div>
    <div class="particles"></div>

    <!-- Navigation -->
    <nav id="navbar">
        <div class="nav-container">
            <div class="logo">OHM.AI</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#education">Education</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="hero-content">
            <div class="hero-badge">👋 Welcome to my Portfolio</div>
            <h1>WIRITPOL NUKHONGKHA</h1>
            <p class="subtitle">AI Engineering Student • Machine Learning Enthusiast</p>
            <p class="description">นักศึกษาชั้นปีที่ 4 สาขาวิศวกรรมปัญญาประดิษฐ์<br>มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตหาดใหญ่</p>
            
            <div class="hero-buttons">
                <a href="#projects" class="btn btn-primary">
                    <i class="fas fa-rocket"></i> View My Work
                </a>
                <a href="#contact" class="btn btn-secondary">
                    <i class="fas fa-envelope"></i> Get In Touch
                </a>
            </div>

            <div class="social-links">
                <a href="mailto:ohmnukongka@gmail.com" class="social-link"><i class="fas fa-envelope"></i></a>
                <a href="https://www.linkedin.com/in/wiritpol-nukhongkha" target="_blank" class="social-link"><i class="fab fa-linkedin"></i></a>
                <a href="https://github.com/Wiritpol" target="_blank" class="social-link"><i class="fab fa-github"></i></a>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section-light">
        <div class="container">
            <div class="section-header animate-on-scroll">
                <span class="section-badge">About Me</span>
                <h2 class="section-title">Who Am I?</h2>
                <p class="section-subtitle">Passionate about creating intelligent systems that solve real-world problems</p>
            </div>

            <div class="about-grid">
                <div class="about-image animate-on-scroll">
                    <div class="profile-placeholder">
                        <!-- แทนที่ด้วยรูปของคุณ -->
                        <img src="/static/images/profile.jpg" alt="Profile" onerror="this.style.display='none'; this.parentElement.innerHTML='🤖';">
                    </div>
                </div>

                <div class="about-content animate-on-scroll">
                    <h3>Hello! I'm Ohm</h3>
                    <p>ผมคือนักศึกษาสาขาวิศวกรรมปัญญาประดิษฐ์ที่หลงใหลในการพัฒนาระบบ AI ที่สามารถเปลี่ยนแปลงโลกได้ ด้วยความสนใจในทั้ง Machine Learning, Deep Learning, Computer Vision และ Natural Language Processing</p>

                    <div class="highlight-box">
                        <h4>🎯 สิ่งที่ฉันทำ</h4>
                        <div class="highlight-item">
                            <i class="fas fa-brain"></i>
                            <div>
                                <strong>Learn</strong> - สอนคอมพิวเตอร์ให้เรียนรู้และเข้าใจข้อมูลมหาศาล
                            </div>
                        </div>
                        <div class="highlight-item">
                            <i class="fas fa-chart-line"></i>
                            <div>
                                <strong>Analyze</strong> - วิเคราะห์และค้นหารูปแบบที่ซ่อนอยู่ในข้อมูล
                            </div>
                        </div>
                        <div class="highlight-item">
                            <i class="fas fa-cogs"></i>
                            <div>
                                <strong>Build</strong> - สร้างระบบอัจฉริยะที่แก้ปัญหาได้จริง
                            </div>
                        </div>
                    </div>

                    <p>ด้วยประสบการณ์จากโปรเจกต์หลากหลายรูปแบบ ตั้งแต่การพัฒนา Chatbot, ระบบ OCR, ไปจนถึงการทำ Predictive Analytics ผมพร้อมที่จะนำความรู้เหล่านี้ไปสร้างสรรค์สิ่งใหม่ๆ</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="section-dark">
        <div class="container">
            <div class="section-header animate-on-scroll">
                <span class="section-badge">My Arsenal</span>
                <h2 class="section-title">Skills & Technologies</h2>
                <p class="section-subtitle">Tools and technologies I use to bring ideas to life</p>
            </div>

            <div class="skills-grid">
                <div class="skill-card animate-on-scroll">
                    <div class="skill-icon">💻</div>
                    <h3>Programming</h3>
                    <div class="skill-tags">
                        <span class="tag">Python</span>
                        <span class="tag">C++</span>
                        <span class="tag">C</span>
                        <span class="tag">HTML/CSS</span>
                    </div>
                </div>

                <div class="skill-card animate-on-scroll">
                    <div class="skill-icon">🤖</div>
                    <h3>AI & ML</h3>
                    <div class="skill-tags">
                        <span class="tag">Machine Learning</span>
                        <span class="tag">Deep Learning</span>
                        <span class="tag">Computer Vision</span>
                        <span class="tag">NLP</span>
                        <span class="tag">OCR</span>
                    </div>
                </div>

                <div class="skill-card animate-on-scroll">
                    <div class="skill-icon">📚</div>
                    <h3>Frameworks</h3>
                    <div class="skill-tags">
                        <span class="tag">TensorFlow</span>
                        <span class="tag">PyTorch</span>
                        <span class="tag">Scikit-learn</span>
                        <span class="tag">Pandas</span>
                    </div>
                </div>

                <div class="skill-card animate-on-scroll">
                    <div class="skill-icon">🗄️</div>
                    <h3>Data & Database</h3>
                    <div class="skill-tags">
                        <span class="tag">SQL</span>
                        <span class="tag">Data Preprocessing</span>
                        <span class="tag">Visualization</span>
                    </div>
                </div>

                <div class="skill-card animate-on-scroll">
                    <div class="skill-icon">🛠️</div>
                    <h3>Tools</h3>
                    <div class="skill-tags">
                        <span class="tag">Git</span>
                        <span class="tag">Docker</span>
                        <span class="tag">Jupyter</span>
                        <span class="tag">Colab</span>
                    </div>
                </div>

                <div class="skill-card animate-on-scroll">
                    <div class="skill-icon">🔒</div>
                    <h3>Additional</h3>
                    <div class="skill-tags">
                        <span class="tag">Cybersecurity</span>
                        <span class="tag">HPC</span>
                        <span class="tag">OOP</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section-light">
        <div class="container">
            <div class="section-header animate-on-scroll">
                <span class="section-badge">Portfolio</span>
                <h2 class="section-title">Featured Projects</h2>
                <p class="section-subtitle">Some of my recent work that I'm proud of</p>
            </div>

            <div class="projects-grid">
                <div class="project-card animate-on-scroll">
                    <div class="project-image">🎓</div>
                    <div class="project-content">
                        <h3 class="project-title">Student Dropout Prediction</h3>
                        <p class="project-desc">ระบบทำนายความเสี่ยงในการถูกไล่ออกของนักศึกษาด้วย Deep Learning พร้อม Dashboard แบบ Interactive</p>
                        <div class="project-tech">
                            <span class="tech-tag">Deep Learning</span>
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Dashboard</span>
                        </div>
                        <a href="https://gitlab.com/ohmnukongka/group4-dashboard.git" target="_blank" class="project-link">
                            View Project <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>

                <div class="project-card animate-on-scroll">
                    <div class="project-image">📹</div>
                    <div class="project-content">
                        <h3 class="project-title">Sum4you</h3>
                        <p class="project-desc">AI-powered YouTube Video Summarizer ที่แปลงวิดีโอเป็นข้อความที่อ่านง่าย ช่วยประหยัดเวลาในการเรียนรู้</p>
                        <div class="project-tech">
                            <span class="tech-tag">NLP</span>
                            <span class="tech-tag">API</span>
                            <span class="tech-tag">Web App</span>
                        </div>
                        <a href="#" class="project-link">
                            Learn More <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>

                <div class="project-card animate-on-scroll">
                    <div class="project-image">🔢</div>
                    <div class="project-content">
                        <h3 class="project-title">Math OCR System</h3>
                        <p class="project-desc">ระบบอ่านโจทย์คณิตศาสตร์จากภาพและตรวจคำตอบอัตโนมัติ เพิ่มประสิทธิภาพการเรียนการสอน</p>
                        <div class="project-tech">
                            <span class="tech-tag">OCR</span>
                            <span class="tech-tag">Computer Vision</span>
                            <span class="tech-tag">TensorFlow</span>
                        </div>
                        <a href="#" class="project-link">
                            Learn More <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>

                <div class="project-card animate-on-scroll">
                    <div class="project-image">🎌</div>
                    <div class="project-content">
                        <h3 class="project-title">AI Anime Recommender</h3>
                        <p class="project-desc">Chatbot บน LINE ที่ใช้ AI Semantic Search และ Graph Database แนะนำอนิเมะที่ตรงใจ</p>
                        <div class="project-tech">
                            <span class="tech-tag">LINE Bot</span>
                            <span class="tech-tag">Semantic Search</span>
                            <span class="tech-tag">Graph DB</span>
                        </div>
                        <a href="#" class="project-link">
                            Learn More <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>

                <div class="project-card animate-on-scroll">
                    <div class="project-image">🎨</div>
                    <div class="project-content">
                        <h3 class="project-title">Drawing Application</h3>
                        <p class="project-desc">โปรแกรมวาดรูปแบบ Paint พัฒนาด้วย C++ สำหรับฝึกทักษะ Programming และ UI Design</p>
                        <div class="project-tech">
                            <span class="tech-tag">C++</span>
                            <span class="tech-tag">GUI</span>
                            <span class="tech-tag">Graphics</span>
                        </div>
                        <a href="https://github.com/Wiritpol/DrawApp" target="_blank" class="project-link">
                            View Code <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Education Section -->
    <section id="education" class="section-dark">
        <div class="container">
            <div class="section-header animate-on-scroll">
                <span class="section-badge">Education</span>
                <h2 class="section-title">Academic Journey</h2>
                <p class="section-subtitle">My path in Artificial Intelligence Engineering</p>
            </div>

            <div class="timeline">
                <div class="timeline-item animate-on-scroll">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <h3>🎓 วิศวกรรมปัญญาประดิษฐ์</h3>
                        <p class="year">2021 - Present (Year 4)</p>
                        <p>มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตหาดใหญ่</p>
                        <p style="margin-top: 15px; opacity: 0.8;">เรียนรู้การพัฒนาระบบ AI ตั้งแต่พื้นฐานจนถึงขั้นสูง พร้อมประสบการณ์จริงจากโปรเจกต์หลากหลาย</p>
                    </div>
                </div>

                <div class="timeline-item animate-on-scroll">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <h3>📚 Key Courses</h3>
                        <ul style="margin-top: 15px; line-height: 2; opacity: 0.9;">
                            <li>• Machine Learning & Deep Learning</li>
                            <li>• Computer Vision</li>
                            <li>• Natural Language Processing</li>
                            <li>• AI for Robot Controlling</li>
                            <li>• Cybersecurity</li>
                            <li>• High-Performance Computing</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section-light">
        <div class="container">
            <div class="section-header animate-on-scroll">
                <span class="section-badge">Get In Touch</span>
                <h2 class="section-title">Let's Connect</h2>
                <p class="section-subtitle">Feel free to reach out for collaborations or just a friendly hello</p>
            </div>

            <div class="contact-grid">
                <div class="contact-card animate-on-scroll">
                    <div class="contact-icon">
                        <i class="fas fa-envelope"></i>
                    </div>
                    <h3>Email</h3>
                    <a href="mailto:ohmnukongka@gmail.com">ohmnukongka@gmail.com</a>
                </div>

                <div class="contact-card animate-on-scroll">
                    <div class="contact-icon">
                        <i class="fab fa-linkedin"></i>
                    </div>
                    <h3>LinkedIn</h3>
                    <a href="https://www.linkedin.com/in/wiritpol-nukhongkha" target="_blank">Wiritpol Nukhongkha</a>
                </div>

                <div class="contact-card animate-on-scroll">
                    <div class="contact-icon">
                        <i class="fab fa-github"></i>
                    </div>
                    <h3>GitHub</h3>
                    <a href="https://github.com/Wiritpol" target="_blank">@Wiritpol</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-logo">OHM.AI</div>
            <div class="social-links">
                <a href="mailto:ohmnukongka@gmail.com" class="social-link"><i class="fas fa-envelope"></i></a>
                <a href="https://www.linkedin.com/in/wiritpol-nukhongkha" target="_blank" class="social-link"><i class="fab fa-linkedin"></i></a>
                <a href="https://github.com/Wiritpol" target="_blank" class="social-link"><i class="fab fa-github"></i></a>
            </div>
            <p class="footer-text">© 2024 Wiritpol Nukhongkha. Crafted with ❤️ and Python</p>
        </div>
    </footer>

    <div class="back-to-top" onclick="scrollToTop()">
        <i class="fas fa-arrow-up"></i>
    </div>

    <script>
        // Create floating particles
        function createParticles() {
            const particles = document.querySelector('.particles');
            for (let i = 0; i < 50; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 15 + 's';
                particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
                particles.appendChild(particle);
            }
        }
        createParticles();

        // Navbar scroll effect
        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            const backToTop = document.querySelector('.back-to-top');
            
            if (window.pageYOffset > 100) {
                navbar.classList.add('scrolled');
                backToTop.classList.add('visible');
            } else {
                navbar.classList.remove('scrolled');
                backToTop.classList.remove('visible');
            }
        });

        // Smooth scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }

        // Intersection Observer for animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                }
            });
        }, observerOptions);

        document.addEventListener('DOMContentLoaded', function() {
            const elements = document.querySelectorAll('.animate-on-scroll');
            elements.forEach(el => observer.observe(el));
        });

        // Add typing effect to hero title
        const heroTitle = document.querySelector('.hero h1');
        const text = heroTitle.textContent;
        heroTitle.textContent = '';
        let i = 0;
        
        function typeWriter() {
            if (i < text.length) {
                heroTitle.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        }
        
        setTimeout(typeWriter, 1000);
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Portfolio Server Starting...")
    print("="*50)
    print("📱 Open your browser at: http://localhost:5000")
    print("🌐 Or access from network: http://0.0.0.0:5000")
    print("⏹️  Press CTRL+C to stop the server")
    print("="*50 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)