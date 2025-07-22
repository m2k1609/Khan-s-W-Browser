<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VTRL - Python Browser Test</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0a0a, #1a1a2e, #16213e);
            color: #ffffff;
            min-height: 100vh;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .hero-section {
            text-align: center;
            padding: 80px 0;
            background: linear-gradient(45deg, #0f0f23, #1a1a2e);
            border-radius: 20px;
            margin-bottom: 40px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .hero-title {
            font-size: 4rem;
            font-weight: 900;
            background: linear-gradient(45deg, #00d4ff, #ff007f, #00ff88);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 3s ease-in-out infinite;
            margin-bottom: 20px;
            text-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
        }
        
        .hero-subtitle {
            font-size: 1.5rem;
            color: #00d4ff;
            margin-bottom: 10px;
            font-weight: 600;
        }
        
        .tagline {
            font-size: 1.2rem;
            color: #cccccc;
            margin-bottom: 40px;
        }
        
        .fps-counter {
            display: flex;
            justify-content: center;
            gap: 60px;
            margin: 40px 0;
            flex-wrap: wrap;
        }
        
        .fps-display {
            text-align: center;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            border: 1px solid rgba(0, 212, 255, 0.3);
            backdrop-filter: blur(10px);
        }
        
        .fps-label {
            color: #888;
            font-size: 1rem;
            margin-bottom: 10px;
        }
        
        .fps-number {
            font-size: 3rem;
            font-weight: 900;
            color: #00d4ff;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        }
        
        .cta-button {
            background: linear-gradient(45deg, #00d4ff, #ff007f);
            color: white;
            padding: 15px 40px;
            border: none;
            border-radius: 50px;
            font-size: 1.2rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
        }
        
        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(0, 212, 255, 0.5);
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin: 60px 0;
        }
        
        .feature-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 30px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            border-color: rgba(0, 212, 255, 0.5);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }
        
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 20px;
            display: block;
        }
        
        .feature-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #00d4ff;
            margin-bottom: 15px;
        }
        
        .feature-description {
            color: #cccccc;
            line-height: 1.6;
        }
        
        .nav {
            background: rgba(0, 0, 0, 0.8);
            padding: 15px 0;
            margin-bottom: 20px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }
        
        .nav a {
            color: #cccccc;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 25px;
            transition: all 0.3s ease;
            font-weight: 500;
        }
        
        .nav a:hover {
            background: rgba(0, 212, 255, 0.2);
            color: #00d4ff;
            transform: translateY(-2px);
        }
        
        .form-section {
            background: rgba(255, 255, 255, 0.05);
            padding: 40px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            margin: 40px 0;
        }
        
        .section-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #00d4ff;
            margin-bottom: 30px;
            text-align: center;
        }
        
        .form-group {
            margin: 20px 0;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            color: #00d4ff;
            font-weight: 600;
        }
        
        input, textarea {
            width: 100%;
            padding: 15px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            color: #ffffff;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        input:focus, textarea:focus {
            outline: none;
            border-color: #00d4ff;
            box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
        }
        
        input::placeholder, textarea::placeholder {
            color: #888;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 30px 0;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            overflow: hidden;
        }
        
        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        th {
            background: rgba(0, 212, 255, 0.2);
            color: #00d4ff;
            font-weight: 700;
        }
        
        .status-complete { color: #00ff88; }
        .status-progress { color: #ffaa00; }
        .status-planned { color: #888; }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .alert {
            background: linear-gradient(45deg, rgba(0, 255, 136, 0.1), rgba(0, 212, 255, 0.1));
            color: #00ff88;
            padding: 20px;
            border-radius: 15px;
            border: 1px solid rgba(0, 255, 136, 0.3);
            margin: 20px 0;
            text-align: center;
            font-weight: 600;
        }
        
        #js-output {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin: 20px 0;
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
    </style>
</head>
<body>
    <div class="nav">
        <div class="nav-container">
            <a href="#home">Home</a>
            <a href="#features">Features</a>
            <a href="#download">Download</a>
            <a href="#about">About</a>
            <a href="https://www.python.org" target="_blank">Python.org</a>
        </div>
    </div>

    <div class="container">
        <div class="hero-section">
            <h1 class="hero-title">VTRL</h1>
            <div class="hero-subtitle">Your PC F***ing Sucks.</div>
            <div class="tagline">Boost FPS, decrease response times, eliminate ping and get rid of crap.</div>
            
            <div class="fps-counter">
                <div class="fps-display">
                    <div class="fps-label">Before:</div>
                    <div class="fps-number" id="fps-before">0</div>
                    <div class="fps-label">FPS</div>
                </div>
                <div class="fps-display">
                    <div class="fps-label">After:</div>
                    <div class="fps-number" id="fps-after">0</div>
                    <div class="fps-label">FPS</div>
                </div>
            </div>
            
            <a href="#download" class="cta-button">Download VTRL</a>
        </div>

        <div class="alert">
            <strong>🚀 Browser Test Active!</strong> If you can see this styled page with animations, your Python browser is handling advanced CSS correctly!
        </div>

        <div class="section-title">All-In-One Utility</div>
        
        <div class="features-grid">
            <div class="feature-card">
                <span class="feature-icon">🎮</span>
                <div class="feature-title">General Tweaks</div>
                <div class="feature-description">Dozens of optimizations to enhance overall system performance and unlock your PC's true potential.</div>
            </div>
            
            <div class="feature-card">
                <span class="feature-icon">⚡</span>
                <div class="feature-title">Latency Optimization</div>
                <div class="feature-description">Reduce input lag and system response times for a smoother, more responsive gaming experience.</div>
            </div>
            
            <div class="feature-card">
                <span class="feature-icon">🌐</span>
                <div class="feature-title">Network Enhancements</div>
                <div class="feature-description">Optimize your network settings for lower ping and better connectivity in online games.</div>
            </div>
            
            <div class="feature-card">
                <span class="feature-icon">⚙️</span>
                <div class="feature-title">Power Plan Configurator</div>
                <div class="feature-description">Create and apply custom power plans to balance performance and energy efficiency.</div>
            </div>
            
            <div class="feature-card">
                <span class="feature-icon">🧹</span>
                <div class="feature-title">System Cleaner</div>
                <div class="feature-description">Remove unnecessary files and optimize storage for improved system responsiveness.</div>
            </div>
            
            <div class="feature-card">
                <span class="feature-icon">🗑️</span>
                <div class="feature-title">Debloat Utility</div>
                <div class="feature-description">Remove unwanted bloatware and organize your system for peak performance.</div>
            </div>
        </div>

        <div class="section-title">Interactive Test Elements</div>
        <div style="text-align: center; margin: 30px 0;">
            <button class="cta-button" onclick="simulateBoost()" style="margin: 0 10px;">Simulate FPS Boost</button>
            <button class="cta-button" onclick="resetCounters()" style="margin: 0 10px;">Reset Counters</button>
        </div>

        <div class="form-section">
            <div class="section-title">Browser Testing Form</div>
            <form onsubmit="handleSubmit(event)">
                <div class="form-group">
                    <label for="name">Username:</label>
                    <input type="text" id="name" name="name" placeholder="Enter your gaming username">
                </div>
                
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" placeholder="Enter your email">
                </div>
                
                <div class="form-group">
                    <label for="message">Performance Feedback:</label>
                    <textarea id="message" name="message" rows="4" placeholder="Tell us about your system's performance..."></textarea>
                </div>
                
                <div style="text-align: center;">
                    <button type="submit" class="cta-button">Submit Feedback</button>
                </div>
            </form>
        </div>

        <div class="section-title">Browser Feature Status</div>
        <table>
            <thead>
                <tr>
                    <th>Browser Component</th>
                    <th>Status</th>
                    <th>Performance Impact</th>
                    <th>Priority</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>HTML Parsing Engine</td>
                    <td class="status-complete">✅ Optimized</td>
                    <td>+60 FPS</td>
                    <td>Critical</td>
                </tr>
                <tr>
                    <td>CSS Rendering Pipeline</td>
                    <td class="status-progress">🔄 Boosting</td>
                    <td>+45 FPS</td>
                    <td>Critical</td>
                </tr>
                <tr>
                    <td>JavaScript V8 Engine</td>
                    <td class="status-planned">⏳ Queued</td>
                    <td>+30 FPS</td>
                    <td>High</td>
                </tr>
                <tr>
                    <td>Image Loading Cache</td>
                    <td class="status-complete">✅ Optimized</td>
                    <td>+25 FPS</td>
                    <td>Medium</td>
                </tr>
                <tr>
                    <td>Network Optimization</td>
                    <td class="status-progress">🔄 Boosting</td>
                    <td>-50ms Latency</td>
                    <td>High</td>
                </tr>
            </tbody>
        </table>

        <div class="section-title" id="test">Python Browser Dev Stack</div>
        <div class="features-grid">
            <div class="feature-card">
                <span class="feature-icon">🐍</span>
                <div class="feature-title">Core Framework</div>
                <div class="feature-description">PyQt6/PySide6 for maximum performance with native rendering capabilities and GPU acceleration support.</div>
            </div>
            
            <div class="feature-card">
                <span class="feature-icon">🌐</span>
                <div class="feature-title">Web Engine</div>
                <div class="feature-description">QWebEngineView with Chromium backend for modern web standards and JavaScript execution.</div>
            </div>
            
            <div class="feature-card">
                <span class="feature-icon">⚡</span>
                <div class="feature-title">Performance Tweaks</div>
                <div class="feature-description">Custom CSS injection, ad blocking, and resource optimization for lightning-fast page loads.</div>
            </div>
        </div>

        <div class="section-title">Real-time Performance Monitor</div>
        <div id="js-output">
            <span style="color: #888;">Initializing performance monitoring...</span>
        </div>
    </div>

    <script>
        function changeColor() {
            const colors = ['#f4f4f4', '#e8f4f8', '#f0f8e8', '#f8f0e8', '#f8e8f0'];
            const randomColor = colors[Math.floor(Math.random() * colors.length)];
            document.body.style.backgroundColor = randomColor;
        }

        function handleSubmit(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            
            document.getElementById('js-output').innerHTML = `
                <strong>Form Submitted!</strong><br>
                Name: ${name}<br>
                Email: ${email}<br>
                Message: ${message}
            `;
        }

        // Test basic DOM manipulation
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('js-output').innerHTML = 
                '<strong>JavaScript is working!</strong> DOM loaded successfully.';
        });
    </script>
    
</body>
</html>