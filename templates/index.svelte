<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Khan's W Free Optimization Tool</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0a0a;
            color: #ffffff;
            line-height: 1.6;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header */
        .header {
            background: rgba(10, 10, 10, 0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            transition: all 0.3s ease;
        }

        .nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0;
        }

        .logo {
            font-size: 2rem;
            font-weight: 900;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo img {
            height: 40px;
            width: auto;
            filter: drop-shadow(0 0 10px rgba(102, 126, 234, 0.3));
        }

        /* Alternative: Logo only (no text) */
        .logo-image-only {
            height: 45px;
            width: auto;
            filter: drop-shadow(0 0 10px rgba(102, 126, 234, 0.3));
        }

        .nav-links {
            display: flex;
            gap: 30px;
            list-style: none;
        }

        .nav-links a {
            color: #ffffff;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
            padding: 8px 16px;
            border-radius: 8px;
        }

        .nav-links a:hover {
            color: #667eea;
            background: rgba(102, 126, 234, 0.1);
        }

        /* Hero Section */
        .hero {
            padding: 120px 0 80px;
            text-align: center;
            background: radial-gradient(ellipse at center, rgba(102, 126, 234, 0.1) 0%, transparent 70%);
        }

        .hero h1 {
            font-size: 4.5rem;
            font-weight: 900;
            margin-bottom: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.1;
        }

        .hero-subtitle {
            font-size: 1.5rem;
            color: #a0a0a0;
            margin-bottom: 40px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .cta-button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 16px 32px;
            border: none;
            border-radius: 12px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }

        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
        }

        /* Stats Section */
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin: 60px 0;
        }

        .stat-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.02) 0%, rgba(255, 255, 255, 0.05) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 30px;
            text-align: center;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
            border-color: rgba(102, 126, 234, 0.3);
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 900;
            color: #667eea;
            margin-bottom: 10px;
            display: block;
        }

        .stat-label {
            color: #a0a0a0;
            font-size: 1.1rem;
            font-weight: 500;
        }

        /* Features Section */
        .section {
            padding: 80px 0;
        }

        .section-title {
            font-size: 2.5rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 60px;
            color: #ffffff;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
        }

        .feature-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.02) 0%, rgba(255, 255, 255, 0.05) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 40px 30px;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }

        .feature-card:hover {
            transform: translateY(-5px);
            border-color: rgba(102, 126, 234, 0.3);
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
        }

        .feature-icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            margin-bottom: 20px;
        }

        .feature-title {
            font-size: 1.4rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 15px;
        }

        .feature-description {
            color: #a0a0a0;
            line-height: 1.6;
        }

        /* Download Section */
        .download-section {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 1px solid rgba(102, 126, 234, 0.2);
            border-radius: 20px;
            padding: 60px 40px;
            text-align: center;
            margin: 60px 0;
        }

        .download-title {
            font-size: 2.2rem;
            font-weight: 800;
            margin-bottom: 20px;
            color: #ffffff;
        }

        .download-subtitle {
            color: #a0a0a0;
            font-size: 1.1rem;
            margin-bottom: 40px;
        }

        .download-buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }

        .download-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
        }

        .download-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }

        .download-btn.secondary {
            background: transparent;
            border: 2px solid rgba(102, 126, 234, 0.5);
            color: #667eea;
        }

        .download-btn.secondary:hover {
            background: rgba(102, 126, 234, 0.1);
            border-color: #667eea;
        }

        /* Footer */
        .footer {
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding: 40px 0;
            text-align: center;
            margin-top: 80px;
        }

        .footer-content {
            color: #666;
            margin-bottom: 20px;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }

        .footer-links a {
            color: #a0a0a0;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .footer-links a:hover {
            color: #667eea;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }
            
            .hero h1 {
                font-size: 3rem;
            }
            
            .stats {
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
            }
            
            .features-grid {
                grid-template-columns: 1fr;
            }
            
            .download-buttons {
                flex-direction: column;
                align-items: center;
            }
        }

        /* Animations */
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

        .animate-on-scroll {
            animation: fadeInUp 0.8s ease forwards;
        }

        /* Interactive elements */
        .interactive-demo {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.02) 0%, rgba(255, 255, 255, 0.05) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 40px;
            margin: 40px 0;
            text-align: center;
        }

        .demo-controls {
            display: flex;
            gap: 15px;
            justify-content: center;
            margin: 20px 0;
            flex-wrap: wrap;
        }

        .demo-btn {
            background: rgba(102, 126, 234, 0.2);
            border: 1px solid rgba(102, 126, 234, 0.3);
            color: #667eea;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .demo-btn:hover {
            background: rgba(102, 126, 234, 0.3);
            transform: translateY(-1px);
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <nav class="nav">
                <div class="logo">Khan's W Tweaking</div>
                <ul class="nav-links">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#features">Features</a></li>
                    <li><a href="#download">Download</a></li>
                    <li><a href="#about">About</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="container">
            <h1>Optimize Your PC Performance</h1>
            <p class="hero-subtitle">Khan's W Tweaking Utility provides advanced system optimizations to boost your FPS, reduce latency, and unlock your PC's true gaming potential.</p>
            <a href="#download" class="cta-button">
                <span>⬇️</span>
                Download KWTW
            </a>
        </div>
    </section>

    <!-- Stats Section -->
    <section class="container">
        <div class="stats">
            <div class="stat-card">
                <span class="stat-number" id="users-count">50,000+</span>
                <div class="stat-label">Active Users</div>
            </div>
            <div class="stat-card">
                <span class="stat-number" id="fps-boost">+60</span>
                <div class="stat-label">Average FPS Boost</div>
            </div>
            <div class="stat-card">
                <span class="stat-number" id="latency-reduction">-25ms</span>
                <div class="stat-label">Latency Reduction</div>
            </div>
            <div class="stat-card">
                <span class="stat-number" id="satisfaction">98%</span>
                <div class="stat-label">User Satisfaction</div>
            </div>
        </div>
    </section>

    <!-- Interactive Demo -->
    <section class="container">
        <div class="interactive-demo">
            <h3>Performance Demo</h3>
            <p>See the difference KWTW makes to your system performance</p>
            <div class="stats" style="margin: 30px 0;">
                <div class="stat-card">
                    <span class="stat-number" id="demo-before">45</span>
                    <div class="stat-label">FPS Before</div>
                </div>
                <div class="stat-card">
                    <span class="stat-number" id="demo-after">45</span>
                    <div class="stat-label">FPS After</div>
                </div>
            </div>
            <div class="demo-controls">
                <button class="demo-btn" onclick="simulateOptimization()">🚀 Run Optimization</button>
                <button class="demo-btn" onclick="resetDemo()">🔄 Reset Demo</button>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="section" id="features">
        <div class="container">
            <h2 class="section-title">Powerful Features</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🎮</div>
                    <h3 class="feature-title">Game Optimization</h3>
                    <p class="feature-description">Automatically detect and optimize settings for over 1000+ popular games to maximize performance.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3 class="feature-title">System Tweaks</h3>
                    <p class="feature-description">Apply dozens of proven registry and system optimizations to reduce latency and boost FPS.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">🌐</div>
                    <h3 class="feature-title">Network Optimization</h3>
                    <p class="feature-description">Optimize TCP settings, DNS configuration, and network adapters for lower ping and stable connection.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">🗑️</div>
                    <h3 class="feature-title">System Cleanup</h3>
                    <p class="feature-description">Remove bloatware, temporary files, and unnecessary processes that slow down your system.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">⚙️</div>
                    <h3 class="feature-title">Power Management</h3>
                    <p class="feature-description">Create custom power plans optimized for gaming performance with intelligent CPU and GPU scaling.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">📊</div>
                    <h3 class="feature-title">Real-time Monitoring</h3>
                    <p class="feature-description">Monitor FPS, temperatures, and system resources in real-time with customizable overlays.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Download Section -->
    <section class="container" id="download">
        <div class="download-section">
            <h2 class="download-title">Ready to Optimize?</h2>
            <p class="download-subtitle">Download Khan's W Free Tweaking Utility and experience the difference in your gaming performance</p>
            <div class="download-buttons">
                <a href="#" class="download-btn" onclick="startDownload()">
                    <span>⬇️</span>
                    Download for Windows
                </a>
                <a href="#" class="download-btn secondary">
                    <span>📖</span>
                    User Guide
                </a>
            </div>
            <p style="color: #666; margin-top: 20px; font-size: 0.9rem;">
                Windows 10/11 • 64-bit • Free to use
            </p>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <p>&copy; 2024 KWTU. Made for gamers, by gamers.</p>
            </div>
            <div class="footer-links">
                <a href="#privacy">Privacy Policy</a>
                <a href="#terms">Terms of Service</a>
                <a href="#support">Support</a>
                <a href="#github">GitHub</a>
            </div>
        </div>
    </footer>

    <script>
        // Smooth scrolling for navigation links
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

        // Header scroll effect
        window.addEventListener('scroll', () => {
            const header = document.querySelector('.header');
            if (window.scrollY > 100) {
                header.style.background = 'rgba(10, 10, 10, 0.98)';
                header.style.borderBottom = '1px solid rgba(102, 126, 234, 0.2)';
            } else {
                header.style.background = 'rgba(10, 10, 10, 0.95)';
                header.style.borderBottom = '1px solid rgba(255, 255, 255, 0.1)';
            }
        });

        // Interactive demo functions
        function simulateOptimization() {
            const beforeElement = document.getElementById('demo-before');
            const afterElement = document.getElementById('demo-after');
            
            let currentFPS = 45;
            let targetFPS = 105;
            
            const interval = setInterval(() => {
                if (currentFPS < targetFPS) {
                    currentFPS += Math.floor(Math.random() * 5) + 1;
                    afterElement.textContent = Math.min(currentFPS, targetFPS);
                } else {
                    clearInterval(interval);
                    afterElement.style.color = '#00ff88';
                    
                    // Add success message
                    setTimeout(() => {
                        const demo = document.querySelector('.interactive-demo');
                        const successMsg = document.createElement('div');
                        successMsg.innerHTML = '<p style="color: #00ff88; margin-top: 20px; font-weight: 600;">🎉 Optimization Complete! +60 FPS gained!</p>';
                        demo.appendChild(successMsg);
                        
                        setTimeout(() => {
                            successMsg.remove();
                        }, 3000);
                    }, 500);
                }
            }, 100);
        }

        function resetDemo() {
            const beforeElement = document.getElementById('demo-before');
            const afterElement = document.getElementById('demo-after');
            
            beforeElement.textContent = '45';
            afterElement.textContent = '45';
            afterElement.style.color = '#667eea';
        }

        function startDownload() {
            // Simulate download
            const btn = event.target;
            const originalText = btn.innerHTML;
            
            btn.innerHTML = '<span>⏳</span> Preparing Download...';
            btn.style.background = 'rgba(102, 126, 234, 0.5)';
            
            setTimeout(() => {
                btn.innerHTML = '<span>✅</span> Download Started!';
                btn.style.background = 'linear-gradient(135deg, #00ff88 0%, #00cc6a 100%)';
                
                setTimeout(() => {
                    btn.innerHTML = originalText;
                    btn.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
                }, 2000);
            }, 1500);
        }

        // Animate stats on page load
        function animateStats() {
            const stats = [
                { element: document.getElementById('users-count'), target: 50000, suffix: '+' },
                { element: document.getElementById('fps-boost'), target: 60, prefix: '+' },
                { element: document.getElementById('latency-reduction'), target: -25, suffix: 'ms' },
                { element: document.getElementById('satisfaction'), target: 98, suffix: '%' }
            ];

            stats.forEach(stat => {
                let current = 0;
                const increment = stat.target / 50;
                const timer = setInterval(() => {
                    current += increment;
                    if ((increment > 0 && current >= stat.target) || (increment < 0 && current <= stat.target)) {
                        clearInterval(timer);
                        current = stat.target;
                    }
                    
                    const prefix = stat.prefix || '';
                    const suffix = stat.suffix || '';
                    stat.element.textContent = prefix + Math.floor(Math.abs(current)).toLocaleString() + suffix;
                }, 50);
            });
        }

        // Run animations when page loads
        window.addEventListener('load', animateStats);
    </script>
</body>
</html>